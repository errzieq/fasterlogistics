from odoo import models, fields, api
from ast import literal_eval

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    transport_product = fields.Many2one('product.product', string="Transport national", domain= '[("purchase_ok", "=", True)]')
    transport_inter_product = fields.Many2one('product.product', string="Transport international", domain= '[("purchase_ok", "=", True)]')
    soustraitance_product = fields.Many2one('product.product', string="Transport sous-traitant", domain= '[("purchase_ok", "=", True)]')
    handling_product = fields.Many2one('product.product', string="Handling", domain= '[("purchase_ok", "=", True)]')
    dedouanement_product = fields.Many2one('product.product', string="Dédouanement", domain= '[("purchase_ok", "=", True)]')
    porteur_product = fields.Many2one('product.product', string="Porteur", domain= '[("purchase_ok", "=", True)]')
    fret_product = fields.Many2one('product.product', string="Fret", domain= '[("purchase_ok", "=", True)]')
    echange_product = fields.Many2one('product.product', string="Echange", domain= '[("purchase_ok", "=", True)]')

    vente_product = fields.Many2one('product.product', string="Vente", domain= '[("sale_ok", "=", True)]')

    def get_transport_product(self):
        transport_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_product')
        transport = self.env['product.product'].search([("id", "=", transport_product)])
        return transport

    def get_transport_inter_product(self):
        transport_inter_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.transport_inter_product')
        transport = self.env['product.product'].search([("id", "=", transport_inter_product)])
        return transport

    def get_soustraitance_product(self):
        soustraitance_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.soustraitance_product')
        soustraitance = self.env['product.product'].search([("id", "=", soustraitance_product)])
        return soustraitance

    def get_handling_product(self):
        handling_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.handling_product')
        handling = self.env['product.product'].search([("id", "=", handling_product)])
        return handling

    def get_dedouanement_product(self):
        dedouanement_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.dedouanement_product')
        dedouanement = self.env['product.product'].search([("id", "=", dedouanement_product)])
        return dedouanement

    def get_porteur_product(self):
        porteur_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.porteur_product')
        porteur = self.env['product.product'].search([("id", "=", porteur_product)])
        return porteur

    def get_fret_product(self):
        fret_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.fret_product')
        fret = self.env['product.product'].search([("id", "=", fret_product)])
        return fret

    def get_echange_product(self):
        echange_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.echange_product')
        echange = self.env['product.product'].search([("id", "=", echange_product)])
        return echange

    def get_vente_product(self):
        vente_product = self.env['ir.config_parameter'].sudo().get_param('cps_freight.vente_product')
        vente = self.env['product.product'].search([("id", "=", vente_product)])
        return vente

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('cps_freight.transport_product', self.transport_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.transport_inter_product', self.transport_inter_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.soustraitance_product', self.soustraitance_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.handling_product', self.handling_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.dedouanement_product', self.dedouanement_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.porteur_product', self.porteur_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.fret_product', self.fret_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.echange_product', self.echange_product.id)
        self.env['ir.config_parameter'].set_param('cps_freight.vente_product', self.vente_product.id)
        return res

    def get_values(self):
        """Return a list of the possible values."""
        res = super(ResConfigSettings, self).get_values()
        res.update(transport_product = self.get_transport_product().id)
        res.update(transport_inter_product = self.get_transport_inter_product().id)
        res.update(soustraitance_product = self.get_soustraitance_product().id)
        res.update(handling_product = self.get_handling_product().id)
        res.update(dedouanement_product = self.get_dedouanement_product().id)
        res.update(porteur_product = self.get_porteur_product().id)
        res.update(fret_product = self.get_fret_product().id)
        res.update(echange_product = self.get_echange_product().id)
        res.update(vente_product = self.get_vente_product().id)
        return res