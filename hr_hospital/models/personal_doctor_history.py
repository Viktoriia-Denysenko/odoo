from odoo import models, fields


class PersonalDoctorHistory(models.Model):

    _name = "hr.hospital.personal.doctor.history"
    _description = "Personal Doctor History"

    name = fields.Char() 
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
    )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )
    visit_date = fields.Date()
