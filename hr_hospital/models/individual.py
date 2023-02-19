from odoo import models, fields

class IndividualMixin(models.AbstractModel):
     _name = 'hr.hospital.individual.mixin'
     _description = 'Individual Mixin'
     
     full_name = fields.Char()
     phone = fields.Char()
     email = fields.Char()
     foto = fields.Image()
     gender = fields.Char()
     