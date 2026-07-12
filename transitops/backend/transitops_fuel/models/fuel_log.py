from odoo import models, fields


class TransitopsFuelLog(models.Model):
    _name = 'transitops.fuel.log'
    _description = 'Vehicle Fuel Log'

    vehicle_id = fields.Many2one(
        'transit.vehicle',
        string='Vehicle',
        required=True,
    )
    liters = fields.Float(
        string='Liters',
    )
    cost = fields.Float(
        string='Cost',
    )
    date = fields.Date(
        string='Date',
    )
    distance = fields.Float(
        string='Distance',
    )
