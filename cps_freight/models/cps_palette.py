"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class CpsPalette(models.Model):

    _name = 'cps.palette'
    _description = "Liste des palettes"

    colis_id = fields.Many2one("cps.colisage", string='Ligne colis')
    name=fields.Char('Nom de la palette')
    longueur = fields.Integer("Longueur")
    largeur = fields.Integer("Largeur")


