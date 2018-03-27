# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    # in prevous version, column doesn't exist. We must create it, because it
    # will be renamed to value_tmp during updating the module

    # Create Column
    cr.execute("ALTER TABLE ir_config_parameter ADD COLUMN value VARCHAR")
