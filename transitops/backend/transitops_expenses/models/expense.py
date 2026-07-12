from odoo import models, fields


class TransitopsExpense(models.Model):
    _name = "transitops.expense"
    _description = "Vehicle Expense"
    _rec_name = "expense_type"

    vehicle_id = fields.Many2one(
        "transit.vehicle",
        string="Vehicle",
        required=True,
    )

    expense_type = fields.Char(
        string="Expense Type",
        required=True,
    )

    amount = fields.Float(
        string="Amount",
    )

    date = fields.Date(
        string="Date",
    )