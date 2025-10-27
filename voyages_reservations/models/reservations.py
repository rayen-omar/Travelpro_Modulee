from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'voyages.reservation'
    _description = 'Réservation de voyage'

    voyage_id = fields.Many2one('voyages.voyage', string='Voyage', required=True, ondelete='cascade')
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    date_reservation = fields.Date(string='Date de réservation', default=fields.Date.today)
    nbr_personnes = fields.Integer(string='Nombre de personnes', default=1)
    montant_total = fields.Float(string='Montant total', compute='_compute_montant_total', store=True)
    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ], string='Statut', default='brouillon')

    @api.depends('voyage_id.prix', 'nbr_personnes')
    def _compute_montant_total(self):
        for reservation in self:
            reservation.montant_total = (reservation.voyage_id.prix or 0.0) * reservation.nbr_personnes

    def action_confirmer(self):
        for reservation in self:
            reservation.state = 'confirmee'

    def action_annuler(self):
        for reservation in self:
            reservation.state = 'annulee'
