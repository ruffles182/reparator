# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Repair(models.Model):
    _inherit = 'repair.order'

    employee_reparador = fields.Many2one('hr.employee', 'Reparador')
    entregado_estatus = fields.Boolean(string='Entregado')
    imei = fields.Char('Imei', size=15)
    fecha_reparado = fields.Date('Fecha Reparado')
    fecha_recibido = fields.Date('Fecha Recibido', default=fields.Date.today())

    @api.onchange('entregado_estatus')
    def _onchange_entregado_estatus(self):
        if self.entregado_estatus == True:
            self.fecha_reparado = fields.Date.today()
        elif self.entregado_estatus == False:
            self.fecha_reparado = ""
