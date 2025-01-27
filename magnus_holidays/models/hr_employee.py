# -*- coding: utf-8 -*-
# Copyright 2018 Magnus ((www.magnus.nl).)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    current_leave_state = fields.Selection(selection_add=[('written', 'Written')])

    # @api.multi
    # def _compute_leaves_count(self):
    #     leaves = self.env['hr.leave'].read_group([
    #         ('employee_id', 'in', self.ids),
    #         ('holiday_status_id.limit', '=', False),
    #         ('state', '!=', 'refuse')],
    #         fields=['number_of_hours_display', 'employee_id'],
    #         groupby=['employee_id']
    #     )
    #     mapping = dict(
    #         [(leave['employee_id'][0], leave['number_of_hours_display'])
    #          for leave in leaves]
    #     )
    #     for employee in self:
    #         employee.leaves_count = mapping.get(employee.id)

    # there is a standard function, commented below is a copy of same code in hr_holidays
    # @api.multi
    # def _compute_leaves_count(self):
    #     all_leaves = self.env['hr.leave.report'].read_group([
    #         ('employee_id', 'in', self.ids),
    #         ('holiday_status_id.allocation_type', '!=', 'no'),
    #         ('holiday_status_id.active', '=', 'True'),
    #         ('state', '=', 'validate')
    #     ], fields=['number_of_days', 'employee_id'], groupby=['employee_id'])
    #     mapping = dict([(leave['employee_id'][0], leave['number_of_days']) for leave in all_leaves])
    #     for employee in self:
    #         employee.leaves_count = float_round(mapping.get(employee.id, 0), precision_digits=2)