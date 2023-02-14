from odoo import models, fields


class Visit(models.Model):

    _name = "hr.hospital.visit"
    _description = "Visit"

    name = fields.Char()

    active = fields.Boolean(
        default=True,
    )
