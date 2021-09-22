from odoo import api, fields, models


class BookingTable(models.Model):
    _name = "booking.table"
    _description = "Booking Tables"
    book_id = fields.Many2one('event.booking')
    product_id = fields.Many2one('catering.table', String='Product')
    description = fields.Char(String='Description')
    uom_id = fields.Many2one('uom.uom', string='UOM', required=True)
    quantity = fields.Integer(String='Quantity')
    price = fields.Float(String='Unit Price')
    sub_total = fields.Float(compute='_compute_total', String='Subtotal')

    @api.onchange('product_id')
    def change_date(self):
        for rec in self:
            rec.uom_id = rec.product_id.uom_id
            rec.price = rec.product_id.price

    @api.depends('quantity')
    def _compute_total(self):
        for val in self:
            val.sub_total = val.price * val.quantity
