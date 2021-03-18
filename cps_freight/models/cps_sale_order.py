from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    voyage_id = fields.Many2one('cps.voyage', 'Liste des voyages')