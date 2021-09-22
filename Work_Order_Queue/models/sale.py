from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    work_order_machine = fields.Many2one('work.machine', string='Machine')
    materials_received = fields.Boolean(String='Materials Received')
    delivery_date = fields.Date(String='Delivery Date')

