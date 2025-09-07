{
    'name': 'Collaborative Clicker',
    'summary': '''
        Small App to demonstrate how to get real updates in the frontend using OWL and the bus,
        using 'bus.listener.mixin'.
    ''',
    'application': True,
    'version': '1.0.0',
    'author': 'Paco Coca',
    'license': 'GPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/clicker_game_views.xml',
        'views/collaborative_clicker_menus.xml',
    ],
    'depends': [
        'bus',
    ],
    'assets': {
        'web.assets_backend': [
            'collaborative_clicker/static/src/**/*',
        ],
    },
}
