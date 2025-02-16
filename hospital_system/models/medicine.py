from odoo import api, fields, models

class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Hospital Medicine'

    name = fields.Char(string="Medicine name")
    unite_price = fields.Float(string="Price")