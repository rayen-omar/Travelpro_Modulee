from odoo import models, fields

class CRMClient(models.Model):
    _name = 'crm.client'
    _description = 'Client'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
