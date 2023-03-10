from odoo import models, fields


class Patient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Patient"

    name = fields.Char()

    active = fields.Boolean(
        default=True,
    )

    doctor_ids = fields.Many2many(
        comodel_name="hr.hospital.doctor", )

    disease_ids = fields.Many2many(
        comodel_name="hr.hospital.disease", )

    visit_ids = fields.Many2many(
        comodel_name="hr.hospital.visit", )
