from datetime import timedelta
from odoo import api,fields, models

class EventCreate(models.Model):
    _name = "event.create"
    _description="Create Event"
    _rec_name="event_name"
    
    event_lyceum_list = fields.Many2one("lyceum.create",string="Lyceum List")
    event_lyceum_available = fields.Char(string="Availability")
    event_name=fields.Char(string="Organize")
    event_description=fields.Text(string="Description")
    event_fromdatetime=fields.Datetime(string ="From Date")
    event_todatetime=fields.Datetime(string="To Date")
    event_totaltime=fields.Char(string="Total Time", compute="_compute_total_time")
    event_projector_needed=fields.Boolean(string="Projector Needed")
    event_capacity_needed=fields.Integer(string="Number of Attendes")
    event_details=fields.Text("Event Agenda")
    event_organizer_name=fields.Many2one("res.users")
    event_phone_number = fields.Char("Phone Number")
    event_email = fields.Char("Email")
    state = fields.Selection(string="state",selection=[('new','New'),('requested',"Requested"),('approved',"Approved"),('cancel',"Cancelled")],default='new')

    def action_request(self):
        for record in self:
            record.state = "requested"
        return True
    
    def action_approve(self):
        for record in self:
            record.state = "approved"
        return True
    
    def action_cancel(self):
        for record in self:
            record.state = "cancel"
        return True
    
    @api.depends("event_fromdatetime","event_todatetime")
    def _compute_total_time(self):
        for record in (self):
            record.event_totaltime=record.event_todatetime-record.event_fromdatetime
    
    # def _inverse_total_time(self):
    #     for record in self:
    #         record.event_todatetime=record.event_fromdatetime+record.event_totaltime
    # #         # date_field2 = date_field1 + timedelta(hours=5,minutes=30)

    # @api.depends("event_fromdatetime","event_todatetime")
    # def _compute_availability(self):
    #     for record in self:
    #         if record.