from odoo import api, fields, models

class Lead(models.Model):
    _inherit = 'crm.lead'
    
    #MQL Score Items
    mql_priority = fields.Selection([
        ('0','MQL 10 or Below'),
        ('1','MQL 11-15'),
        ('2','MQL 16-20'),
        ('3','MQL 21-25'),
    ], string="MQL Priority")

    @api.model
    def default_get(self, fields_list):
        res = super(Lead, self).default_get(fields_list)
        stage_id = self.env.context.get('default_stage_id')
        if stage_id == '1':
            res['order'] = 'mql_priority desc, id desc'
        return res

    @api.onchange('partner_id', 'partner_id.mql_score')
    def _compute_mql_priority(self):
        # Calculate the MQL Priority based on the value of MQL Score field from partner.
        for lead in self:
            if lead.partner_id.mql_score < 11:
                lead['mql_priority'] = '0'
            elif 11 <= lead.partner_id.mql_score <= 15:
                lead['mql_priority'] = '1'
            elif 16 <= lead.partner_id.mql_score <= 20:
                lead['mql_priority'] = '2'
            elif 21 <= lead.partner_id.mql_score <= 25:
                lead['mql_priority'] = '3'