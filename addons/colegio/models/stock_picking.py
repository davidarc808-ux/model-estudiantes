from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    estudiante_id = fields.Many2one(
        'colegio.estudiante',
        string="Estudiante"
    )
    
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _prepare_picking(self):
        res = super(SaleOrder, self)._prepare_picking()
        res['estudiante_id'] = self.estudiante_id.id 
        return res
    