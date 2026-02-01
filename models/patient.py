from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    # This line is NEW: It gives your model 'social' abilities
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'


    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='DOB')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
