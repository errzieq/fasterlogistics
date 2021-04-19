"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResPartner(models.Model):
    """Inherit Partner Model."""

    _inherit = 'fleet.vehicle'

    soustraitant_id = fields.Many2one("res.partner", string='Sous-traitant', domain=[('is_transitaire', '=', False),('is_soutraitant', '=', True),('is_compagnie_aerienne', '=', False),('is_compagnie_maritine', '=', False),('is_compagnie_magasinnage', '=', False),('supplier_rank', '=', 1),('is_company', '=', True)])
    type_vehicule = fields.Selection(string="Type véhicule", selection=[('type1', 'Type 1'),
                                                                       ('type2', 'Type 2'),
                                                                       ('type3', 'Type 3'),
                                                                       ('type3a', 'Type 3A'),
                                                                       ('type4', 'Type 4'),
                                                                       ('type5', 'Type 5'),
                                                                       ('type6', 'Type 6'),
                                                                       ('type7', 'Type 7'),
                                                                       ('type8', 'Type 8'),
                                                                       ('type9', 'Type 9'),
                                                                       ('type10', 'Type 10')
                                                                        ])

    @api.depends('license_plate')
    def _compute_vehicle_name(self):
        for record in self:
            record.name = record.license_plate or _('No Plate')
