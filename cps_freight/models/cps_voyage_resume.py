"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class CpsVoyageResume(models.Model):

    _name = 'cps.voyage.resume'
    _description = "Résumé du voyage"

    voyage_id = fields.Many2one('cps.voyage', 'Voyage')

    description = fields.Char('Déscription')
    product_id = fields.Many2one("product.product", string='Article')
    type_prestataire = fields.Selection([('parc','Parc interne'), ('sous-traitant','Sous-traitant'), ('transit','Transitaire'), ('aerienne','Compagnie aerienne'), ('particulier','Particulier'), ('maritine','Compagnie maritine'), ('magasinnage','Compagnie magasinage'), ('autre','autre')], string='Type préstataire')
    client_id = fields.Many2one("res.partner", string='Préstataire')
    cout = fields.Monetary(string="Cout")
    currency_id = fields.Many2one('res.currency', string='Devise', related='client_id.property_purchase_currency_id', store=True)
    is_manuel = fields.Boolean('Operation manuelle')