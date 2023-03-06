from odoo import fields,models

class Evaluatiojn(models.Model):
    _name = "evaluation"
    _description = "This is regarding the Evaluation"
    
    week = fields.Integer(string = 'week')
    odoo_concept = fields.Selection(
        selection=[('ni', 'Needs Improvement'), ('me', 'Meets Expectations'),
                   ('ee', 'Exceeds Expectations'), ('sse', 'Strongly Exceed Expectations')]
    )
    code_quality = fields.Selection(
        selection=[('ni', 'Needs Improvement'), ('me', 'Meets Expectations'),
                   ('ee', 'Exceeds Expectations'), ('sse', 'Strongly Exceed Expectations')]
    )
    productivity = fields.Selection(
        selection=[('ni', 'Needs Improvement'), ('me', 'Meets Expectations'),
                   ('ee', 'Exceeds Expectations'), ('sse', 'Strongly Exceed Expectations')]
    )
    interaction = fields.Selection(
        selection=[('ni', 'Needs Improvement'), ('me', 'Meets Expectations'),
                   ('ee', 'Exceeds Expectations'), ('sse', 'Strongly Exceed Expectations')]
    )
    
    evaluatedby = fields.Many2many("res.users",string = "Evaluated By")
    remarks = fields.Text(string = "Remarks")
    intern_allocation_id = fields.Many2one('intern.allocation')