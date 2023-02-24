from odoo import fields, models

class LyceumCreate(models.Model):
    _name = "lyceum.create"
    _description = "lyceum create"
    _rec_name="ly_name"

    ly_name = fields.Char()
    ly_description = fields.Text()
    ly_tags_ids = fields.Many2many("lyceum.tags",string="Tags")
    ly_area = fields.Integer()
    ly_capacity = fields.Integer()
    ly_projectoravailable=fields.Boolean()
    ly_status=fields.Selection(string='Status',selection=[('available',"Available"),('reserved',"Reserved")])
    # ly_id = fields.One2many("event.create","event_lyceum_list")