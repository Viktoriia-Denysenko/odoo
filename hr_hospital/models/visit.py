from odoo import models, fields


class Visit(models.Model):

    _name = "hr.hospital.visit"
    _description = "Visit"

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
    )

    visit_datetime = fields.Datetime()

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
    )
    
    research_id = fields.Many2many(
        comodel_name='hr.hospital.research',
    )

    recommendation = fields.Char()
