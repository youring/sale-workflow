# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains(
        'state',
        'order_line',
    )
    def _check_state(self):
        for order in self:
            if order.state != 'sale':
                continue
            service_products = order.order_line.mapped('product_id').filtered(
                lambda p: p.type == 'service')
            # Check if all service products has the same user_profile value
            user_profile = service_products[:1].user_profile
            if service_products.filtered(
                    lambda p: p.user_profile != user_profile):
                raise ValidationError(_(
                    "With a service product of type 'User profile', "
                    "all service products must have 'User profile' type."
                ))

    @api.constrains('order_line')
    def _check_multi_timesheet(self):
        """Don't make this check for orders with "user_profile" lines"""
        orders = self.filtered(lambda x: not any(
            l.product_id.user_profile for l in x.order_line))
        return super(SaleOrder, orders)._check_multi_timesheet()

    @api.multi
    def action_confirm(self):
        """Pass the default field value only for sales orders with
        "user_profile" lines.
        """
        user_profile_orders = self.filtered(
            lambda x: any(l.product_id.user_profile for l in x.order_line)
        ).with_context(
            default_project_uses_task_sale_line_map=True
        )
        if user_profile_orders:  # needed because self.ensure_one()
            super(SaleOrder, user_profile_orders).action_confirm()
        rest_orders = self - user_profile_orders
        if rest_orders:  # needed because self.ensure_one()
            return super(SaleOrder, rest_orders).action_confirm()
