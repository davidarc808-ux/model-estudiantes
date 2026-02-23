from odoo import models, fields

class Estudiante(models.Model):
    _name = 'colegio.estudiante'
    _description = 'Registro de Estudiantes'

    name = fields.Char(string="Nombre", required=True)
    apellido_paterno = fields.Char(string="Apellido Paterno")
    apellido_materno = fields.Char(string="Apellido Materno")
    edad = fields.Integer(string="Edad")
    grado = fields.Selection([
        ('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero')
    ], string="Grado")
    grupo = fields.Char(string="Grupo")
    
    estado = fields.Selection([
        ('aprobado', 'Aprobado'),
        ('no_aprobado', 'No Aprobado')
    ], string="Estado", default='no_aprobado')

    # Relación inversa (opcional pero recomendada)
    partner_id = fields.Many2one('res.partner', string="Contacto Relacionado")