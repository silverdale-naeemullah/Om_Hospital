from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'
    # Add this line to search by both patient and reference
    _rec_names_search = ['patient_id', 'reference']

    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    date_appointment = fields.Date(string='Date', required=True, tracking=True)
    note = fields.Text(string='Note')

    # State field for Status Bar [00:01:31]
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    # ADD THIS LINE:
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)

    # One2many field definition
    # Parameters: (Co-model name, Inverse field name in the co-model)
    appointment_line_ids = fields.One2many(
        'hospital.appointment.line',
        'appointment_id',
        string='Lines'
    )
    # 1. Define the field with 'compute' attribute [00:02:22]
    total_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty", store=True)

    # 2. Define the compute logic [00:02:50]
    @api.depends('appointment_line_ids.qty')  # Recompute when a line quantity changes [00:11:44]
    def _compute_total_qty(self):
        for rec in self:
            # Simple way: sum the qty of all lines [00:07:00]
            rec.total_qty = sum(rec.appointment_line_ids.mapped('qty'))

    def _compute_display_name(self):
        for rec in self:
            name = rec.patient_id.name
            if rec.reference:
                # Combining reference and name using Python f-string
                rec.display_name = f"[{rec.reference}] {name}"
            else:
                rec.display_name = name

    # Button Action Methods [00:11:15]
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference', 'New') == 'New':
                # Fetches the sequence defined in Step 1
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'New'
        return super().create(vals_list)








class HospitalAppointmentLine(models.Model):
    _name = "hospital.appointment.line"
    _description = "Hospital Appointment Line"

    # [00:03:45] This is the RELATIONAL FIELD.
    # It is a Many2one field pointing back to the parent model.
    # This is required for the One2many relationship to work.

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    product_id = fields.Many2one('product.product', string='Product')  # This is the field Odoo was missing!
    qty = fields.Integer(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
