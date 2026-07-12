{
    'name': 'TransitOps Reports',
    'version': '19.0.1.0.0',
    'author': 'Ajeetha',
    'category': 'Fleet',
    'summary': 'Generate analytical reports for TransitOps modules',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/transitops_menu.xml',
        'views/report_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

