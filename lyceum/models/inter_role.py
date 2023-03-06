from odoo import fields,models

class internRole(models.Model):
    _name = "intern.role"
    _description = "This is regarding the intern role allocation"
    
    name = fields.Char(string='Name',required = True)
    intern_type_ids = fields.One2many('intern.allocation','intern_type' , string='Intern Name')