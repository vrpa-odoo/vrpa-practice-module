from odoo import fields,models

class deskAllocation(models.Model):
    _name = "desk.allocation"
    _description = "Regarding the Desk Allocation"

    desk_no = fields.Integer(string="Desk Number")
    desk_type = fields.Selection(
        selection=[('straight desk','Straight desk'),('l shape','L shape')],string="Desk Type"
    )
    is_assigned = fields.Boolean('Assigned')
    sequence = fields.Integer('Sequence',default=1)

    def name_get(self):
        res=[]
        for rec in self:
            res.append((rec.id, '%s - %s'%(rec.desk_no, rec.desk_type)))
        return res