from odoo import fields, models, api

class Student(models.Model):
    _name = "school.student"
    _description = "School student model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "studentName"

    studentName = fields.Char(string="Name")
    studentDob = fields.Date(string="Date of birth")
    studentClass = fields.Char(string="Class", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    teacher_id = fields.Many2one('res.users', string="Teacher")
    address = fields.Html(string="Address")