from odoo import models, fields

class Vente(models.Model):
    _name = 'vente.facturation'
    _description = 'Vente & Facturation'

    name = fields.Char(string='Produit', required=True)
    quantite = fields.Integer(string='Quantité')
    prix = fields.Float(string='Prix')
