"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError

class CpsVoyage(models.Model):

    _name = 'cps.voyage'
    _description = "Liste des voyages"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    progress = fields.Float("Progression", compute='compute_progress_state', store=True, group_operator="avg", help="Display progress of current task.")

    state_national = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('attente_liv','Att. livr.'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_cch = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('dedouanement','Dédouanement'), ('handling','Handling'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_dap = fields.Selection([('pret','Pret'),('attente_doc','Att. Doc.'), ('echange','En echange'),  ('dedouanement','Dédouanement'), ('attente_chargement','Att. Char.'), ('charge','Chargé'), ('route','En route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_fret = fields.Selection([('pret','Pret'),('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('landing','Landing'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_obc = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('take_off','Take off'),('landed','Landed'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_charter_dtd = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('take_off','Take off'),('landed','Landed'),('released','Released'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_routier = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_routier_transbordement = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('transbordement','Transbordement'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_general =  fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('transbordement','Transbordement'),('route_2','En Route'), ('livre','Livré'),('charge','Chargé'), ('attente_liv','Att. Liv.'),('handling','Handling'),('echange','Echange'),('landing','Landing'),('en_board','On board'),('take_off','Take off'),('landed','Landed'),('released','Released'),('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')

    priorite = fields.Selection([('faible','Faible'),('moyen','Moyen'),('eleve','Elevé'), ('prioritaire','Prioritaire')], string='Priorité', default='faible')
    tracking_ids = fields.One2many('cps.voyage.tracking', 'voyage_id', string='Tracking du voyage')
    resume_ids = fields.One2many('cps.voyage.resume', 'voyage_id', string='Résumé du voyage')
    date= fields.Datetime(string="Date")
    default_code = fields.Char("N° Voyage")
    client_id = fields.Many2one("res.partner", string='Client', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 0),('is_company', '=', True)])
    ref_client = fields.Char("Référence Client")
    type_ramassage = fields.Selection([('ftl','F.T.L.'), ('groupage','Groupage')], string='Type ramassage', default='ftl')
    colisage_ids = fields.One2many('cps.colisage', 'voyage_id', string='Liste des colis')

    facture_achat_ids = fields.One2many('account.move', 'voyage_id', domain=[('move_type', '=', 'in_invoice')], string="Factures d'achat")
    total_facture_achats = fields.Float('Factures achats', compute="compute_facture_achat_amount")
    facture_vente_ids = fields.One2many('account.move', 'voyage_id', domain=[('move_type', '=', 'out_invoice')], string="Factures de vente")
    total_facture_vente = fields.Float('Factures ventes', compute="compute_facture_vente_amount")

    commande_achat_ids = fields.One2many('purchase.order', 'voyage_id', string="Factures d'achat")
    total_commandes_achats = fields.Float('Commandes achats', compute="compute_commande_achat_amount")
    commande_vente_ids = fields.One2many('sale.order', 'voyage_id', string="Factures de vente")
    total_commandes_vente = fields.Float('Commandes ventes', compute="compute_commande_vente_amount")

    type_voyage  = fields.Selection([('national','National'), ('international','International')], string='Type', default='national')
    type_trajet = fields.Selection([('import','Import'), ('export','Export')], string='Direction', default='export')
    type_parcours = fields.Selection([('oneway','Single trip'), ('round','Round trip')], string='Parcours', default='oneway')
    type_operation = fields.Selection([('cch','CCH'), ('dap','DAP'), ('fret','Fret Aerien'), ('obc','OBC'), ('charter','Charter'), ('dtd','DTD'), ('routier','Routier'), ('routier-trans','Routier avec Transbordement')], string='Transport', default='cch')

    ton = fields.Char("TON")
    ref_tmc = fields.Char("Ref TMC")
    # prestation_id = fields.Many2one("cps.prestation", string='Type préstation')
    name = fields.Char('Nom du voyage', compute='compute_name', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)
    currency_id = fields.Many2one(related="company_id.currency_id", string="devise")

    lieu_ramassage = fields.Many2one("res.partner", string='Lieu de ramassage', domain=[('type','=', 'delivery')], required=True)
    lieu_livraison = fields.Many2one("res.partner", string='Lieu de livraison', domain=[('type','=', 'delivery')], required=True)
    ville_ramassage = fields.Many2one("res.city", related='lieu_ramassage.ville', string='Ville ramassage', store=True)
    ville_livraison = fields.Many2one("res.city",related='lieu_livraison.ville', string='Ville livraison', store=True)

    cout_trajet = fields.Float(string="Cout du trajet", store=True)
    cout_total = fields.Monetary( compute='compute_cout', string="Cout total", store=True)
    marge = fields.Float('Marge (%)')
    prix = fields.Monetary(string="Prix de vente", compute='compute_price' , store=True)
    sous_traitance_1 = fields.Boolean('Sous-traitance ?')
    vehicule_parc_1 = fields.Many2one('fleet.vehicle', 'Vehicule parc', domain=[('soustraitant_id', '=', False)])
    mat_vehicule_parc_1 = fields.Char('Matricule', related='vehicule_parc_1.license_plate')
    vehicule_sous_traitant_1 = fields.Many2one('cps.soustraitant', 'Vehicule sous-traitant')
    cout_sous_traitant_1 = fields.Monetary(string="Cout")
    mat_vehicule_sous_traitant_1 = fields.Char('Matricule', related='vehicule_sous_traitant_1.vehicule_id.license_plate')
    # ----CCH fields--------
    dedouanement_1 = fields.Many2one("res.partner", string='Transitaire', domain=[('is_transitaire', '=', True),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transitaire_1 = fields.Monetary(string="Cout")
    handling = fields.Many2one("res.partner", string='Handling', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', True),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_handling = fields.Monetary(string="Cout")
    porteur = fields.Monetary(string="Porteurs")

    #-----DAP------------
    n_lta = fields.Char(string='N° LTA')
    echange= fields.Many2one("res.partner", string='Echange', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', True),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_echange = fields.Monetary(string="Cout")


    #--------- FRET--------------
    fret = fields.Many2one("res.partner", string='Fret', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', True),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_fret = fields.Monetary(string="Cout fret")

    #OBC
    cout_bagage = fields.Monetary(string="Excédent bagage")
    frais_divers = fields.Monetary(string="Frais divers")
    dedouanement_2 = fields.Many2one("res.partner", string='Transitaire', domain=[('is_transitaire', '=', True),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transitaire_2 = fields.Monetary(string="Cout")
    sous_traitance_2 = fields.Boolean('Sous-traitance ?')
    vehicule_parc_2 = fields.Many2one('fleet.vehicle', 'Vehicule parc', domain=[('soustraitant_id', '=', False)])
    mat_vehicule_parc_2 = fields.Char('Matricule', related='vehicule_parc_2.license_plate')
    vehicule_sous_traitant_2 = fields.Many2one('cps.soustraitant', 'Vehicule sous_traitant')
    mat_vehicule_sous_traitant_2 = fields.Char('Matricule', related='vehicule_sous_traitant_2.vehicule_id.license_plate')
    cout_sous_traitant_2 = fields.Monetary(string="Cout")


    #INTER-ROUTIER
    bateau = fields.Many2one("res.partner", string='Bateau', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', True),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_bateau = fields.Monetary(string="Cout")
    dedouanement_zf = fields.Many2one("res.partner", string='Transitaire ZF', domain=[('is_transitaire', '=', True),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transitaire_zf = fields.Monetary(string="Cout")

    #INTER-ROUTIER TRANSBORDEMENT
    transbordement = fields.Many2one("res.partner", string='Transbordement', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', True),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transbordement = fields.Monetary(string="Cout")

    # @api.onchange('vehicule_sous_traitant_1')
    # def onchange_vehicule_soustraitant(self):
    #     vehicule_sous_traitant = self.env['cps.soustraitant.price'].search([('trajet_id', '=', self.trajet_id.id),('vehicule_sous_traitant_1', '=', self.vehicule_sous_traitant_1.id)],order='id desc', limit=1)
    #     self.cout_sous_traitant_1 = vehicule_sous_traitant.price
    #     if self.type_voyage=='national':
    #         self.cout_trajet = self.cout_sous_traitant_1

    @api.model
    def create (self, vals):
        vals['default_code'] = self.env['ir.sequence'].next_by_code('cps.voyage')
        result = super ( CpsVoyage, self).create(vals)
        self.env['cps.voyage.tracking'].create({'voyage_id': result.id, 'date_tracking': fields.Datetime.now(), 'description': dict(self._fields['state_national'].selection).get(self.state_national)})
        result.calculer_resume()
        return result

    def write(self, values):
        voyage = super(CpsVoyage, self).write(values)
        self.calculer_resume()
        self.compute_state(values)
        return voyage

    @api.depends('ville_ramassage','ville_livraison','vehicule_parc_1','vehicule_sous_traitant_1','type_voyage','client_id')
    def compute_price(self):
        if self.vehicule_parc_1 is not False:
            trajet_price = self.env['cps.trajet.lines'].search([('lieu_ramassage', '=', self.ville_ramassage.id),('lieu_livraison', '=', self.ville_livraison.id),('type_vehicule', '=', self.vehicule_parc_1.type_vehicule),('type_voyage', '=', self.type_parcours),('partner_id', '=', self.client_id.id)])
        if self.vehicule_sous_traitant_1 is not False:
            trajet_price = self.env['cps.trajet.lines'].search([('lieu_ramassage', '=', self.ville_ramassage.id),('lieu_livraison', '=', self.ville_livraison.id),('type_vehicule', '=', self.vehicule_sous_traitant_1.vehicule_id.type_vehicule),('type_voyage', '=', self.type_parcours),('partner_id', '=', self.client_id.id)])
        self.prix = trajet_price.cout


    @api.depends('state_national','state_cch','state_dap','state_fret','state_charter_dtd','state_routier','state_routier_transbordement')
    def compute_progress_state(self):
        i=0
        progress=0
        for s in self:
            if s.type_voyage=='national':
                if s.state_national!="pret" and s.state_national!="bloque" and  s.state_national!="annule" :
                    for state in dict(s._fields['state_national'].selection).keys():
                        i+=1
                        if state==s.state_national:
                            progress=i / (len(dict(s._fields['state_national'].selection))-2)*100
            if s.type_operation=="cch":
                if s.state_cch!="pret" and s.state_cch!="bloque" and  s.state_cch!="annule" :
                    for state in dict(s._fields['state_cch'].selection).keys():
                        i+=1
                        if state==s.state_cch:
                            progress=i / (len(dict(s._fields['state_cch'].selection))-2)*100
            if s.type_operation=="dap":
                if s.state_dap!="pret" and s.state_dap!="bloque" and  s.state_dap!="annule" :
                    for state in dict(s._fields['state_dap'].selection).keys():
                        i+=1
                        if state==s.state_dap:
                            progress=i / (len(dict(s._fields['state_dap'].selection))-2)*100
            if s.type_operation=="fret":
                if s.state_fret!="pret" and s.state_fret!="bloque" and  s.state_fret!="annule" :
                    for state in dict(s._fields['state_fret'].selection).keys():
                        i+=1
                        if state==s.state_fret:
                            progress=i / (len(dict(s._fields['state_fret'].selection))-2)*100
            if s.type_operation=="charter" or s.type_operation=="dtd":
                if s.state_charter_dtd!="pret" and s.state_charter_dtd!="bloque" and  s.state_charter_dtd!="annule" :
                    for state in dict(s._fields['state_charter_dtd'].selection).keys():
                        i+=1
                        if state==s.state_charter_dtd:
                            progress=i / (len(dict(s._fields['state_charter_dtd'].selection))-2)*100
            if s.type_operation=="routier":
                if s.state_routier!="pret" and s.state_routier!="bloque" and  s.state_routier!="annule" :
                    for state in dict(s._fields['state_routier'].selection).keys():
                        i+=1
                        if state==s.state_routier:
                            progress=i / (len(dict(s._fields['state_routier'].selection))-2)*100
            if s.type_operation=="routier_transbordement-trans":
                if s.state_routier_transbordement!="pret" and s.state_routier_transbordement!="bloque" and  s.state_routier_transbordement!="annule" :
                    for state in dict(s._fields['state_routier_transbordement'].selection).keys():
                        i+=1
                        if state==s.state_routier_transbordement:
                            progress=i / (len(dict(s._fields['state_routier_transbordement'].selection))-2)*100
            s.progress = progress

    def compute_state(self, values):
        for p in self:
            last_tracking = p.env['cps.voyage.tracking'].search([('voyage_id', '=', p.id)],order='id desc', limit=1)
            time_elapsed=0
            if len(last_tracking)>0:
                time_elapsed = (fields.Datetime.now()-last_tracking.date_tracking).total_seconds() / 60.0
            last_tracking.duree = time_elapsed
            if 'state_national' in values:
                if values['state_national']:
                    p.env['cps.voyage.tracking'].create({'voyage_id': p.id,'date_tracking':fields.Datetime.now(),'description': dict(p._fields['state_national'].selection).get(p.state_national)})
                    p.state_general = p.state_national
            elif 'state_cch' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_cch'].selection).get(p.state_cch)})
                p.state_general = p.state_cch
            elif 'state_dap' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_dap'].selection).get(p.state_dap)})
                p.state_general = p.state_dap
            elif 'state_fret' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_fret'].selection).get(p.state_fret)})
                p.state_general = p.state_fret
            elif 'state_obc' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_obc'].selection).get(p.state_obc)})
                p.state_general = p.state_obc
            elif 'state_charter_dtd' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_charter_dtd'].selection).get(p.state_charter_dtd)})
                p.state_general = p.state_charter_dtd
            elif 'state_routier' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_routier'].selection).get(p.state_routier)})
                p.state_general = p.state_routier
            elif 'state_routier_transbordement' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_routier_transbordement'].selection).get(p.state_routier_transbordement)})
                p.state_general = p.state_routier_transbordement

    def calculer_resume(self):
        for p in self:
            p.resume_ids.unlink()
            if p.cout_trajet > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Cout du voyage ", 'cout': p.cout_trajet})
            if p.cout_sous_traitant_1 > 0:
                if len(p.vehicule_sous_traitant_1)>0:
                    product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.soustraitance_product'))])
                    p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Sous-traitance véhicule " + p.vehicule_sous_traitant_1.vehicule_id.name , 'type_prestataire':'sous-traitant', 'client_id': p.vehicule_sous_traitant_1.soustraitant_id.id, 'cout': p.cout_sous_traitant_1})
            if p.cout_transitaire_1 > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit " , 'type_prestataire':'transit', 'client_id': p.dedouanement_1.id, 'cout': p.cout_transitaire_1})
            if p.cout_handling > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.handling_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de handling " , 'type_prestataire':'aerienne', 'client_id': p.handling.id, 'cout': p.cout_handling})
            if p.cout_echange > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.echange_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais d'échange " , 'type_prestataire':'aerienne', 'client_id': p.echange.id, 'cout': p.cout_echange})
            if p.cout_fret > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de fret " , 'type_prestataire':'aerienne', 'client_id': p.fret.id, 'cout': p.cout_fret})
            if p.cout_bagage > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais d'excedent de bagage' " , 'type_prestataire':'aerienne', 'client_id': p.fret.id, 'cout': p.cout_bagage})
            if p.frais_divers > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais divers' " , 'type_prestataire':'autre', 'cout': p.frais_divers})
            if p.cout_transitaire_2 > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit " , 'type_prestataire':'transit', 'client_id': p.dedouanement_2.id, 'cout': p.cout_transitaire_2})
            if p.cout_sous_traitant_2 > 0:
                if len(p.vehicule_sous_traitant_2)>0:
                    product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                    p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Sous-traitance véhicule " + p.vehicule_sous_traitant_2.name , 'type_prestataire':'sous-traitant', 'client_id': p.vehicule_sous_traitant_2.soustraitant_id.id, 'cout': p.cout_sous_traitant_2})
            if p.cout_bateau > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de bateau " , 'type_prestataire':'maritine', 'client_id': p.bateau.id, 'cout': p.cout_bateau})
            if p.cout_transitaire_zf > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit en Z.F. ", 'type_prestataire':'transit', 'client_id': p.dedouanement_zf.id, 'cout': p.cout_transitaire_zf})
            if p.cout_transbordement > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.echange_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transbordement ", 'type_prestataire':'magasinnage', 'client_id': p.transbordement.id, 'cout': p.cout_transbordement})

    def action_generate_bill(self):
        # "creating cps facture"
        account_revenue = self.env['account.account'].search([('code', '=', '612630')])
        for p in self.resume_ids:
            if len(p.client_id) > 0:
                account_journal = self.env['account.journal'].search([('type', '=', 'purchase')], limit=1)
                invoice = self.env['account.move'].create({
                    'partner_id': p.client_id.id,
                    'partner_shipping_id': p.client_id.id,
                    'journal_id': account_journal.id,
                    'move_type': 'in_invoice',
                    'invoice_date': fields.Datetime.now(),
                    'invoice_payment_term_id': p.client_id.property_supplier_payment_term_id.id,
                    'currency_id': self.currency_id.id,
                    'name': '/',
                    'voyage_id' : self.id,
                    'invoice_line_ids' : [],
                    'state': 'draft',

                })
                invoice_line = []
                invoice_line.append((0, 0, {
                                                'quantity': 1,
                                                'price_unit': p.cout,
                                                'name': p.description,
                                                'account_id': account_revenue.id,
                                                # 'tax_ids': [(6, 0, sol.tax_id.ids if tax_id is not False else [])],
                                                'sale_line_ids': [],
                                                # 'facturation_line_id': facture_line.id
                                            }),
                                    )
                invoice.write({'invoice_line_ids': invoice_line})

    def action_generate_purchase_order(self):
        for p in self.resume_ids:
            if len(p.client_id) > 0:
                pOrder = self.env['purchase.order'].create({
                    'company_id': self.env.user.company_id.id,
                    'partner_id': self.client_id.id,
                    'voyage_id': self.id,
                    'date_order': fields.datetime.now(),
                    'date_planned': fields.datetime.now(),
                    'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
                    'order_line': [(0, 0, {
                                    'product_id': p.product_id.id,
                                    'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
                                    'name': p.description,
                                    'product_uom_qty': 1,
                                    'product_qty': 1,
                                    'qty_received': 1,
                                    'price_unit':p.cout,
                                    # 'product_uom' : self.product_id.uom_id.id,
                                    })]
                })
                pOrder.button_confirm()
                pOrder.date_planned = fields.datetime.now()

    def action_generate_sale_order(self):
        if self.client_id is not False:
            product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.vente_product'))])
            sOrder = self.env['sale.order'].create({
                'company_id': self.env.user.company_id.id,
                'partner_id': self.client_id.id,
                'voyage_id': self.id,
                'date_order': fields.datetime.now(),
                'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
                'order_line': [(0, 0, {
                                'product_id': product_id.id,
                                'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
                                'name': self.name,
                                'product_uom_qty': 1,
                                'qty_delivered': 1,
                                'price_unit': self.prix,
                                # 'product_uom' : self.product_id.uom_id.id,
                                })]
            })
            sOrder.action_confirm()

    def action_generate_invoice(self):
        # "creating cps facture"
        account_revenue = self.env['account.account'].search([('user_type_id', '=', self.env.ref('account.data_account_type_revenue').id)], limit=1)
        if self.client_id is not False:
            account_journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
            invoice = self.env['account.move'].create({
                'partner_id': self.client_id.id,
                'partner_shipping_id': self.client_id.id,
                'journal_id': account_journal.id,
                'move_type': 'out_invoice',
                'invoice_date': fields.Datetime.now(),
                'invoice_payment_term_id': self.client_id.property_payment_term_id.id,
                'currency_id': self.currency_id.id,
                'voyage_id': self.id,
                'name': '/',
                'invoice_line_ids': [],
                'state': 'draft',

            })
            invoice_line = []
            invoice_line.append((0, 0, {
                'quantity': 1,
                'price_unit': self.prix,
                # 'name': self.trajet_id.name,
                'account_id': account_revenue.id,
                # 'tax_ids': [(6, 0, sol.tax_id.ids if tax_id is not False else [])],
                'sale_line_ids': [],
                # 'facturation_line_id': facture_line.id
            }),
                                )
            invoice.write({'invoice_line_ids': invoice_line})

    def compute_facture_achat_amount(self):
        total=0
        for f in self.facture_achat_ids:
            total+=f.amount_untaxed_signed
        self.total_facture_achats = -total

    def compute_commande_achat_amount(self):
        total=0
        for f in self.commande_achat_ids:
            total+=f.amount_untaxed
        self.total_commandes_achats = total

    def action_view_factures_achat(self):
        if len(self.facture_achat_ids) > 0:
            result = {
                'name': "Liste des factures d'achat",
                'res_model': 'account.move',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.facture_achat_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else :
            raise UserError(_("Aucune facture n'est encore disponible"))

    def action_view_commandes_achat(self):
        if len(self.commande_achat_ids) > 0:
            result = {
                'name': "Liste des commandes d'achat",
                'res_model': 'purchase.order',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.commande_achat_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else :
            raise UserError(_("Aucune commande d'achat n'est encore disponible"))

    def compute_facture_vente_amount(self):
        total=0
        for f in self.facture_vente_ids:
            total+=f.amount_untaxed_signed
        self.total_facture_vente = total

    def compute_commande_vente_amount(self):
        total=0
        for f in self.commande_vente_ids:
            total+=f.amount_untaxed
        self.total_commandes_vente = total

    def action_view_factures_vente(self):
        if len(self.facture_vente_ids) > 0:
            result = {
                'name': "Liste des factures de vente",
                'res_model': 'account.move',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.facture_vente_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else :
            raise UserError(_("Aucune facture n'est encore disponible"))

    def action_view_commandes_vente(self):
        if len(self.commande_vente_ids) > 0:
            result = {
                'name': "Liste des commandes de vente",
                'res_model': 'sale.order',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.commande_vente_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else :
            raise UserError(_("Aucune commande de vente n'est encore disponible"))

    def action_view_vehicule_parc_1(self):
        result = {
            'name': "Liste des vehicules",
            'res_model': 'fleet.vehicle',
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'domain': [('id', '=', self.vehicule_parc_1.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
        return result

    def action_view_vehicule_parc_2(self):
        result = {
            'name': "Liste des vehicules",
            'res_model': 'fleet.vehicle',
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'domain': [('id', '=', self.vehicule_parc_2.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
        return result

    def action_view_vehicule_soustraitant_1(self):
        result = {
            'name': "Liste des vehicules",
            'res_model': 'fleet.vehicle',
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'domain': [('id', '=', self.vehicule_sous_traitant_1.vehicule_id.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
        return result

    def action_view_vehicule_soustraitant_2(self):
        result = {
            'name': "Liste des vehicules",
            'res_model': 'fleet.vehicle',
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'domain': [('id', '=', self.vehicule_sous_traitant_2.vehicule_id.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
        return result

    @api.depends('cout_trajet','cout_sous_traitant_1','cout_transitaire_1','cout_handling','cout_echange','cout_fret','cout_bagage','frais_divers','cout_transitaire_2','cout_sous_traitant_2','cout_bateau','cout_transitaire_zf','cout_transbordement')
    def compute_cout(self):
        for p in self:
            p.cout_total= p.cout_trajet+p.cout_sous_traitant_1+p.cout_transitaire_1+p.cout_handling+p.cout_echange + p.cout_fret + p.cout_bagage+ p.frais_divers+ p.cout_transitaire_2+ p.cout_sous_traitant_2+ p.cout_bateau+ p.cout_transitaire_zf+ p.cout_transbordement

    def set_price(self):
        for p in self:
            p.prix=p.cout_total+((p.cout_total*p.marge)/100)

    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            res.append((rec.id, name))
        return res

    # def get_name(self):
    #     for s in self:
    #         name = ""
    #         if s.default_code is not False:
    #             name = name + s.default_code
    #         if s.trajet_id is not False:
    #             name += " / " + s.trajet_id.name
    #         return name

    @api.depends('default_code')
    def compute_name(self):
        for s in self:
            name = ""
            print('s.default_code-----------------------',s.default_code)
            # print('s.trajet_id-----------------------',s.trajet_id)
            if s.default_code is not False:
                name = name + s.default_code
            # if len(s.trajet_id)>0:
            #     name += " / " + str(s.trajet_id.name)
            s.name = name

    @api.onchange('type_voyage')
    def on_change_type_voyage(self):
        self.type_operation=""