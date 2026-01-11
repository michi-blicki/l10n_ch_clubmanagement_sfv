from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

from datetime import date

class ClubMemberTrainerDiploma(models.Model):
    _name = 'club.member.trainer.diploma'
    _description = 'Trainer Diplomas held by Club Member'
    _order = 'diploma_id, acquisition_date'

    member_id = fields.Many2one(string="Member", comodel_name="club.member", required=True, ondelete="cascade")
    diploma_id = fields.Many2one(string="Diploma", comodel_name="sfv.trainer.diploma", required=True)
    acquisition_date = fields.Date(string="Acquisition Date")
    last_refresh_date = fields.Date(string="Last Refresh Date")
    expiry_date = fields.Date(string="Expiration Date", compute="_compute_expiry_date", store=True, readonly=True)
    remarks = fields.Text(string="Notes")

    valid = fields.Boolean(string="Valid", compute="_compute_valid", store=True, readonly=True)

    @api.depends("acquisition_date", "last_refresh_date")
    def _compute_expiry_date(self):
        for diploma in self:
            base_date = diploma.last_refresh_date or diploma.acquisition_date
            if not base_date:
                diploma.expiry_date = False
                continue

            year_plus_two = base_date.year + 2
            diploma.expiry_date = date(year_plus_two, 12, 31)

    @api.depends('expiry_date')
    def _compute_valid(self):
        today = fields.Date.today()
        for diploma in self:
            diploma.valid = bool(diploma.expiry_date and diploma.expiry_date >= today)