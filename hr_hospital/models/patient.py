from datetime import date
from odoo import models, fields, api, _


class Patient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Patient"
    _inherit = 'hr.hospital.individual.mixin'

    birthday = fields.Date()
    age = fields.Integer(compute='compute_age')
    passport = fields.Char()
    
    contact_person_id = fields.Many2one(
        comodel_name="hr.hospital.contact.person", )
    
    personal_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')

    doctor_id = fields.Many2one(
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
                
    @api.model
    def create(self, vals):
        record = super(Patient, self).create(vals)
        if 'personal_doctor_id' in vals:
            values = {
                'appointment_datetime': fields.Datetime.now(),
                'patient_id': record.id,
                'doctor_id': vals['personal_doctor_id'],
            }
            self.env['hr.hospital.personal.doctor.history'].create(values)
        return record

    def write(self, vals):
        record = super(Patient, self).write(vals)
        if 'personal_doctor_id' in vals:
            for record in self:
                if record.personal_doctor_id != vals['personal_doctor_id']:
                    values = {
                        'appointment_datetime': fields.Datetime.now(),
                        'patient_id': record.id,
                        'doctor_id': vals['personal_doctor_id'],
                    }
                self.env['hr.hospital.personal.doctor.history'].create(values)
        return record
    