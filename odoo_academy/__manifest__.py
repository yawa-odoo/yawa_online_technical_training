# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'application': True,
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to Manage Training:
    """,
    'license': 'LGPL-3',
    'author': 'Odoo',
    'website': 'www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ]
}
