from odoo import fields, models

class LyceumCreate(models.Model):
    _name = "lyceum.create"
    _description = "lyceum create"

    ly_name = fields.Char()
    
    ly_description = fields.Text()
    ly_area = fields.Integer()
    ly_capacity = fields.Integer()
    ly_projectoravailable=fields.Boolean()
