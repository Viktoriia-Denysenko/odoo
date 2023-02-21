from datetime import date
from odoo import models, fields


class Patient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Patient"

    name = fields.Char()
    gender = fields.Char()
    birthday = fields.Date()
    age = fields.Integer(compute='compute_age')
    passport = fields.Char()
    
    contact_person_id = fields.Many2one(
        comodel_name="hr.hospital.contact.person", )
    
    personal_doctor = fields.Char()

    doctor_ids = fields.Many2many(
        comodel_name="hr.hospital.doctor", )

    disease_ids = fields.Many2many(
        comodel_name="hr.hospital.disease", )

    visit_ids = fields.Many2many(
        comodel_name="hr.hospital.visit", )

    def compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = (date.today() - rec.birthday).days // 365
            else:
                rec.age = 0