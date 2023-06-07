from odoo import api, fields, models

class NxcMqlPriorityOpportunity(models.Model):
    _inherit = 'crm.lead'
    
    #MQL Score Items
    mql_priority = fields.Selection([
        ('0','MQL 10 or Below'),
        ('1','MQL 11-15'),
        ('2','MQL 16-20'),
        ('3','MQL 21-25'),
    ], string="MQL Priority")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if count or not order or 'my_activity_date_deadline' not in order:
            return super(Lead, self).search(args, offset=offset, limit=limit, order=order, count=count)
        order_items = [order_item.strip().lower() for order_item in (order or self._order).split(',')]

        # Fill with remaining leads. If a limit is given, simply remove count of
        # already fetched. Otherwise keep none. If an offset is set we have to
        # reduce it by already fetched results hereabove. Order is updated to exclude
        # my_activity_date_deadline when calling super().

        lead_limit = (limit - len(my_lead_ids_keep)) if limit else None
        if offset:
            lead_offset = max((offset - len(search_res), 0))
        else:
            lead_offset = 0

        # Modify the order based on stage_id value
        stage_id = self.env.context.get('default_stage_id')
        if stage_id == '1':
            lead_order = ', '.join(item if 'priority' not in item else 'mql_priority desc' for item in order_items)
        else:
            lead_order = ', '.join(item for item in order_items if 'my_activity_date_deadline' not in item)

        other_lead_res = super(Lead, self).search(
            expression.AND([[('id', 'not in', my_lead_ids_skip)], args]),
            offset=lead_offset, limit=lead_limit, order=lead_order, count=count
        )
        return self.browse(my_lead_ids_keep) + other_lead_res

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