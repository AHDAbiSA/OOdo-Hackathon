# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TransitTrip(models.Model):
    _name = "transit.trip"
    _description = "Transit Trip"
    _rec_name = "trip_reference"
    _order = "id desc"

    trip_reference = fields.Char(
        string="Trip Reference",
        required=True,
        readonly=True,
        copy=False,
        default="New"
    )

    source_location = fields.Char(
        string="Source",
        required=True
    )

    destination_location = fields.Char(
        string="Destination",
        required=True
    )

    vehicle_id = fields.Many2one(
        "transit.vehicle",
        string="Vehicle",
        required=True
    )

    driver_id = fields.Many2one(
        "transit.driver",
        string="Driver",
        required=True
    )

    cargo_weight = fields.Float(
        string="Cargo Weight"
    )

    planned_distance = fields.Float(
        string="Planned Distance (km)"
    )

    dispatch_date = fields.Datetime(
        string="Dispatch Date"
    )

    completion_date = fields.Datetime(
        string="Completion Date"
    )

    trip_status = fields.Selection([
        ("draft", "Draft"),
        ("dispatched", "Dispatched"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled")
    ],
        default="draft",
        string="Status"
    )

    @api.model
    def create(self, vals):
        if vals.get("trip_reference", "New") == "New":
            vals["trip_reference"] = self.env["ir.sequence"].next_by_code(
                "transit.trip"
            ) or "New"
        return super().create(vals)

    @api.constrains("cargo_weight", "vehicle_id")
    def _check_capacity(self):
        for record in self:
            if (
                record.vehicle_id
                and record.cargo_weight >
                record.vehicle_id.max_load_capacity
            ):
                raise ValidationError(
                    "Cargo weight exceeds vehicle capacity."
                )

    def action_dispatch(self):
        for record in self:
            if record.vehicle_id.status != "available":
                raise ValidationError(
                    "Vehicle is not available."
                )

            if record.driver_id.status != "available":
                raise ValidationError(
                    "Driver is not available."
                )

            record.vehicle_id.status = "on_trip"
            record.driver_id.status = "on_trip"
            record.dispatch_date = fields.Datetime.now()
            record.trip_status = "dispatched"

    def action_complete(self):
        for record in self:
            record.vehicle_id.status = "available"
            record.driver_id.status = "available"
            record.trip_status = "completed"
            record.completion_date = fields.Datetime.now()

    def action_cancel(self):
        for record in self:
            record.vehicle_id.status = "available"
            record.driver_id.status = "available"
            record.trip_status = "cancelled"