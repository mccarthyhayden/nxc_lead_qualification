from odoo import api, fields, models

class NxcLeadQualificationPartner(models.Model):
    _inherit = 'res.partner'
    
    #MQL Score Items
    company_size_score = fields.Integer(string="Company Size")
    market_position_score = fields.Integer(string="Market Position")
    problems_we_solve_score = fields.Integer(string="Problems We Solve")
    growth_factor_score = fields.Integer(string="Growth Factor")
    core_value_alignment_score = fields.Integer(string="Core Value Alignment")
    mql_score = fields.Integer(string="MQL Score")

    #Other MQL Items
    mql_criteria_1 = fields.Text(string="Compelling Reason to Buy")
    mql_criteria_2 = fields.Text(string="Value Proposition")
    mql_criteria_3 = fields.Text(string="Key Contacts")
    mql_criteria_4 = fields.Text(string="Next Actions")

    #SQL Items
    sql_criteria_1 = fields.Text(string="Key Relationships to Build")
    sql_criteria_2 = fields.Text(string="Verify Buying Process")
    sql_criteria_3 = fields.Text(string="Customer Needs")
    sql_criteria_4 = fields.Text(string="Comparative Advantage")
    sql_criteria_5 = fields.Text(string="Competition")
    sql_criteria_6 = fields.Text(string="Shared Core Values")
    sql_criteria_7 = fields.Text(string="Target Locations")
    sql_criteria_8 = fields.Text(string="Specific Projects/$$$/Dates")
    sql_criteria_9 = fields.Text(string="Confirmation of Value Proposition")