# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    _sql_constraints = [
        ('name_company_uniq', 'unique (name,company_id)',
         _('The name of the Lot/Serial number must be unique per company !'))
    ]
