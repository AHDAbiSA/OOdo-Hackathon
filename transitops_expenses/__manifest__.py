{
    'name': 'TransitOps Expenses',
    'version': '17.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Record operational expenses',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/expense_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
