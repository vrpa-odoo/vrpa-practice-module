from odoo import api,fields, models

class InternRoles(models.Model):
    _name = "role.allocation"
    _description="Intern Roles"

    intern_name = fields.Char(string="Name")
    intern_mobno = fields.Char(sting="Mobile Number")
    intern_joiningdate = fields.Char(string="Joining Date")