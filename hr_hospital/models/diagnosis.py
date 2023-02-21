from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Diagnosis(models.Model):
    _name = "hr.hospital.diagnosis"
    _description = "Diagnosis"
    
    doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor", )
    
    patient_id = fields.Many2one(
        comodel_name="hr.hospital.patient", ) 
    
    disease_id = fields.Many2one(
        comodel_name="hr.hospital.disease", )   
    
    treatment = fields.Char()
    
    visit_id = fields.Many2one(
        comodel_name="hr.hospital.visit", ) 
    
    research_id = fields.Many2one(
        comodel_name="hr.hospital.research", ) 
      
    diagnosis_date = fields.Datetime(default=fields.Date.today,
                                     required=True) 
    
    comment = fields.Text()
    
    @api.constrains('doctor_id')
    def _check_intern(self):
         if self.doctor_id.intern and not self.comment:
            raise ValidationError("Doctor's comment is needed!")
    
    