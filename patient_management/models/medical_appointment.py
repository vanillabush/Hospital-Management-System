


from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class medical_appointment(models.Model):
    _name = "medical.appointment"
    _inherit = 'mail.thread'
    
    name = fields.Char(string="Appointment ID", readonly=True, copy=True)
    patient_id = fields.Many2one('medical.patient','Patient',required=True)
    appointment_type = fields.Selection([
			('new', 'New'),
			('scheduled', 'Scheduled'),
			('regular', 'Regular'),
		], 'Appointment Type', sort=False,default='outpatient')
    urgency_level = fields.Selection([
			('a', 'Normal'),
			('b', 'Urgent'),
			('c', 'Medical Emergency'),
		], 'Urgency Level', sort=False,default="b")
    appointment_date = fields.Datetime('Appointment Date',required=True,default = fields.Datetime.now)
    appointment_end = fields.Datetime('Appointment End',required=True)
    doctor_id = fields.Many2one('medical.physician','Physician',required=True)
    notes = fields.Text(string="Info")


    @api.model 
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
        msg_body = 'Appointment created'
        for msg in self:
          msg.message_post(body=msg_body)
        result = super(medical_appointment, self).create(vals)
        return result

    def confirm(self):
      self.write({'state': 'confirmed'})

    def done(self):
      self.write({'state': 'done'})

    def cancel(self):
      self.write({'state': 'cancel'})

