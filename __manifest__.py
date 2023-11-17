# -*- coding: utf-8 -*-
{
    'name' : 'Custom POS Report',
    'version' : '0.1',
    'summary': 'Custom POS Report',
    'sequence': -21,
    'description': """ 
1. Adds image to POS report
2. Use full name (with SKU) on report
    """,
    'category': 'uncategorized',
    'website': '',
    'depends' : ['point_of_sale'],
    'data': [
        'report/report_saledetails_mod.xml',
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}