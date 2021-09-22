from odoo import api, fields, models


class ServiceTable(models.Model):
    _name = "service.table"
    s_id = fields.Many2one('event.service', String='No')
    s_details = fields.Char(String='Description')
    quantity = fields.Integer(String='Quantity')
    price = fields.Float(String='Unit Price')
    sub_total = fields.Float(compute='_compute_subtotal', String='Subtotal')

    @api.depends('price')
    def _compute_subtotal(self):
        for rec in self:
            rec.sub_total = rec.price * rec.quantity

