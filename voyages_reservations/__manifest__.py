{
    'name': 'TravelPro - Voyages & Réservations',
    'version': '1.0',
    'summary': 'Gestion des voyages et réservations pour agence de voyage',
    'author': 'Rayen Ben Amor',
    'category': 'Travel',
    'depends': ['base', 'contacts', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/voyages_views.xml',
        'views/reservations_views.xml',
    ],
    'application': True,
}
