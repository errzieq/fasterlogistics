"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResPartner(models.Model):
    """Inherit Partner Model."""

    _inherit = 'res.partner'

    liste_voyages = fields.One2many('cps.voyage', 'client_id', 'Liste des voyages')
    liste_vehicules = fields.One2many('fleet.vehicle', 'soustraitant_id', 'Liste des véhicules')

    is_transitaire = fields.Boolean(string="Transitaire")
    is_soutraitant = fields.Boolean(string="Sous-traitant")
    is_compagnie_aerienne = fields.Boolean(string="Compagnie aerienne")
    is_compagnie_maritine = fields.Boolean(string="Compagnie maritine")
    is_compagnie_magasinnage = fields.Boolean(string="Compagnie de magasinnage")

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
