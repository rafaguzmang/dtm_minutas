from odoo import api,models,fields
from datetime import datetime

class Minutas(models.Model):
    _name = "dtm.minutas"
    _description = "Modelo para llevar el control de la juntas de Procesos"

    fecha = fields.Date(string="Fecha",default = datetime.today())
    anataciones = fields.Text(string="Anotaciones")
    asistentes = fields.One2many("dtm.minutas.asistentes","model_id")

    @api.model
    def get_view(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(Minutas, self).get_view(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

        # get_self = self.env[''].search([],)

        return res


class Asistentes(models.Model):
    _name = "dtm.minutas.asistentes"
    _description = "Modelo para llevar la lista de asistentes"

    model_id = fields.Many2one("dtm.minutas")
    asistente = fields.Many2one("dtm.minutas.nombres",string="Nombre")
    actividades = fields.Text(string="Actividades")


class Nombres(models.Model):
    _name = "dtm.minutas.nombres"
    _description = "Modelo para almacenar los nombres de los participantes"
    _rec_name = "nombre"

    nombre = fields.Char(string="Participante")



