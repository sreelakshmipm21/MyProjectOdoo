from odoo import fields, models


class WorkOrderMachine(models.Model):
    _name = "work.machine"
    _description = "WorkOrder Machine"
    name = fields.Char(string='Name', required=True)
