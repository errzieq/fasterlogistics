"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class CpsVoyageSoustraitant(models.Model):

    _name = 'cps.voyage.soustraitant'
    _description = "Liste des vehicules sous-traitant"

    voyage_id = fields.Many2one('cps.voyage', string='Voyages')
    soustraitant_id = fields.Many2one("res.partner", string='Sous-traitant')
    vehicule_st_1 = fields.Many2one('fleet.vehicle', domain="[('soustraitant_id', '=', soustraitant_id)]", string="Véhicule")
    etape_voyage = fields.Integer(string="Etape")
    modele_vehicule = fields.Char('Modéle', related='vehicule_st_1.model_id.name')
    type_vehicule = fields.Selection(string="Type véhicule",selection=[('type1', 'Type 1'),
                                                                       ('type2', 'Type 2'),
                                                                       ('type3', 'Type 3'),
                                                                       ('type3a', 'Type 3A'),
                                                                       ('type4', 'Type 4'),
                                                                       ('type5', 'Type 5'),
                                                                       ('type6', 'Type 6'),
                                                                       ('type7', 'Type 7'),
                                                                       ('type8', 'Type 8'),
                                                                       ('type9', 'Type 9'),
                                                                       ('type10', 'Type 10')
                                                                        ])
    client_id = fields.Many2one("res.partner", string='Client', related='voyage_id.client_id', store=True)
    lieu_ramassage = fields.Many2one("res.partner", string='Lieu de ramassage', domain=[('type','=', 'delivery')], related='voyage_id.lieu_ramassage', store=True)
    lieu_livraison = fields.Many2one("res.partner", string='Lieu de livraison', domain=[('type','=', 'delivery')], related='voyage_id.lieu_livraison', store=True)
    ville_ramassage = fields.Many2one("res.city", related='lieu_ramassage.ville', string='Ville ramassage', store=True)
    ville_livraison = fields.Many2one("res.city",related='lieu_livraison.ville', string='Ville livraison', store=True)
    type_voyage  = fields.Selection([('national','National'), ('international','International')], string='Type', related='voyage_id.type_voyage', store=True)
    type_parcours = fields.Selection([('oneway','Single trip'), ('return','Return way'), ('round','Round trip')], string='Parcours', related='voyage_id.type_parcours', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)
    currency_id = fields.Many2one(related="soustraitant_id.property_purchase_currency_id", string="devise")

    cout = fields.Monetary(string="Cout véhicule", compute='compute_price_frns', inverse='uncompute_price_frns', store=True)
    prix = fields.Monetary(string="Prix véhicule", compute='compute_price', inverse='uncompute_price', store=True)

    def uncompute_price_frns(self):
        print('test')

    def uncompute_price(self):
        print('test')

    @api.onchange('vehicule_st_1')
    def onchange_vehicule_st_1(self):
        self.type_vehicule=self.vehicule_st_1.type_vehicule

    @api.depends('ville_ramassage','ville_livraison','type_vehicule','type_parcours','type_parcours','soustraitant_id')
    def compute_price_frns(self):
        for p in self:
            if self.soustraitant_id is not False:
                trajet_price = p.env['cps.trajet.lines.frns'].search([('lieu_ramassage', '=', p.ville_ramassage.id),('lieu_livraison', '=', p.ville_livraison.id),('type_vehicule', '=', p.type_vehicule),('type_voyage', '=', p.type_parcours),('partner_id', '=', p.vehicule_st_1.soustraitant_id.id)]).cout
            else:
                trajet_price = p.env['cps.trajet.lines.frns'].search([('lieu_ramassage', '=', p.ville_ramassage.id),('lieu_livraison', '=', p.ville_livraison.id),('type_vehicule', '=', p.type_vehicule),('type_voyage', '=', p.type_parcours),('partner_id', '=', False)]).cout
            p.cout = trajet_price
            p.voyage_id.compute_cout

    @api.depends('ville_ramassage','ville_livraison','type_vehicule','type_parcours','client_id')
    def compute_price(self):
        for p in self:
            print('calucl prix de vente------------------------------------')
            p.prix = p.env['cps.trajet.lines'].search([('lieu_ramassage', '=', p.ville_ramassage.id), ('lieu_livraison', '=', p.ville_livraison.id), ('type_vehicule', '=', p.type_vehicule), ('type_voyage', '=', p.type_parcours), ('partner_id', '=', p.client_id.id)]).cout
            p.voyage_id.compute_prix


