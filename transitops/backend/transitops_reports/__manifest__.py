{
    'name': 'TransitOps Reports',
    'version': '19.0.1.0.0',
    'author': 'Ajeetha',
    'category': 'Fleet',
    'summary': 'Generate analytical reports for TransitOps modules',

    'depends': [
        'base',
        'transitops_expenses',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/report_views.xml',
        'views/transitops_menu.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

