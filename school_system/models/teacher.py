from odoo import api, fields, models
from datetime import date


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "school teacher"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name")
    department = fields.Char(string="Department")
    dob = fields.Date(string="Date of Birth")
    joinDate = fields.Datetime(string="Joined")
    student_id = fields.Many2one('school.student', string="Student")
    studentClass = fields.Char(string="Student's class")
    studentDob = fields.Date(related="student_id.studentDob")
    age = fields.Integer(string="Age", compute="calculateAge")
    profile = fields.Html(string="Upload Profile pdf")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",
        help='Teacher feedback')
    state = fields.Selection([('to do', 'To Do'), ('done', 'Done'), ('cancelled','Cancelled')], string='Status', default='open', required=True)

    def action_todo(self):
        for record in self:
            record.state = "to do"

    def action_done(self):
        for record in self:
            record.state = "done"

    def action_cancelled(self):
        for record in self:
            record.state = "cancelled"

    @api.depends('dob')
    def calculateAge(self):
        for record in self:
            today = date.today()
            if record.dob:
                record.age = today.year - record.dob.year
            else:
                record.age = 1

    @api.onchange('student_id')
    def studentInfo(self):
        self.studentClass = self.student_id.studentClass

    def donesuccess(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "<strong><b>Good job!</b> You went through all steps of this tour.</strong>",
                'type': 'rainbow_man',
            }
        }