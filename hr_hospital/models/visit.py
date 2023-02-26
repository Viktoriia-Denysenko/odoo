from odoo import models, fields, _
from odoo.exceptions import UserError


class Visit(models.Model):

    _name = "hr.hospital.visit"
    _description = "Visit"

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
    )

    visit_datetime = fields.Datetime(string='Date and time')

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
    )
    
    diagnosis_id = fields.Many2one(
        comodel_name='hr.hospital.diagnosis',
    )
    
    research_id = fields.Many2many(
        comodel_name='hr.hospital.research',
    )

    recommendation = fields.Char()

    def action_archive(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError(
                    _('You can not archive this visit, the diagnosis is filled in'))
        return super(Visit, self).action_archive()

    def unlink(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError(
                    _('You can not delete this visit, the diagnosis is filled in'))
        return super(Visit, self).unlink()