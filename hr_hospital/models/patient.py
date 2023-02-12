import logging  

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__) 

class Patient(models.Model): 
    _name = "hr.hos.patient"
    _description = "Patient"
    
    name = fields.Char()
    
    active = fields.Boolean(
        default=True,
    )
