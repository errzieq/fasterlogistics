"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class ResCity(models.Model):

    _name = 'res.city'
    _description = "Villes"

    voyage_lieu_ramassage = fields.One2many('cps.trajet.lines', 'lieu_ramassage',  'Lieux de ramassage')
    voyage_lieu_livraison = fields.One2many('cps.trajet.lines', 'lieu_livraison',  'Lieux de livraison')
    name = fields.Char('Nom')

    def get_name(self):
        for p in self:
             return p.name
