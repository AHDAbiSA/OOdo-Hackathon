from odoo import models, fields


class TransitOpsVehicle(models.Model):
    _inherit = 'transit.vehicle'
    _description = 'TransitOps Vehicle Extension'

    license_plate = fields.Char(string='License Plate')
    driver = fields.Char(string='Driver')
