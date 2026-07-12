# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TransitVehicle(models.Model):
    _name = 'transit.vehicle'
    _description = 'Transit Vehicle'
    _order = 'vehicle_name'
    _rec_name = 'vehicle_name'

    registration_number = fields.Char(
        string='Registration Number', 
        required=True, 
        index=True
    )
    vehicle_name = fields.Char(
        string='Vehicle Name', 
        required=True
    )
    vehicle_type = fields.Selection([
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('bus', 'Bus'),
        ('trailer', 'Trailer')
    ], string='Vehicle Type')
    
    max_load_capacity = fields.Float(
        string='Max Load Capacity (kg)'
    )
    odometer_reading = fields.Float(
        string='Odometer Reading (km)'
    )
    acquisition_cost = fields.Float(
        string='Acquisition Cost'
    )
    status = fields.Selection([
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('in_shop', 'In Shop'),
        ('retired', 'Retired')
    ], string='Status', default='available', required=True)

    _sql_constraints = [
        ('registration_number_uniq', 'unique(registration_number)', 'The registration number must be unique!'),
    ]

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for record in self:
            if not record.registration_number or not record.registration_number.strip():
                raise ValidationError("Registration Number cannot be empty.")
            
            # Check for duplicate registration numbers
            duplicate = self.search([
                ('registration_number', '=', record.registration_number),
                ('id', '!=', record.id)
            ], limit=1)
            if duplicate:
                raise ValidationError("A vehicle with registration number '%s' already exists." % record.registration_number)
