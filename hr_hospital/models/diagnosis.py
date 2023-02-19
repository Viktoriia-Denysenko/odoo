from odoo import models, fields

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
    