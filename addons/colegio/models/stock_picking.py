from odoo import models, fields, api

class StockPicking(models.Model):
    # Heredamos el modelo de transferencias (albaranes)
    _inherit = 'stock.picking'

    # 1. Creamos el mismo campo Many2one que tenemos en la Sale Order
    estudiante_id = fields.Many2one(
        'colegio.estudiante', 
        string="Estudiante",
        related='sale_id.estudiante_id',
        store=True
    )

