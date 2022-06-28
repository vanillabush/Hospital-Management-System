


from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 

class patientManagement(models.Model):

    _name = 'medical.patient'
    _description = 'Patient'

     
    patient_ref = fields.Char(string="Patient Number", readonly=True,required=True,copy=False,default='New')
    
    name = fields.Char(compute="_compute_name",string="Fullname", store=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    date_of_birth = fields.Date(string="Date of Birth",required=True)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string="sex",required=True)
    deceased = fields.Selection([('y', 'Yes'),('n', 'No')], string="deceased?",required=True)
    age = fields.Char(compute="_compute_age",string="Patient Age", store=True)
    photo = fields.Binary(string="Picture")
    patient_address = fields.Char(required=True)
    country = fields.Char('Country')
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status',required=True)
    number_of_children = fields.Integer(string="Meals per day")
    primary_care_physician_id = fields.Many2one('medical.physician', string="Primary Care Doctor")
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    critical_info = fields.Text(string="Patient Critical Information")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = fields.Date.today()
                rd = relativedelta(d2,d1)
                rec.age = f"{rd.years}y {rd.months}m {rd.days}d"
            else:
                rec.age = "No Date Of Birth!!"
                
    @api.depends('first_name','last_name')
    def _compute_name(self):
        for rec in self:
            if rec.first_name and rec.last_name:
                rec.name = f"{rec.first_name} {rec.last_name}"
            else:
                rec.name = False
    
    
    @api.model
    def create(self,vals):
        vals['patient_ref'] = self.env['ir.sequence'].next_by_code(
            'medical.patient.sequence'
            ) or 'New'
        result = super(patientManagement,self).create(vals)
        return result
            
              
    @api.onchange('patient_id')
    def _onchange_patient(self):
        address_id = self.patient_id
        self.partner_address_id = address_id