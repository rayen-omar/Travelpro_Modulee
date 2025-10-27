from odoo import models, fields

class Achat(models.Model):
    _name = 'achat.approvisionnement'
    _description = 'Achat & Approvisionnement'

    name = fields.Char(string='Nom du produit', required=True)
    quantite = fields.Integer(string='Quantité')
    fournisseur = fields.Char(string='Fournisseur')
