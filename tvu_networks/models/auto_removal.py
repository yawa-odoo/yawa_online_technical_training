# -*- coding: utf-8 -*-

from odoo import models
from odoo.fields import Date


class AutoRemoval(models.Model):
    _inherit = 'sale.order'

    def _remove_expired_quotations(self):
        today = Date.today()
        for record in self.search([('state', '=', 'draft')]):
            if record.validity_date and record.validity_date < today:
                record._action_cancel()
