{
    'name': 'TransitOps Maintenance',
    'version': '19.0.1.0.0',
    'author': 'Ajeetha',
    'category': 'Fleet',
    'summary': 'Manage vehicle maintenance schedules and records',

    'depends': [
        'base',
        'transitops_expenses',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/transitops_menu.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}