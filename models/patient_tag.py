from odoo import models, fields, api

class PatientTag(models.Model):
    _name = 'om.hospital.patient.tag'
 # <--- THIS IS CRITICAL
    _description = 'Patient Tag'
    _order = 'sequence,id'

    name = fields.Char(string='Patient Tag', required=True, tracking=True)

    sequence = fields.Integer(default=10)

