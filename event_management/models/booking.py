import datetime

from odoo import api, fields, models


class EventBooking(models.Model):
    _name = "event.booking"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Event Types"
    name = fields.Char(String='Name')
    event_type = fields.Many2one('event.type', String='Event Type')
    customer_id = fields.Many2one('res.partner', String="Customer")
    event_date = fields.Date(string='Book Date')
    start_date = fields.Datetime(String='Start Date')
    end_date = fields.Datetime(string='End Date')
    time_duration = fields.Integer(compute='difference_date',
                                   String='Time Duration', Store=True,
                                   readonly=False, copy=False, tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')],
                             default='draft', String='Status')
    table_ids = fields.One2many('booking.table', 'book_id')

    @api.depends('end_date')
    def difference_date(self):
        for day in self:
            start_date = fields.Date.to_string(day.start_date)
            end_date = fields.Date.to_string(day.end_date)
            if start_date and end_date:
                print(start_date, type(start_date))
                print(end_date, type(end_date))
                date_format = '%Y-%m-%d'
                d1 = datetime.datetime.strptime(start_date, date_format).date()
                print(d1, type(d1))
                d2 = datetime.datetime.strptime(end_date, date_format).date()
                print(d2, type(d2))
                if d2 >= d1:
                    day.time_duration = (d2-d1).days + 1
                    print(d2 - d1, type(d2-d1))
                else:
                    raise ValueError("end date should be superior than start "
                                     "days")

    def name_get(self):
        result = []
        for rec in self:
            print(rec)
            start_date = fields.Date.to_string(rec.start_date)
            end_date = fields.Date.to_string(rec.end_date)
            customer = rec.customer_id.name
            result.append((rec.id, '%s : %s / %s : %s' % (rec.event_type.name,
                                                          customer,
                                                          start_date,
                                                          end_date)))
        return result

    @api.model
    def action_catering(self, context):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Catering',
            'view_mode': 'form',
            'res_model': 'event.catering',
            'view_id': self.env.ref('event_management.event_catering_form').id,
            'target': 'current',

        }

    def action_booking_confirm(self):
        self.state = 'confirmed'







