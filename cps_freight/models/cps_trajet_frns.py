"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class CpsTrajetFrns(models.Model):

    _name = 'cps.trajet.frns'
    _description = "Trajets fournisseur"

    partner_id = fields.Many2one('res.partner', 'Fournisseur', domain=[('is_soutraitant', '=', True),('supplier_rank', '>', 0),('is_company', '=', True)])
    tarif_interne = fields.Boolean('Tarif interne')
    trajet_lines = fields.One2many("cps.trajet.lines.frns", 'trajet_id', string="Détail du trajet")

