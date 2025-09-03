{
    'name': 'Real Time',
    'summary': '''
        Small App to demonstrate how to get real updates in the frontend using OWL and the bus.
    ''',
    'application': True,
    'version': '1.0.0',
    'author': 'Paco Coca',
    'license': 'GPL-3',
    'data': [
        'views/sale_order_views.xml',
    ],
    'depends': [
        'sale_management',
    ],
    'assets': {
        'web.assets_backend': [
            'real_time/static/src/**/*',
        ],
    },
}
