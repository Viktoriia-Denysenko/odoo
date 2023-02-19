from odoo import models, fields


class Research(models.Model):

    _name = "hr.hospital.research"
    _description = "Research"

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
    )
    
    name = fields.Char()
    
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    sample = fields.Char()

    conclusion = fields.Char()
