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
    'version': '1.0.1.9',
    'category': 'Inventory/Inventory',
    'demo': [],
    'depends': ['stock','web'],
    'data': [
        'data/report_paperformat_data.xml',
        'report/report_package_barcode.xml',
        'report/stock_report_views.xml',
        'views/stock_quant_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'stock_quant_package_report_custom_formats/static/src/css/custom.css',
            'stock_quant_package_report_custom_formats/static/src/fonts/myriad/stylesheet.css',
        ],
    },
    'license': 'LGPL-3',
}
