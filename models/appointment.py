from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'om.hospital.appointment'

    # define the inheritance from odoo.

    _inherit = ['mail.thread', 'mail.activity.mixin']  # <--- THIS IS CRITICAL
    _description = 'appointment'
    _rec_name = 'patient_id'

    reference=fields.Char(string='Patient Reference', default='New')

    #define the relation to other connected tables. which in this case will be many to one as a patient can have man
    # appointments.
    patient_id = fields.Many2one(comodel_name='om.hospital.patient', string='Patient')


    #define the fields or data that will go into the tables.
    name = fields.Char(string='Patient Name', tracking=True)
    date_of_appointment = fields.Date(string='Date of appointment', required=True)
    note = fields.Text(string='Note')

    # Updated state field with 'done' and 'cancel'
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string="Status", default='draft', tracking=True)


    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                # Passing the sequence code heres
                vals['reference'] = self.env['ir.sequence'].next_by_code('om.hospital.appointment')
        return super().create(vals_list)

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'
            print('Confirm button clicked:', self, record)

    def action_ongoing(self):
        for record in self:
            record.state = 'ongoing'
            print('Ongoing button clicked:', self, record)

    def action_done(self):
        for record in self:
            record.state = 'done'
            print('Done button clicked:', self, record)

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
            print('Cancel button clicked:', self, record)

    def action_draft(self):
        for record in self:
            record.state = 'draft'
            print('Reset to Draft button clicked:', self, record)