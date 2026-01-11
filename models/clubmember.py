from odoo import models, fields, api, _
from odoo.exceptions import AccessError, ValidationError, UserError

class ClubMember(models.Model):
    _name = 'club.member'
    _inherit = 'club.member'

    sfv_license             = fields.Integer(string="SFV License", required=False)
    sfv_qualified_from      = fields.Date(string="SFV Qualified From", required=False)
    sfv_qualified_until     = fields.Date(string="SFV Qualified Until", required=False)
    sfv_request_submit_date = fields.Date(string="SFV Request Submit Date", required=False)
    sfv_valid_license       = fields.Boolean(string="SFV Valid License", readonly=True, compute="_compute_sfv_valid_license", required=True, default=False)

    sfv_trainer_diploma_ids = fields.One2many(string="SFV Trainer Diplomas", comodel_name='club.member.trainer.diploma', inverse_name='member_id', required=False)

    @api.depends('sfv_qualified_from', 'sfv_qualified_until')
    def _compute_sfv_valid_license(self):
        for member in self:
            if member.sfv_license:
                sfv_valid_license = False
                today = fields.Date.today()
                if member.sfv_qualified_from:
                    if member.sfv_qualified_from < today:
                        sfv_valid_license = True
                if member.sfv_qualified_until:
                    if today < member.sfv_qualified_until:
                        sfv_valid_license = True
                if not member.sfv_qualified_from and not member.sfv_qualified_until:
                    sfv_valid_license = True
            else:
                sfv_valid_license = True

            member.sfv_valid_license = sfv_valid_license
