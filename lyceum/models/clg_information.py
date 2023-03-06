from odoo import fields, models

class CollegeInformation(models.Model):
    _name = "college.information"
    _description = "Regarding intern college information"

    name = fields.Char(string="Name")
    clg_name_ids=fields.One2many('intern.allocation','clg_name',string='College Name')
    