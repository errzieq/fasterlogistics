"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class CpsTrajetLines(models.Model):

    _name = 'cps.trajet.lines'
    _description = "Lignes des trajets"

    trajet_id = fields.Many2one('cps.trajet', 'Trajet')
    partner_id = fields.Many2one("res.partner", related='trajet_id.partner_id', store=True)
    lieu_ramassage = fields.Many2one("res.city", string='Ville de ramassage', required=True)
    lieu_livraison = fields.Many2one("res.city", string='Ville de livraison', required=True)
    type_vehicule = fields.Selection(string="Type véhicule", selection=[('type1', 'Type 1'),
                                                                       ('type2', 'Type 2'),
                                                                       ('type3', 'Type 3'),
                                                                       ('type4', 'Type 4'),
                                                                       ('type5', 'Type 5')])
    type_voyage =  fields.Selection(string="Type voyage", selection=[('oneway', 'One way'),
                                                                       ('round', 'Round trip')])
    cout = fields.Float(string="Cout")
    currency_id = fields.Many2one('res.currency', string='Devise')

    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            res.append((rec.id, name))
        return res

    def get_name(self):
        for p in self:
            name = ""
            if p.lieu_ramassage is not False and p.lieu_livraison is not False :
                name = name + str(p.lieu_ramassage.name) + " - " + str(p.lieu_livraison.name)
            return name

    @api.depends('lieu_ramassage','lieu_livraison')
    def compute_name(self):
        for p in self:
            name = ""
            if p.lieu_ramassage is not False and p.lieu_livraison is not False :
                name = name + str(p.lieu_ramassage.name)  + " -> " + str(p.lieu_livraison.name)
            p.name =  name