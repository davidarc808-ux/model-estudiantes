{
    'name': 'Gestión Escolar',
    'version': '1.0',
    'depends': ['base', 'sale', 'stock', ], 
    'data': [
        'security/ir.model.access.csv',
        'views/estudiante_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': True,
}