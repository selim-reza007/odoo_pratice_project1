from odoo import api, models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'hospital appointment'
    _rec_name = 'patient_name'

    patient_name = fields.Many2one('hospital.patient', string="hospital.patient")
    appointment_time = fields.Datetime(default=fields.Datetime.now)
    medicine_line_ids = fields.One2many('appointment.medicine.line','appointment_id',string="Medicine")


class AppointmentMedicineLine(models.Model):
    _name = 'appointment.medicine.line'
    _description = 'appointment medicine line'
    _rec_name = 'medicine_name'

    medicine_name = fields.Many2one('hospital.medicine', string='Medicine')
    price = fields.Float(string="Price")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")