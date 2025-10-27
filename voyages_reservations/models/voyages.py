from odoo import models, fields, api

class Voyage(models.Model):
    _name = 'voyages.voyage'
    _description = 'Voyage'

    name = fields.Char(string='Nom du voyage', required=True)
    description = fields.Text(string='Description')
    prix = fields.Float(string='Prix', required=True)
    date_depart = fields.Date(string='Date de départ', required=True)
    date_retour = fields.Date(string='Date de retour')
    places_totales = fields.Integer(string='Places totales', default=0)
    places_reservees = fields.Integer(string='Places réservées', compute='_compute_places_reservees', store=True)
    places_disponibles = fields.Integer(string='Places disponibles', compute='_compute_places_disponibles', store=True)
    reservation_ids = fields.One2many('voyages.reservation', 'voyage_id', string='Réservations')

    @api.depends('reservation_ids.nbr_personnes', 'reservation_ids.state')
    def _compute_places_reservees(self):
        for voyage in self:
            voyage.places_reservees = sum(r.nbr_personnes for r in voyage.reservation_ids if r.state == 'confirmee')

    @api.depends('places_totales', 'places_reservees')
    def _compute_places_disponibles(self):
        for voyage in self:
            voyage.places_disponibles = voyage.places_totales - voyage.places_reservees
