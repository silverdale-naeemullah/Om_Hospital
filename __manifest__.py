{
    'name': 'Hospital Management System',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Odoo Mates',
    'summary': 'Hospital Management System for Odoo 18',
    'description': """
        This module manages Hospital Operations including Patients, 
        Appointments, and Medical Records.
    """,
    'license': 'LGPL-3',


    'depends': ['base', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/patient_tag_views.xml', # New file added
        'views/appointment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}