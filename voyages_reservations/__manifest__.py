{
    'name': 'TravelPro - Voyages & Réservations',
    'version': '1.1',
    'summary': 'Gestion des voyages et réservations pour agence de voyage (centré sur amicale)',
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
