from odoo import fields,models

class PersonalModule(models.Model):
    _name = "personal.module"
    _description = "This is regarding the personal module page"
    
    module_name =fields.Char(String="Module Name")
    doc_file =fields.Char(string="Document file")
    models = fields.Text(string = "Models")
    documentation =fields.Char(string="Documentation Link")
    github = fields.Char(string="Github Link")  
    intern_personal_id = fields.Many2one("intern.allocation")