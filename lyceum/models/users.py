from odoo import fields,models

class Users(models.Model):
    _inherit='res.users'

    intern_ids = fields.One2many('intern.allocation','coach',string="Intern Name")