from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'voyages.reservation'
    _description = 'Réservation de voyage'

    voyage_id = fields.Many2one(
        'voyages.voyage', 
        string='Voyage', 
        required=True, 
        ondelete='cascade'
    )
    amicale_id = fields.Many2one(
        'res.partner',
        string='Amicale / Société',
        domain=[('is_company', '=', True)],
        required=True
    )
    membres_ids = fields.Many2many(
        'res.partner',
        string='Membres',
        domain="[('parent_id', '=', amicale_id)]"
    )
    date_reservation = fields.Date(
        string='Date de réservation', 
        default=fields.Date.today
    )
    nbr_personnes = fields.Integer(
        string='Nombre de participants', 
        compute='_compute_nbr_personnes',
        store=True
    )
    montant_total = fields.Float(
        string='Montant total', 
        compute='_compute_montant_total', 
        store=True
    )
    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ], string='Statut', default='brouillon')

    @api.depends('membres_ids')
    def _compute_nbr_personnes(self):
        for rec in self:
            rec.nbr_personnes = len(rec.membres_ids)

    @api.depends('voyage_id.prix', 'nbr_personnes')
    def _compute_montant_total(self):
        for rec in self:
            rec.montant_total = (rec.voyage_id.prix or 0.0) * rec.nbr_personnes

    def action_confirmer(self):
        for rec in self:
            rec.state = 'confirmee'

    def action_annuler(self):
        for rec in self:
            rec.state = 'annulee'