import datetime

from odoo import api, fields, models


class Catering(models.Model):
    _name = "event.catering"
    _description = "Catering"
    _rec_name = 'event_date'
    event_id = fields.Many2one('event.booking', String='Event')
    event_date = fields.Date(String='Date')
    start_date = fields.Date(String='Start Date')
    end_date = fields.Date(String='End Date')
    guests = fields.Integer(String='Guests')
    welcome_drink = fields.Boolean(String='Welcome Drink')
    breakfast = fields.Boolean(String='Breakfast')
    lunch = fields.Boolean(String='Lunch')
    dinner = fields.Boolean(String='Lunch')
    snacks = fields.Boolean(String='Snacks And Drinks')
    beverages = fields.Boolean(String='Beverages')
    drink_ids = fields.One2many('catering.table', 'cat_id')
    breakfast_ids = fields.One2many('catering.table', 'cat_id')
    lunch_ids = fields.One2many('catering.table', 'cat_id')
    dinner_ids = fields.One2many('catering.table', 'cat_id')
    snack_ids = fields.One2many('catering.table', 'cat_id')
    beverage_ids = fields.One2many('catering.table', 'cat_id')
    drink_total = fields.Float(String='Total1')
    breakfast_total = fields.Float(String='Total2')
    lunch_total = fields.Float(String='Total3')
    dinner_total = fields.Float(String='Total4')
    snacks_total = fields.Float(String='Total5')
    beverages_total = fields.Float(String='Total6')
    grand_total = fields.Float(compute='_compute_total', String='Grand Total')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('delivered', 'Delivered'),
                              ('invoiced', 'Invoiced'),
                              ('expired', 'Expired')], default='draft',
                             String='Status')
    current_date = fields.Date(default=fields.Date.today())

    @api.onchange('event_id')
    def change_date(self):
        for rec in self:
            rec.event_date = rec.event_id.event_date
            rec.start_date = rec.event_id.start_date
            rec.end_date = rec.event_id.end_date

    @api.onchange('drink_ids')
    def onchange_drink(self):
        val = 0
        for rec in self.drink_ids:
            val += rec.sub_total
            self.drink_total = val

    @api.onchange('breakfast_ids')
    def onchange_breakfast(self):
        val = 0
        for rec in self.breakfast_ids:
            val += rec.sub_total
            self.breakfast_total = val

    @api.onchange('lunch_ids')
    def onchange_lunch(self):
        val = 0
        for rec in self.lunch_ids:
            val += rec.sub_total
            self.lunch_total = val

    @api.onchange('dinner_ids')
    def onchange_dinner(self):
        val = 0
        for rec in self.dinner_ids:
            val += rec.sub_total
            self.dinner_total = val

    @api.onchange('snack_ids')
    def onchange_snack(self):
        val = 0
        for rec in self.snack_ids:
            val += rec.sub_total
            self.snacks_total = val

    @api.onchange('beverage_ids')
    def onchange_beverage(self):
        val = 0
        for rec in self.beverage_ids:
            val += rec.sub_total
            self.beverages_total = val

    @api.depends('drink_ids', 'breakfast_ids', 'lunch_ids', 'dinner_ids',
                 'beverage_ids')
    def _compute_total(self):
        val = 0
        for rec in self:
            val = rec.drink_total + rec.breakfast_total + rec.lunch_total + \
                  rec.dinner_total + rec.snacks_total + rec.beverages_total
            self.grand_total = val

    @api.onchange('start_date')
    def onchange_state(self):
        for day in self:
            start_date = fields.Date.to_string(day.start_date)
            current_date = fields.Date.to_string(day.current_date)
            if start_date and current_date:
                print(start_date, type(start_date))
                print(current_date, type(current_date))
                date_format = '%Y-%m-%d'
                d1 = datetime.datetime.strptime(start_date, date_format).date()
                print(d1, type(d1))
                d2 = datetime.datetime.strptime(current_date, date_format).\
                    date()
                print(d2, type(d2))
                if d2 >= d1:
                    self.state = 'expired'

    def action_catering_confirm(self, line=None):
        self.state = 'confirmed'
        if self.state == 'confirmed':
            catering_obj = self.env['event.booking']
            rec = catering_obj.search([('event_date', '=', self.event_date)])
            if rec:
                rec.state = 'confirmed'
        for rec in self.drink_ids:
            line = self.env['booking.table'].create(
                {
                    'product_id': rec.product_id.id,
                    'description': rec.description,
                    'uom_id': rec.uom_id.id
                }
            )

    def action_catering_delivered(self):
        self.state = 'delivered'
