from odoo import models, fields


class Patient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Patient"

    name = fields.Char()
    gender = fields.Char()
    birthday = fields.Date()
    age = fields.Char()
    passport = fields.Char()
    contact_person = fields.Char()
    personal_doctor = fields.Char()

    doctor_ids = fields.Many2many(
        comodel_name="hr.hospital.doctor", )

    disease_ids = fields.Many2many(
        comodel_name="hr.hospital.disease", )

    visit_ids = fields.Many2many(
        comodel_name="hr.hospital.visit", )
