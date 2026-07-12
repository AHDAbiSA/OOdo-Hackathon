from odoo import models, fields


class TransitopsMaintenance(models.Model):
    _name = 'transitops.maintenance'
    _description = 'Vehicle Maintenance Record'
    _rec_name = 'description'

    vehicle_id = fields.Many2one(
        'transit.vehicle',
        string='Vehicle',
        required=True,
    )

    description = fields.Char(
        string='Description',
        required=True,
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