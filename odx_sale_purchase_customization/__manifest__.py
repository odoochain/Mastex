# -*- coding: utf-8 -*-

{
    'name': 'Sale & Purchase Customization',
    'category': 'Sale, Purchase',
    'sequence': 14,
    'summary': 'Purchase Order is created while conforming the Sale Order and vice versa ',
    'description': """
        Adding sequence to  customers and including it in name get and name search. 
        New fields is added in both sale order and purchase order. While confirming sale order,a purchase
        order is created based on the corresponding sale order and vice versa.
    """,
    'author': 'Odox SoftHub / Albin /Ashif',
    'website': 'https://www.odoxsofthub.com',
    'version': '13.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'report_xlsx', 'odx_sale_discount_total', 'purchase_total_discount'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sale_purchase_customization_data.xml',
        'views/res_partner.xml',
        'views/sale_views.xml',
        'views/purchase_views.xml',
        'views/purchase_landing_cost_view.xml',
        'views/account_move_views.xml',
        'report/sale_report_template.xml',
        'report/purchase_report.xml',
        'report/rfq_print.xml',
        'views/purchase_shipment_view.xml',
        'views/ir_attachment_view.xml',
        'report/instruction_report_template.xml',
        'report/report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
