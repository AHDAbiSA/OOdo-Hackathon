{
    'name': 'TransitOps Fuel',
    'version': '19.0.1.0.0',
    'author': 'Ajeetha',
    'category': 'Fleet',
    'summary': 'Track fuel usage and costs',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/transitops_menu.xml',
        'views/fuel_log_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

