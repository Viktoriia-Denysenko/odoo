from odoo import models, fields


class Doctor(models.Model):

    _name = "hr.hospital.doctor"
    _description = "Doctor"
   

    name = fields.Char()
    specialization = fields.Char()
