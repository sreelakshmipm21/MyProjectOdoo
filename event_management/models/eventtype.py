from odoo import fields, models


class EventTypes(models.Model):
    _name = "event.type"
    _description = "Event Types"
    name = fields.Char(String='Name')
    code = fields.Char(String='Code')
    image = fields.Binary(String='Image')
