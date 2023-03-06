from odoo import fields,models

class laptopAllocation(models.Model):
    _description = "This is regarding the laptop allocation"
    _name = "laptop.allocation"
    
    name = fields.Char(string='Name',required = True)
    technician_name = fields.Char(string = 'Technician Name')
    model = fields.Char(string='Model')
    location = fields.Char(string = 'Used in Location')
    war_expire =fields.Date(string='Warranty Expiration Date')
    mac_address=fields.Char(string="Mac Address")
    intern_name_ids=fields.One2many("intern.allocation", 'laptop_assigned', string="Intern Name" )