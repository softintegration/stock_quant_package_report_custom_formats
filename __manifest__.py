# -*- coding: utf-8 -*- 


{
    'name': 'Package labels with custom format',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.14',
    'category': 'Inventory/Inventory',
    'demo': [],
    'depends': ['stock','web'],
    'data': [
        'data/report_paperformat_data.xml',
        'data/stock_quant_package_report_custom_formats_data.xml',
        'report/report_package_barcode.xml',
        'report/stock_report_views.xml',
        'views/stock_quant_views.xml'
    ],
    'license': 'LGPL-3',
}
