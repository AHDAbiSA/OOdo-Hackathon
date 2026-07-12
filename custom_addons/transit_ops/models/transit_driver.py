# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TransitDriver(models.Model):
    _name = 'transit.driver'
    _description = 'Transit Driver'
    _order = 'driver_name'
    _rec_name = 'driver_name'

    driver_name = fields.Char(
        string='Driver Name',
        required=True,
        help='Enter the full name of the driver.'
    )

    license_number = fields.Char(
        string='License Number',
        required=True,
        index=True,
        help='Unique driving license number.'
    )

    license_category = fields.Selection([
        ('lmv', 'LMV'),
        ('hmv', 'HMV'),
        ('transport', 'Transport')
    ],
        string='License Category',
        required=True
    )

    license_expiry = fields.Date(
        string='License Expiry',
        required=True
    )

    contact_number = fields.Char(
        string='Contact Number',
        help='Enter a valid 10-digit contact number.'
    )

    safety_score = fields.Float(
        string='Safety Score',
        default=100.0,
        help='Driver safety score between 0 and 100.'
    )

    status = fields.Selection([
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('on_leave', 'On Leave'),
        ('suspended', 'Suspended')
    ],
        string='Status',
        default='available',
        required=True
    )

    _sql_constraints = [
        (
            'license_number_uniq',
            'unique(license_number)',
            'The License Number must be unique.'
        ),
    ]

    @api.constrains('driver_name')
    def _check_driver_name(self):
        for record in self:
            if not record.driver_name or not record.driver_name.strip():
                raise ValidationError(
                    "Driver Name cannot be empty."
                )

    @api.constrains('license_number')
    def _check_license_number(self):
        for record in self:
            if not record.license_number or not record.license_number.strip():
                raise ValidationError(
                    "License Number cannot be empty."
                )

            duplicate = self.search([
                ('license_number', '=', record.license_number),
                ('id', '!=', record.id)
            ], limit=1)

            if duplicate:
                raise ValidationError(
                    "A driver with this License Number already exists."
                )

    @api.constrains('license_expiry', 'status')
    def _check_license_expiry(self):
        today = fields.Date.context_today(self)

        for record in self:
            if (
                record.license_expiry
                and record.license_expiry < today
                and record.status in ('available', 'on_trip')
            ):
                raise ValidationError(
                    "License Expiry cannot be in the past for an active driver."
                )

    @api.constrains('safety_score')
    def _check_safety_score(self):
        for record in self:
            if record.safety_score < 0 or record.safety_score > 100:
                raise ValidationError(
                    "Safety Score must be between 0 and 100."
                )

    @api.constrains('contact_number')
    def _check_contact_number(self):
        for record in self:
            if record.contact_number:
                contact = record.contact_number.strip()

                if not contact.isdigit():
                    raise ValidationError(
                        "Contact Number must contain only digits."
                    )

                if len(contact) != 10:
                    raise ValidationError(
                        "Contact Number must contain exactly 10 digits."
                    )