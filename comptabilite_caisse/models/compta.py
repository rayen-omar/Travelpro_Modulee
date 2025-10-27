from odoo import models, fields

class Comptabilite(models.Model):
    _name = 'compta.caisse'
    _description = 'Comptabilité & Caisse'

    name = fields.Char(string='Libellé')
    montant = fields.Float(string='Montant')
    type_op = fields.Selection([('depense', 'Dépense'), ('recette', 'Recette')], string='Type')
