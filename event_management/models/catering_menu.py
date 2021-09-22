from odoo import fields, models


class CateringMenu(models.Model):
    _name = "catering.menu"
    _description = "Catering Menu"
    _rec_name = 'dish_name'
    dish_name = fields.Char(String='Name')
    category = fields.Selection([
        ('welcome_drink', 'Welcome Drink'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks And Drinks'),
        ('beverages', 'Beverages')
    ])
    image = fields.Binary(String='image')
    uom_id = fields.Many2one('uom.uom', string='UOM', required=True)
    price = fields.Float(String='Unit Price')

