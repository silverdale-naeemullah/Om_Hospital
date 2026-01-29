from odoo import models, fields, api

class Patient(models.Model):
    _name = 'om.hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <--- THIS IS CRITICAL
    _description = 'Patient'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email Address')
    address = fields.Char(string='Address')

    tag_ids=fields.Many2many('om.hospital.patient.tag', string='Tags')
