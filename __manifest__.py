{
    'name': 'TravelPro Module',
    'version': '1.0',
    'category': 'Travel Management',
    'summary': 'Module principal regroupant tous les modules TravelPro',
    'description': 'Gestion complète des voyages, réservations, ventes, achats, comptabilité et CRM',
    'author': 'Rayen Ben Amor',
    'depends': ['base', 'contacts', 'sale', 'account'],
    'data': [
        # Modules secondaires

        'views/travel_menu.xml',
        'voyages_reservations/security/ir.model.access.csv',
        'voyages_reservations/views/voyages_views.xml',
        'voyages_reservations/views/reservations_views.xml',
        'voyages_reservations/views/menu.xml',
   
        
        
        

        'achat_approvisionnement/security/ir.model.access.csv',
        'achat_approvisionnement/views/achat_views.xml',

        'vente_facturation/security/ir.model.access.csv',
        'vente_facturation/views/vente_views.xml',

        'comptabilite_caisse/security/ir.model.access.csv',
        'comptabilite_caisse/views/compta_views.xml',

        'client_manager/security/ir.model.access.csv',
        'client_manager/views/crm_views.xml',
    ],
    'installable': True,
    'application': True,
}
