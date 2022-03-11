# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api



class Facturas(models.Model):
    _inherit = 'account.invoice'

    descuento_nomina = fields.Boolean(string='Descuento Nómina')
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Empleado')    

    
class Nomina(models.Model):
    _inherit = 'hr.payslip'

    @api.one
    def compute_sheet(self):
        contrato_id = self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id), ('state', '=', 'open')])
        fecha_desde=str(self.date_from)
        fecha_hasta = str(self.date_to)
        hastaStr = datetime.strptime(fecha_hasta, '%Y-%m-%d')
        desdeStr = datetime.strptime(fecha_desde, '%Y-%m-%d')
        comision = 0
        domain_facturas = [
                ('state', 'in', ['open','paid']),
                ('date_invoice', '>=', fecha_desde),
                ('date_invoice', '<=', fecha_hasta),
                ('employee_id','=',self.employee_id.id),
                ('type','=','in_invoice'),
                ('sii_code','in',['30','33','34'])
            ]

        invoice=self.env['account.invoice'].search(domain_facturas)
        valor_factura=0
        for i in invoice:
            valor_factura+=i.amount_untaxed

        payslip = self.env['hr.payslip.input'].search([('code', '=', 'ASUE2'),('contract_id','=',contrato_id.id),('payslip_id','=',self.id)])
        payslip.write({'amount': valor_factura})
        return super(Nomina, self).compute_sheet()