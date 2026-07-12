{
    'name': 'TransitOps Fuel',
    'version': '1.0.0',
    'author': 'Ajeetha',
    'category': 'TransitOps',
    'summary': 'Manage fuel logs for vehicles',

    'depends': [
        'base',
        'transit_ops',
        'transitops_expenses',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/fuel_log_views.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}



