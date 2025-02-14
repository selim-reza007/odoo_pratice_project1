from odoo import api, models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char(string="Patient name")
    contact = fields.Char(string="Contact no.")