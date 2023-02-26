from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError


class DiseaseCategory(models.Model):
    _name = "hr.hospital.disease.category"
    _description = "Disease Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char('Name', index=True, required=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    parent_id = fields.Many2one('hr.hospital.disease.category', 'Parent Category', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr.hospital.disease.category', 'parent_id', 'Child Categories')
    disease_count = fields.Integer(
        compute='_compute_disease_count', )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        for obj in self:
            obj.disease_count = self.env['hr.hospital.disease'].search_count([
                ('category_id', 'child_of', obj.id)
            ])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.ondelete(at_uninstall=False)
    def _unlink_except_default_category(self):
        main_category = self.env.ref('hr_hospital.hr_hospital_disease_category_all')
        if main_category in self:
            raise UserError(_("You cannot delete this disease category, it is the default generic category."))