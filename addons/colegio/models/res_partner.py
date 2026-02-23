from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Relacionamos el contacto con el estudiante (Many2one)
    # Esto permitirá que en la ficha de un contacto elijas a un estudiante
    estudiante_id = fields.Many2one(
        'colegio.estudiante', 
        string="Estudiante Asignado"
    )