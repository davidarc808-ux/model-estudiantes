from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    
    estudiante_id = fields.Many2one(
        'colegio.estudiante', 
        string="Estudiante Beneficiario"
    )