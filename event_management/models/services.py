from odoo import api, fields, models


class EventService(models.Model):
    _name = "event.service"
    _description = "Services"
    s_name = fields.Char(String='Name')
    res_person = fields.Many2one('res.partner', String='Responsible Person')
    table_ids = fields.One2many('service.table', 's_id')
    amount_total = fields.Float(String='Total')

    @api.onchange('table_ids')
    def onchange_sum(self):
        val = 0
        for rec in self.table_ids:
            val += rec.sub_total
            self.amount_total = val
