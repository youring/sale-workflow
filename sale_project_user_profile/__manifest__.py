# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# Copyright 2017 Tecnativa - Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Project User Profile',
    'version': '10.0.1.0.0',
    'author': 'Camptocamp SA, '
              'Tecnativa, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Project',
    'website': 'https://github.com/OCA/sale-workflow',
    'depends': [
        'hr_timesheet',
        'product',
        'project',
        'sale',
        'sale_timesheet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/project_project.xml',
    ],
    'installable': True,
    'auto_install': False,
}
