{
    'name': 'TransitOps Fuel',
    'version': '17.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Track fuel logs and efficiency',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        '../frontend/transitops_fuel/views/fuel_log_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
