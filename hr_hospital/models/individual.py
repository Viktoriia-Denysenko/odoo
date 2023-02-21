from odoo import models, fields

class IndividualMixin(models.AbstractModel):
     _name = 'hr.hospital.individual.mixin'
     _description = 'Individual Mixin'
     
     name = fields.Char()
     phone = fields.Char()
     email = fields.Char()
     foto = fields.Image("Image", max_width=1920, max_height=192)
     gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')])
     
     
class ContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact person'
    _inherit = 'hr.hospital.individual.mixin'
     