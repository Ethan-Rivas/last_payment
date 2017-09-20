# -*- coding: utf-8 -*-
from openerp import api
from openerp.osv import fields, osv

class account_invoice(osv.osv):
    _inherit = "account.invoice"

    def action_ver_pagos(self, cr, uid, ids, context=None):
        factura = self.browse(cr, uid, ids[0])

        # Codigo para obtener los ids de los pagos (account.move.line)
        pagos = []

        for pago in factura.move_lines:
            pagos.append(pago.id)

        return {
            'name': 'Testing',
            'res_model': 'account.move.line',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'list,form',
            'domain': [('id', 'in', pagos)]
        }

    @api.depends('payment_ids')
    def _get_ultimo_pago(self):
        '''for rec in self:
            rec.last_payment_date = # Codigo'''

    _columns = {
        'last_payment_date': fields.text(compute='_get_ultimo_pago', string="Fecha de ultimo pago")
    }
