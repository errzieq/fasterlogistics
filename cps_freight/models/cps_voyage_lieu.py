"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class CpsVoyageLieux(models.Model):

    _name = 'cps.voyage.lieux'
    _description = "Liste des lieux"

    # voyage_ids = fields.Many2many('cps.voyage', 'ramassage_ids', string='Liste des ramassages')
    # voyage_livraison_ids = fields.Many2many('cps.voyage', 'livraison_ids', string='Liste des livraisons')
    voyages_ids = fields.Many2one('cps.voyage', 'ramassages_ids')
    voyages_livraison_ids = fields.Many2one('cps.voyage', 'livraisons_ids')
    tracking_ids = fields.Many2one('cps.voyage.tracking', 'Tracking')
    lieu = fields.Many2one("res.partner", string='Lieu', domain=[('type','=', 'delivery')], required=True)
    ville = fields.Many2one("res.city", related='lieu.ville', string='Ville', store=True)
    zip = fields.Char(related='lieu.zip', string='Code postal', store=True)
