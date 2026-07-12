from odoo import models, fields

class TransitOpsVehicle(models.Model):
    _name = 'transitops.vehicle'
    _description = 'TransitOps Vehicle'

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate')
    driver = fields.Char(string='Driver')
