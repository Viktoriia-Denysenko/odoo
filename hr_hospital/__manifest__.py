{
    'name': 'Hospital',
    'version': '15.0.1.0.0',
    'summary': 'My hospital App',
    'author': 'Viktoriia',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/doctor.xml',
        'views/patient.xml',
        'views/disease.xml',
        'views/disease_category.xml',
        'views/visit.xml',
        'views/diagnosis.xml',
        'views/personal_doctor_history.xml',
        'views/research.xml',
        'views/doctor_schedule.xml',
        'wizard/doctor_change_wizard_views.xml',
    ],

    'demo': [
        'data/hr_hospital_disease_category_demo.xml',
        'data/hr_hospital_disease_demo.xml',
    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
