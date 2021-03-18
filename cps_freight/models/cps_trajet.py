"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class CpsTrajet(models.Model):

    _name = 'cps.trajet'
    _description = "Trajets"

    partner_id = fields.Many2one('res.partner', 'Client', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', False),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 0),('is_company', '=', True)])
    # voyage_ids = fields.One2many("cps.voyage", 'trajet_id', string="Liste des voyages")
    trajet_lines = fields.One2many("cps.trajet.lines", 'trajet_id', string="Détail du trajet")

