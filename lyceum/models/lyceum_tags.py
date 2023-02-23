from odoo import fields, models

class LyceumTags(models.Model):
    _name = "lyceum.tags"
    _description = "lyceum tags"

    name = fields.Char(required = True, string="Type")
    color = fields.Integer()