# models/patient_tag.py
from odoo import models, fields

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10) # Used for ordering