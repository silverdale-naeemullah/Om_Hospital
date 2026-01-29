{
    'name': 'Om Hospital',
    'version': '1.0',
    'author': 'Silverdale tech',
    'License': 'LGPL-3',
    'installable': True,
    'application': True,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_tag_views.xml',  # Load this FIRST
        'views/patient_views.xml',
        'views/patient_readonly_view.xml',
        'views/appointment_views.xml',
        'views/menu.xml',  # <--- Use relative paths!
    ]
}
