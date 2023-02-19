from odoo import models, fields


class DoctorSchedule(models.Model):

    _name = "hr.hospital.doctor.schedule"
    _description = "Doctor's schedule"
    
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    date = fields.Date()
