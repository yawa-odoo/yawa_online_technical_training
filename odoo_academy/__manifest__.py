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
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ]
}
