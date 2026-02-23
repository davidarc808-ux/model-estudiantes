from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Relacionamos el pedido de venta con un estudiante
    estudiante_id = fields.Many2one(
        'colegio.estudiante', 
        string="Estudiante Beneficiario"
    )