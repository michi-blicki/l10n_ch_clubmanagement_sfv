from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class ClubTeam(models.Model):
    _name = 'club.team'
    _inherit = 'club.team'

    sfv_team_id = fields.Integer(string="SFV Team ID", required=False)