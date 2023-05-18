from . import models
from . import views
from odoo import api, SUPERUSER_ID

def _setup(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.data'].sudo().create({
        'name': 'view_nxc_lead_qualification_partner_form',
        'module': 'nxc_lead_qualification',
        'res_id': env.ref('nxc_lead_qualification.view_nxc_lead_qualification_partner_form').id,
        'model': 'ir.ui.view',
    })

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.data'].sudo().search([
        ('module', '=', 'nxc_lead_qualification'),
        ('name', '=', 'view_nxc_lead_qualification_partner_form')
    ]).unlink()

def post_init_hook(cr, registry):
    _setup(cr, registry)