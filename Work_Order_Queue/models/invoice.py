from odoo import api, fields, models


class InvoiceMultipleSo(models.Model):
    _inherit = "account.move"
    so_ids = fields.Many2many('sale.order', string="Related SO",
                              domain=[('invoice_status', '=', 'to invoice')])

    @api.onchange('so_ids')
    def onchange_product_id(self):
        for rec in self:
            lines = [(5, 0)]
        for i in self.so_ids.order_line:
            val = {
                'product_id': i.product_id.id,
                'name': i.name,
                'price_unit': i.price_unit,
                'price_subtotal': i.price_subtotal,
            }
            lines.append([0, 0, val])
            rec.invoice_line_ids = lines
