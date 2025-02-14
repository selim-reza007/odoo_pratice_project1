from odoo import api, models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital doctor'

    name = fields.Char(string="Doctor name")
    contact = fields.Char(string="Contact no.")
    available_days = fields.Char(string="Available in")