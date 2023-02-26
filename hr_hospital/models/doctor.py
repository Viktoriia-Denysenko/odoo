from odoo import models, fields


class Doctor(models.Model):
    _name = "hr.hospital.doctor"
    _description = "Doctor"
    _inherit = 'hr.hospital.individual.mixin'
   
    specialization = fields.Char()
    intern = fields.Boolean(default=False)
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                domain="[('intern', '=', False)]")
