from odoo import api,models,fields
from datetime import datetime

class Minutas(models.Model):
    _name = "dtm.minutas"
    _description = "Modelo para llevar el control de la juntas de Procesos"

    fecha = fields.Date(string="Fecha",default = datetime.today())
    titulo = fields.Char(string="Nombre de la Junta")
    anotaciones = fields.Text(string="Anotaciones")
    asistentes = fields.One2many("dtm.minutas.asistentes","model_id")


    def action_autocomplear(self):
        if not self.asistentes:
            get_self = self.env['dtm.minutas'].search([],order='id DESC', limit=2)
            self.titulo = get_self[1].titulo
            self.anotaciones = get_self[1].anotaciones
            asistentes = get_self[1].asistentes
            for asistente in asistentes:
                vals = {
                    "model_id":self.id,
                    "asistente":asistente.asistente.id,
                    "asistencia":asistente.asistencia,
                    "actividades":asistente.actividades
                }
                self.env['dtm.minutas.asistentes'].create(vals)

class Asistentes(models.Model):
    _name = "dtm.minutas.asistentes"
    _description = "Modelo para llevar la lista de asistentes"

    model_id = fields.Many2one("dtm.minutas")
    asistencia = fields.Boolean(default=True)
    asistente = fields.Many2one("dtm.minutas.nombres",string="Nombre")
    actividades = fields.Text(string="Actividades")


class Nombres(models.Model):
    _name = "dtm.minutas.nombres"
    _description = "Modelo para almacenar los nombres de los participantes"
    _rec_name = "nombre"

    nombre = fields.Char(string="Participante")



