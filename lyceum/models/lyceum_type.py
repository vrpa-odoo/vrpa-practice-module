from odoo import fields, models

class LyceumType(models.Model):
    _name = "lyceum.type"
    _description = "lyceum type"

    name = fields.Char(required = True, string="Type")
    projectoravialable = fields.Boolean(required = True, string="Projector Avialble")
