# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
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
    ],
    'demo': [
        'demo/academy_demo.xml',
    ]
}
