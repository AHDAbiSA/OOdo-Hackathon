{
    'name': 'TransitOps Reports',
    'version': '17.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Fleet KPIs and analytics dashboard',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        '../frontend/transitops_reports/views/report_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
