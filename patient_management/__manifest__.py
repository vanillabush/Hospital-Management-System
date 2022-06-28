
{
    'name':'Patient Management',
    'description':"""This module is used to manage Hospital and
     Healthcare Management and Clinic Management apps. """,
    'version':'14.0.1',
    'author':'Ohia Ikenna MarkHenry',
    'depends':['base', 'sale_management', 'stock', 'account'],
    'data':['security/ir.model.access.csv',
            'security/hospital_group.xml',
            'views/main_menu.xml',
            'views/medical_patient_seq.xml',
            'views/medical_physician_seq.xml',
            'views/medical_appointment.xml',
            'views/medical_pathology_category.xml',
            'views/medical_pathology_group.xml',
            'views/medical_pathology.xml',
            'views/medical_patient_disease.xml',
            'views/medical_patient_evaluation.xml',
            'views/medical_patient.xml',
            'views/medical_physician.xml'
            ],
    'application':True,
    "installable": True,
    'sequence':"10",
    
    

}