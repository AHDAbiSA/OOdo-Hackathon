from odoo import models, fields


class TransitopsMaintenance(models.Model):
    _name = 'transitops.maintenance'
    _description = 'Vehicle Maintenance Record'

    vehicle_id = fields.Many2one(
        'transitops.vehicle',
        string='Vehicle',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )
    cost = fields.Float(
        string='Cost',
    )
    status = fields.Selection(
        [
            ('in_shop', 'In Shop'),
            ('available', 'Available'),
        ],
        string='Status',
        default='in_shop',
    )
