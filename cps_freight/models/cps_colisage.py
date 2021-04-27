"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class CpsColisage(models.Model):

    _name = 'cps.colisage'
    _description = "Liste des colis"

    voyage_id = fields.Many2one("cps.voyage", string='Voyage')
    palette_id = fields.Many2one("cps.palette", string='Palette')
    type_colis = fields.Selection([('colis','Colis'), ('palette','Palette'), ('machine','Machine')], string='Type', default='colis')
    qte_colis = fields.Integer("Quantité")
    poids_colis = fields.Integer("Poids")
    longueur = fields.Integer("Longueur")
    largeur = fields.Integer("Largeur")
    hauteur = fields.Integer("Hauteur")

    @api.onchange('palette_id')
    def onchange_palette(self):
        self.longueur= self.palette_id.longueur
        self.largeur= self.palette_id.largeur