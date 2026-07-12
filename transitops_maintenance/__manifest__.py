{
    'name': 'TransitOps Maintenance',
    'version': '17.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Manage vehicle maintenance records',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
