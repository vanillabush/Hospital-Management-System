


from odoo import models, fields,api, _

class medical_patient_evaluation(models.Model):
    _name = 'medical.patient.evaluation'
    _rec_name = 'medical_patient_id'
    
    patient_id = fields.Many2one('res.partner', domain=[('is_patient','=',True)], string="Patient")
    medical_patient_id = fields.Many2one('medical.patient',string="Patient")
    start_evaluation = fields.Datetime(string="Start Evaluation")
    physician_partner_id = fields.Many2one('medical.physician', string="Primary Care Doctor")
    end_evaluation = fields.Datetime(string="End of Evaluation")
    evaluation_type = fields.Selection([
		('a','Ambulatory'),
		('e','Emergency'),
		('i','Inpatient'),
		('pa','Pre-arranged appointment'),
		('pc','Periodic Control'),
		('p','Phone Call'),
		('t','Telemedicine'),
	], string='Type')
    chief_complaint = fields.Char('Chief Complaint')
    information_source = fields.Char('source')
    reliable_info = fields.Boolean('Reliable')
    present_illness = fields.Text(string='Present Illness')
    
    weight = fields.Float(string='Weight (kg)',help='Weight in Kilos')
    height = fields.Float(string='Height (cm)')
    abdominal_circ = fields.Float(string='Abdominal Circumference')
    hip = fields.Float(string='Hip')
    bmi = fields.Float(string='Body Mass Index')
    whr = fields.Float(string='WHR')
    head_circumference = fields.Float(string='Head Circumference')
    malnutrition = fields.Boolean('Malnutrition')
    dehydration = fields.Boolean('Dehydration')
    systolic = fields.Integer('Systolic Pressure')
    loc = fields.Integer('Level of Conciuosness')
    judgment = fields.Boolean('Judgment')
    medical_appointment_date_id = fields.Many2one('medical.appointment','Appointment Date')
    
    tag = fields.Integer(
		string='Last TAGs',
		help="Triacyglycerol(triglicerides) level can be approximative",
	)
    is_tremor = fields.Boolean(
		string='tremor',
		help='Check if patient shows signs of tremor'
	)
    mood = fields.Selection([
		('n','Normal'),
		('s','Sad'),
		('f','Fear'),
		('r','Rage'),
		('h','Happy'),
		('d','Disgust'),
		('e','Euphoria'),
		('fl','Flat'),
	], string='Mood')
    glycemia = fields.Float(
		string='Glycemia',
		help="Last blood lucose level can be approximative"
	)
    evaluation_summary = fields.Text(string='Evaluation Summary')
    osat = fields.Integer(string='Oxygen Saturation',help='Oxygen Saturation(arterial).')
    bpm = fields.Integer(string='Heart Rate',help='Heart rate expressed in beats per minute')
    loc_eyes = fields.Selection([
		('1','Does not open Eyes'),
		('2', 'Opens eyes in response to painful stimuli'),
		('3', 'Opens eyes in response to voice'),
		('4', 'Opens eyes spontaneously'),
	],string='Glasgow - Eyes')
    loc_verbal = fields.Selection([
		('1','Make no sounds'),
		('2','Incomprehensible sounds'),
		('3','Utters inappropriate words'),
		('4','Confused,disoriented'),
		('5','Oriented, converses normally'),
	],string='Glasgow-verbal')
    loc_motor = fields.Selection([
		('1','Make no movement'),
		('2','Extension to painful stimuli decerebrate response'),
		('3','Abnormal flexion to painful stimuli decerebrate response'),
		('4','Flexion/withdrawal to painful stimuli'),
		('5','Localizes painful stimuli'),
		('6','Obeys commands')
	],string='Glasgow - motor')
    violent = fields.Boolean('Voilent Behavior')
    orientation = fields.Boolean('Orientation')
    memory = fields.Boolean('Memory')
    judgement = fields.Boolean('Judgement')
    next_appointment_id = fields.Many2one('medical.appointment','Next Appointment')
    