"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResPartner(models.Model):
    """Inherit Partner Model."""

    _inherit = 'res.partner'

    liste_voyages = fields.One2many('cps.voyage', 'client_id', 'Liste des voyages')
    liste_vehicules = fields.One2many('fleet.vehicle', 'soustraitant_id', 'Liste des véhicules')

    is_transitaire = fields.Boolean(string="Transitaire")
    is_soutraitant = fields.Boolean(string="Transporteur")
    is_soutraitant_inter = fields.Boolean(string="Transporteur international")
    is_compagnie_aerienne = fields.Boolean(string="Compagnie aerienne")
    is_compagnie_maritine = fields.Boolean(string="Compagnie maritime")
    is_compagnie_magasinnage = fields.Boolean(string="Sté de Magasinage")
    is_autorite_portuaire = fields.Boolean(string="Autorité portuaire")
    is_fret_forwarder = fields.Boolean(string="Fret forwarder")
    is_service = fields.Boolean(string="Service")

    ville = fields.Many2one("res.city", string='Ville', required=True)

    numero_ice = fields.Char('ICE')
    numero_cnss = fields.Char('N° CNSS')
    numero_rc = fields.Char('N° RC')
    numero_if = fields.Char('N° IF')
    numero_tp = fields.Char('N° TP')
    classement = fields.Char('Classement')

    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            res.append((rec.id, name))
        return res

    def get_name(self):
        for s in self:
            name = s.name + " " + s.city + " " + s.zip
            return name
