# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    # in prevous version, column doesn't exist

    # create column
    cr.execute("ALTER TABLE ir_config_parameter ADD COLUMN value VARCHAR")

    # fill column
    env = api.Environment(cr, SUPERUSER_ID, {})

    field_id = env.ref('base.field_ir_config_parameter_value').id
    default_values = env['ir.property'].search([
        ('fields_id', '=', field_id),
        ('company_id', '=', False)
    ])

    default_values._update_config_parameter_value()
