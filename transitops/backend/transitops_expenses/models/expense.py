from odoo import models, fields


class TransitopsExpense(models.Model):
    _name = 'transitops.expense'
    _description = 'Vehicle Expense'

    vehicle_id = fields.Many2one(
        'transitops.vehicle',
        string='Vehicle',
        required=True,
    )
    expense_type = fields.Char(
        string='Expense Type',
    )
    amount = fields.Float(
        string='Amount',
    )
    date = fields.Date(
        string='Date',
    )
