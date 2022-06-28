from odoo import api, fields, models, _


class ResPatient(models.Model):
    _inherit = 'res.partner'
    
    is_patient = fields.Boolean("Is patient?")