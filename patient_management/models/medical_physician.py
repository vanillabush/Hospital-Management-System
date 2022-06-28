


from odoo import models, fields, api, _

class medical_physician(models.Model):
    _name="medical.physician"
    

    name = fields.Char(compute="_compute_name",readonly=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    doc_ref = fields.Char(string="Doctor Number", readonly=True,required=True,copy=False,default='New')
    info = fields.Text('Extra Info')
    
    
    @api.depends('first_name','last_name')
    def _compute_name(self):
        for rec in self:
            if rec.first_name and rec.last_name:
                rec.name = f"{rec.first_name} {rec.last_name}"
            else:
                rec.name = False
                
    @api.model
    def create(self,vals):
        if vals.get('doc_ref','New') =='New':
            vals['doc_ref'] = self.env['ir.sequence'].next_by_code(
                'medical.physician.sequence'
            ) or 'New'
        result = super(medical_physician,self).create(vals)
        return result