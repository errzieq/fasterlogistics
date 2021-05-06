"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError

class CpsVoyage(models.Model):

    _name = 'cps.voyage'
    _description = "Liste des voyages"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    progress = fields.Float("Progression", compute='compute_progress_state', store=True, group_operator="avg", help="Display progress of current task.")

    #STATES
    # state_cch = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('dedouanement','Dédouanement'), ('handling','Handling'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_dap = fields.Selection([('pret','Pret'),('attente_doc','Att. Doc.'), ('echange','En echange'),  ('dedouanement','Dédouanement'), ('attente_chargement','Att. Char.'), ('charge','Chargé'), ('route','En route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_fret = fields.Selection([('pret','Pret'),('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('landing','Landing'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_obc = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('take_off','Take off'),('landed','Landed'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_charter_dtd = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('take_off','Take off'),('landed','Landed'),('released','Released'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_routier = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    # state_routier_transbordement = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('transbordement','Transbordement'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_general =  fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('dedouanement_zf','Dédouanement ZF'), ('route','En route'), ('dedouanement','Dédouanement'),('scanner','En Scanner'),('on_board','On board'),('amarrage','Amarage'),('accostage','Accostage'),('transbordement','Transbordement'),('route_2','En Route'), ('livre','Livré'),('charge','Chargé'), ('attente_liv','Att. Liv.'),('handling','Handling'),('echange','Echange'),('landing','Landing'),('en_board','On board'),('take_off','Take off'),('landed','Landed'),('released','Released'),('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')

    state_national = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('attente_liv','Att. livr.'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_dtd_road = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('take_off','Take off'),('landed','Landed'),('released','Released'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_dta = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('dedouanement','Dédouanement'), ('handling','Handling'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_atd = fields.Selection([('pret','Pret'), ('encours','En cours'), ('dedouanement','Dédouanement'), ('handling','Handling'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_ata = fields.Selection([('pret','Pret'), ('en_board','En board'),('take_off','Take off'),('landed','Landed'),('released','Released')], string='Etat', default='pret')

    state_dtd_sea = fields.Selection([('pret','Pret'),('encours','En cours'), ('attente_chargement','Att. Char.'),('attente_doc','Att. Doc.'), ('route','En route'), ('dedouanement','Dédouanement'),('en_board','En board'),('amarrage','Amarrage'),('accostage','Accostage'),('released','Released'),('route_2','En Route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_dtp = fields.Selection([('pret','Pret'), ('encours','En cours'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('dedouanement','Dédouanement'), ('handling','Handling'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_ptd = fields.Selection([('pret','Pret'), ('encours','En cours'), ('dedouanement','Dédouanement'), ('attente_chargement','Att. Char.'), ('attente_doc','Att. doc.'), ('charge','Chargé'), ('route','En route'), ('livre','Livré'), ('annule','Annulé'), ('bloque','BLoqué')], string='Etat', default='pret')
    state_ptp = fields.Selection([('pret','Pret'),('en_board','En board'),('amarrage','Amarrage'),('accostage','Accostage'),('released','Released')], string='Etat', default='pret')

    #GENERAL
    date= fields.Datetime(string="Date", default=fields.Date.today())
    default_code = fields.Char("N° dossier")
    priorite = fields.Selection([('faible','Faible'),('moyen','Moyen'),('eleve','Elevé'), ('prioritaire','Prioritaire')], string='Priorité', default='faible')
    client_id = fields.Many2one("res.partner", string='Client', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 0),('is_company', '=', True)])
    ref_client = fields.Char("Référence Client")
    name = fields.Char('Nom du dossier', compute='compute_name',inverse='uncompute_name', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)
    currency_id = fields.Many2one(related="client_id.property_product_pricelist.currency_id", string="devise")
    ref_tmc = fields.Char("Ref TMC")
    is_groupage = fields.Boolean('Groupage ?')

    #PARAMETRAGE VOYAGES
    service = fields.Selection([('transport','Transport'), ('consignation','Consignation'), ('transvasement','Transvasement'),('magasinage','Magasinage'), ('location','Location')], string='Service', default='transport')
    type_voyage  = fields.Selection([('national','National'), ('international','International')], string='Type')
    voie = fields.Selection([('road','Road'),('sea','Sea'),('air','Air')], string='Voie')
    type_trajet = fields.Selection([('import','Import'), ('export','Export'), ('domestique','Domestique')], string='Catégorie')
    type_parcours = fields.Selection([('oneway','Single trip'), ('return','Return way'), ('round','Round trip')], string='Parcours')
    cch = fields.Boolean('CCH ?')
    type_prestation = fields.Selection([('standard','Standard'), ('premium','Premium')], string='Type préstation')
    transport = fields.Selection([('dtd','DTD'), ('dta','DTA'), ('ata','ATA'), ('atd','ATD')], string='Transport')
    transport_sea = fields.Selection([('dtd','DTD'), ('dtp','DTP'), ('ptp','PTP'), ('ptd','PTD')], string='Transport')
    type_transport = fields.Selection([('charter','Charter'), ('handcarry','Hand carry'), ('fret','Air fret')], string='Type transport')
    type_chemin = fields.Selection([('pre', 'Pré-acheminement'),('post', 'Post-acheminement'),('pre-post', 'Acheminement complet')], string='Type chemin')

    lieu_ramassage = fields.Many2one("res.partner", string='Lieu de ramassage', domain=[('type','=', 'delivery')])
    lieu_livraison = fields.Many2one("res.partner", string='Lieu de livraison', domain=[('type','=', 'delivery')])
    ville_ramassage = fields.Many2one("res.city", related='lieu_ramassage.ville', string='Ville ramassage', store=True)
    ville_livraison = fields.Many2one("res.city",related='lieu_livraison.ville', string='Ville livraison', store=True)
    zip_ramassage = fields.Char(related='lieu_ramassage.zip', string='Code postal', store=True)
    zip_livraison = fields.Char(related='lieu_livraison.zip', string='Code postal', store=True)

    # ramassage_ids = fields.Many2many('cps.voyage.lieu', 'voyage_ids', string='Ramassages')
    # livraison_ids = fields.Many2many('cps.voyage.lieu', 'voyage_livraison_ids', string='Ramassages')

    ramassage_ids = fields.One2many('cps.voyage.lieux', 'voyages_ids', string='Ramassages')
    livraison_ids = fields.One2many('cps.voyage.lieux', 'voyages_livraison_ids', string='Livraisons')

    #COLISAGE
    colisage_ids = fields.One2many('cps.colisage', 'voyage_id', string='Liste des colis')

    #PRIX
    cout_trajet = fields.Float(string="Cout du trajet", store=True)
    cout_total = fields.Monetary(compute='compute_cout', string="Cout total", store=True)
    prix = fields.Monetary(compute='compute_prix',string="Prix de vente",inverse='uncompute_price', store=True)
    marge = fields.Float('Marge (%)')

    #VEHICULES
    sous_traitance_1 = fields.Boolean('Sous-traitance ?')
    vehicule_st1_ids = fields.One2many('cps.voyage.soustraitant', 'voyage_id', 'Sous-traitants', domain=[('etape_voyage', '=', 1)])
    vehicule_parc_1_ids = fields.One2many('cps.voyage.parc', 'voyage_id', 'Parc Faster')
    vehicule_st2_ids = fields.One2many('cps.voyage.soustraitant', 'voyage_id', 'Sous-traitants', domain=[('etape_voyage', '=', 2)])
    vehicule_parc2_ids = fields.One2many('cps.voyage.parc2', 'voyage_id', 'Parc Faster')

    # ----CCH fields--------
    is_dedouanement_1 = fields.Boolean('Dédouanement ?')
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
    is_dedouanement_2 = fields.Boolean('Dédouanement ?')
    dedouanement_2 = fields.Many2one("res.partner", string='Transitaire', domain=[('is_transitaire', '=', True),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transitaire_2 = fields.Monetary(string="Cout")
    sous_traitance_2 = fields.Boolean('Sous-traitance ?')


    #INTER-ROUTIER
    bateau = fields.Many2one("res.partner", string='Bateau', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', True),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_bateau = fields.Monetary(string="Cout")
    date_sortie_bateau = fields.Datetime('Heure sortie')
    bill_loading = fields.Char('Bill of loading')
    is_dedouanement_zf =  fields.Boolean('Dédouanement Z.F. ?')
    dedouanement_zf = fields.Many2one("res.partner", string='Transitaire ZF', domain=[('is_transitaire', '=', True),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transitaire_zf = fields.Monetary(string="Cout")

    #INTER-ROUTIER TRANSBORDEMENT
    transbordement = fields.Many2one("res.partner", string='Transbordement', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', True),('supplier_rank', '=', 1),('is_company', '=', True)])
    cout_transbordement = fields.Monetary(string="Cout")

    #Documents de vente
    facture_achat_ids = fields.One2many('account.move', 'voyage_id', domain=[('move_type', '=', 'in_invoice')], string="Factures d'achat")
    total_facture_achats = fields.Float('Factures achats', compute="compute_facture_achat_amount")
    facture_vente_ids = fields.One2many('account.move', 'voyage_id', domain=[('move_type', '=', 'out_invoice')], string="Factures de vente")
    total_facture_vente = fields.Float('Factures ventes', compute="compute_facture_vente_amount")

    #Documents achat
    commande_achat_ids = fields.One2many('purchase.order', 'voyage_id', string="Commandes d'achat")
    total_commandes_achats = fields.Float('Commandes achats', compute="compute_commande_achat_amount")
    commande_vente_ids = fields.One2many('sale.order', 'voyage_id', string="Commandes de vente")
    total_commandes_vente = fields.Float('Commandes ventes', compute="compute_commande_vente_amount")

    #TRacking et resumé
    tracking_ids = fields.One2many('cps.voyage.tracking', 'voyage_id', string='Tracking du dossier')
    resume_ids = fields.One2many('cps.voyage.resume', 'voyage_id', string='Résumé du dossier')

    def uncompute_price(self):
        print('test')

    def uncompute_name(self):
        print('test')

    @api.onchange('transport', 'transport_sea')
    def onchange_transport(self):
        self.type_chemin=False
        if self.transport =='dta' or self.transport_sea =='dtp' :
            self.type_chemin='pre'
        if self.transport=='atd' or self.transport_sea =='ptd' :
            self.type_chemin='post'
        if self.transport=='dtd' or self.transport_sea =='dtd' :
            self.type_chemin='pre-post'

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

    @api.depends('state_national','state_dtd_sea','state_dtp','state_ptd','state_ptp','state_dtd_road','state_dta','state_atd','state_ata')
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
            if s.transport=="dtd":
                if s.state_dtd_road!="pret" and s.state_dtd_road!="bloque" and  s.state_dtd_road!="annule" :
                    for state in dict(s._fields['state_dtd_road'].selection).keys():
                        i+=1
                        if state==s.state_dtd_road:
                            progress=i / (len(dict(s._fields['state_dtd_road'].selection))-2)*100
            if s.transport=="dta":
                if s.state_dta!="pret" and s.state_dta!="bloque" and  s.state_dta!="annule" :
                    for state in dict(s._fields['state_dta'].selection).keys():
                        i+=1
                        if state==s.state_dta:
                            progress=i / (len(dict(s._fields['state_dta'].selection))-2)*100
            if s.transport=="atd":
                if s.state_atd!="pret" and s.state_atd!="bloque" and  s.state_atd!="annule" :
                    for state in dict(s._fields['state_atd'].selection).keys():
                        i+=1
                        if state==s.state_atd:
                            progress=i / (len(dict(s._fields['state_atd'].selection))-2)*100
            if s.transport=="ata":
                if s.state_ata!="pret" and s.state_ata!="bloque" and  s.state_ata!="annule" :
                    for state in dict(s._fields['state_ata'].selection).keys():
                        i+=1
                        if state==s.state_ata:
                            progress=i / (len(dict(s._fields['state_ata'].selection))-2)*100
            if s.transport_sea=="dtd":
                if s.state_dtd_sea!="pret" and s.state_dtd_sea!="bloque" and  s.state_dtd_sea!="annule" :
                    for state in dict(s._fields['state_dtd_sea'].selection).keys():
                        i+=1
                        if state==s.state_dtd_sea:
                            progress=i / (len(dict(s._fields['state_dtd_sea'].selection))-2)*100
            if s.transport_sea=="dtp":
                if s.state_dtp!="pret" and s.state_dtp!="bloque" and  s.state_dtp!="annule" :
                    for state in dict(s._fields['state_dtp'].selection).keys():
                        i+=1
                        if state==s.state_dtp:
                            progress=i / (len(dict(s._fields['state_dtp'].selection))-2)*100
            if s.transport_sea=="ptd":
                if s.state_ptd!="pret" and s.state_ptd!="bloque" and  s.state_ptd!="annule" :
                    for state in dict(s._fields['state_ptd'].selection).keys():
                        i+=1
                        if state==s.state_ptd:
                            progress=i / (len(dict(s._fields['state_ptd'].selection))-2)*100
            if s.transport_sea=="ptp":
                if s.state_ptp!="pret" and s.state_ptp!="bloque" and  s.state_ptp!="annule" :
                    for state in dict(s._fields['state_ptp'].selection).keys():
                        i+=1
                        if state==s.state_ptp:
                            progress=i / (len(dict(s._fields['state_ptp'].selection))-2)*100


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
            elif 'state_dtd_road' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_dtd_road'].selection).get(p.state_dtd_road)})
                p.state_general = p.state_dtd_road
            elif 'state_dta' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_dta'].selection).get(p.state_dta)})
                p.state_general = p.state_dta
            elif 'state_atd' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_atd'].selection).get(p.state_atd)})
                p.state_general = p.state_atd
            elif 'state_ata' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_ata'].selection).get(p.state_ata)})
                p.state_general = p.state_ata
            elif 'state_dtd_sea' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_dtd_sea'].selection).get(p.state_dtd_sea)})
                p.state_general = p.state_dtd_sea
            elif 'state_dtp' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_dtp'].selection).get(p.state_dtp)})
                p.state_general = p.state_dtp
            elif 'state_ptd' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_ptd'].selection).get(p.state_ptd)})
                p.state_general = p.state_ptd
            elif 'state_ptp' in values:
                p.env['cps.voyage.tracking'].create({'voyage_id': p.id, 'date_tracking': fields.Datetime.now(), 'description': dict(p._fields['state_ptp'].selection).get(p.state_ptp)})
                p.state_general = p.state_ptp

    def calculer_resume(self):
        for p in self:
            for resume_id in p.resume_ids:
                print('resume_id.is_manuel----------------------', resume_id.is_manuel)
                if resume_id.is_manuel == False:
                    resume_id.unlink()
            if p.cout_trajet > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Cout du voyage ", 'cout': p.cout_trajet, 'is_manuel' : False})
            for vehicule_st_1_id in p.vehicule_st1_ids:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.soustraitance_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Sous-traitance véhicule " + vehicule_st_1_id.vehicule_st_1.license_plate, 'type_prestataire': 'sous-traitant', 'client_id': vehicule_st_1_id.soustraitant_id.id, 'cout': vehicule_st_1_id.cout, 'is_manuel' : False})
            for vehicule_parc_1_id in p.vehicule_parc_1_ids:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Véhicule Faster " + vehicule_parc_1_id.vehicule_id.license_plate, 'type_prestataire': 'parc', 'client_id': '', 'cout': vehicule_parc_1_id.cout, 'is_manuel' : False})
            for vehicule_st2_id in p.vehicule_st2_ids:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.soustraitance_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Sous-traitance véhicule " + vehicule_st2_id.vehicule_st_1.license_plate, 'type_prestataire': 'sous-traitant', 'client_id': vehicule_st2_id.soustraitant_id.id, 'cout': vehicule_st2_id.cout, 'is_manuel' : False})
            for vehicule_parc2_id in p.vehicule_parc2_ids:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description': "Véhicule Faster " + vehicule_parc2_id.vehicule_id.license_plate, 'type_prestataire': 'parc', 'client_id': '', 'cout': vehicule_parc2_id.cout, 'is_manuel' : False})
            if p.cout_transitaire_1 > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit " , 'type_prestataire':'transit', 'client_id': p.dedouanement_1.id, 'cout': p.cout_transitaire_1, 'is_manuel' : False})
            if p.cout_handling > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.handling_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de handling " , 'type_prestataire':'aerienne', 'client_id': p.handling.id, 'cout': p.cout_handling, 'is_manuel' : False})
            if p.cout_echange > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.echange_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais d'échange " , 'type_prestataire':'aerienne', 'client_id': p.echange.id, 'cout': p.cout_echange, 'is_manuel' : False})
            if p.cout_fret > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de fret " , 'type_prestataire':'aerienne', 'client_id': p.fret.id, 'cout': p.cout_fret, 'is_manuel' : False})
            if p.cout_bagage > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais d'excedent de bagage' " , 'type_prestataire':'aerienne', 'client_id': p.fret.id, 'cout': p.cout_bagage, 'is_manuel' : False})
            if p.frais_divers > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais divers' " , 'type_prestataire':'autre', 'cout': p.frais_divers, 'is_manuel' : False})
            if p.cout_transitaire_2 > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit " , 'type_prestataire':'transit', 'client_id': p.dedouanement_2.id, 'cout': p.cout_transitaire_2, 'is_manuel' : False})
            if p.cout_bateau > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de bateau " , 'type_prestataire':'maritine', 'client_id': p.bateau.id, 'cout': p.cout_bateau, 'is_manuel' : False})
            if p.cout_transitaire_zf > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transit en Z.F. ", 'type_prestataire':'transit', 'client_id': p.dedouanement_zf.id, 'cout': p.cout_transitaire_zf, 'is_manuel' : False})
            if p.cout_transbordement > 0:
                product_id = self.env['product.product'].search([("id", "=", self.env['ir.config_parameter'].sudo().get_param('cps_freight.echange_product'))])
                p.env['cps.voyage.resume'].create({'voyage_id': p.id, 'product_id': product_id.id, 'description':"Frais de transbordement ", 'type_prestataire':'magasinnage', 'client_id': p.transbordement.id, 'cout': p.cout_transbordement, 'is_manuel' : False})

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

    def action_validate(self):
        self.action_generate_purchase_order()
        self.action_generate_sale_order()

    def action_generate_purchase_order(self):
        for p in self.resume_ids:
            if len(p.client_id) > 0:
                pOrder = self.env['purchase.order'].create({
                    'company_id': self.env.user.company_id.id,
                    'partner_id': p.client_id.id,
                    'voyage_id': self.id,
                    'date_order': fields.datetime.now(),
                    'date_planned': fields.datetime.now(),
                    'currency_id': p.currency_id.id,
                    'order_line': [(0, 0, {
                                    'product_id': p.product_id.id,
                                    'currency_id': p.currency_id.id,
                                    'voyage_id': self.id,
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
                                'name': product_id.name,
                                'voyage_id': self.id,
                                'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
                                'product_uom_qty': 1,
                                'qty_delivered': 1,
                                'price_unit': self.prix,
                                # 'product_uom' : self.product_id.uom_id.id,
                                })]
            })
            sOrder.action_confirm()

    # def action_generate_invoice(self):
    #     # "creating cps facture"
    #     account_revenue = self.env['account.account'].search([('user_type_id', '=', self.env.ref('account.data_account_type_revenue').id)], limit=1)
    #     if self.client_id is not False:
    #         account_journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
    #         invoice = self.env['account.move'].create({
    #             'partner_id': self.client_id.id,
    #             'partner_shipping_id': self.client_id.id,
    #             'journal_id': account_journal.id,
    #             'move_type': 'out_invoice',
    #             'invoice_date': fields.Datetime.now(),
    #             'invoice_payment_term_id': self.client_id.property_payment_term_id.id,
    #             'currency_id': self.client_id.property_product_pricelist[0].currency_id.id,
    #             'voyage_id': self.id,
    #             'name': '/',
    #             'invoice_line_ids': [],
    #             'state': 'draft',
    #
    #         })
    #         invoice_line = []
    #         invoice_line.append((0, 0, {
    #             'quantity': 1,
    #             'price_unit': self.prix,
    #             # 'name': self.trajet_id.name,
    #             'account_id': account_revenue.id,
    #             # 'tax_ids': [(6, 0, sol.tax_id.ids if tax_id is not False else [])],
    #             'sale_line_ids': [],
    #             # 'facturation_line_id': facture_line.id
    #         }),
    #                             )
    #         invoice.write({'invoice_line_ids': invoice_line})

    def compute_facture_achat_amount(self):
        total=0
        for f in self.facture_achat_ids:
            total+=f.amount_untaxed_signed
        self.total_facture_achats = -total

    def compute_commande_achat_amount(self):
        total=0
        for f in self.commande_achat_ids:
            total+=f.amount_untaxed * (1/f.currency_rate)
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
            total+=f.amount_untaxed * (1/f.currency_rate)
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
            'domain': [('id', '=', self.vehicule_st_1.vehicule_id.id)],
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
            'domain': [('id', '=', self.vehicule_st_2.vehicule_id.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
        return result

    @api.depends('resume_ids')
    def compute_cout(self):
        for p in self:
            p.cout_total=0
            for resume in self.resume_ids:
                p.cout_total+=resume.cout

    @api.depends('vehicule_st1_ids','vehicule_parc_1_ids','vehicule_st2_ids','vehicule_parc2_ids')
    def compute_prix(self):
        for p in self:
            p.prix=0
            for vehicule_st1_id in self.vehicule_st1_ids:
                p.prix+=vehicule_st1_id.prix
            for vehicule_st2_id in self.vehicule_st2_ids:
                p.prix+=vehicule_st2_id.prix
            for vehicule_parc_id in self.vehicule_parc_1_ids:
                p.prix+=vehicule_parc_id.prix
            for vehicule_parc2_ids in self.vehicule_parc2_ids:
                p.prix+=vehicule_parc2_ids.prix
            print('prix-------------------', p.prix)

    def set_price(self):
        for p in self:
            p.prix=p.cout_total+((p.cout_total*p.marge)/100)

    def name_get(self):
        print('name get----------------')
        res = []
        for rec in self:
            name = rec.name
            res.append((rec.id, name))
        return res

    def copy(self, default=None):
        default = dict(default or {})
        default.update ({'ref_client': '',
                         'ref_tmc':'',
                         'porteur':0,
                         'is_dedouanement_1':False,
                         'cout_transitaire_1' : 0
                         })
        new_dossier = super(CpsVoyage, self).copy(default)
        return new_dossier

    def get_name(self):
        print('get name----------------')

        for s in self:
            name = ""
            if s.default_code is not False:
                name = name + s.default_code
            return name

    @api.depends('default_code')
    def compute_name(self):
        for s in self:
            name = ""
            print('s.default_code-----------------------',s.default_code)
            # print('s.trajet_id-----------------------',s.trajet_id)
            print('compute name----------------')
            if s.default_code is not False:
                name = name + s.default_code
            # if len(s.trajet_id)>0:
            #     name += " / " + str(s.trajet_id.name)
            s.name = name

    @api.onchange('type_voyage')
    def on_change_type_voyage(self):
        self.transport=""