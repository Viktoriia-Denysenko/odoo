{
    'name': 'Hospital',
    'version': '15.0.1.0.0',
    'description': '',
    'summary': 'My hospital',
    'author': 'Viktoriia',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'depends': [
        'base',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        
        'views/menu.xml',
        'views/doctor.xml',
    ],
    'demo': [],
    
    'application': False,
    'installable': True,
    'auto_install': False,
    'assets': {
        
    }
}