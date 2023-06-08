from odoo import api, fields, models

class Lead(models.Model):
    _inherit = 'crm.lead'

    _order = "mql_priority desc, priority desc, id desc"
    
    #MQL Score Items
    mql_priority = fields.Selection([
        ('0','MQL 10 or Below'),
        ('1','MQL 11-15'),
        ('2','MQL 16-20'),
        ('3','MQL 21-25'),
    ], string="MQL Priority")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        stage_id = self.env.context.get('default_stage_id')
        if stage_id == '1':
            if not order or 'mql_priority' not in order:
                order = 'mql_priority desc, ' + self._order if self._order else 'mql_priority desc'
        return super(Lead, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.onchange('stage_id', 'partner_id', 'partner_id.mql_score')
    def _compute_mql_priority(self):
        # Calculate the MQL Priority based on the value of MQL Score field from partner.
        for lead in self:
            if lead.stage_id == '1':
                if lead.partner_id.mql_score < 11:
                    lead['mql_priority'] = '0'
                elif 11 <= lead.partner_id.mql_score <= 15:
                    lead['mql_priority'] = '1'
                elif 16 <= lead.partner_id.mql_score <= 20:
                    lead['mql_priority'] = '2'
                elif 21 <= lead.partner_id.mql_score <= 25:
                    lead['mql_priority'] = '3'
            else:
                lead['mql_priority'] = False