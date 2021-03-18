from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    voyage_id = fields.Many2one('cps.voyage', 'Liste des voyages')
