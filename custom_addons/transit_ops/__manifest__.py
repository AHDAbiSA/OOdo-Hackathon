# -*- coding: utf-8 -*-
{
    'name': 'TransitOps Core',
    'version': '18.0.1.0.0',
    'summary': 'Core module for TransitOps management system',
    'sequence': 1,
    'description': """
TransitOps Core Module
======================
This is the base custom module for the TransitOps system.
    """,
    'category': 'Operations',
    'author': 'TransitOps team',
    'website': 'https://www.transitops.example.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/transit_ops_security.xml',
        'security/ir.model.access.csv',
        'views/transit_vehicle_views.xml',
        'views/transit_driver_views.xml',
        'views/transit_menus.xml',
    ],
    'demo': [
        'demo/users_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            # JS and CSS/SCSS assets will be added here
        ],
    },
}
