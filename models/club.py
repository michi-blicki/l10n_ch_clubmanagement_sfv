from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, date, timedelta

import logging
_logger = logging.getLogger(__name__)

class Club(models.Model):
    _name = 'club.club'
    _inherit = 'club.club'

    sfv_club_id = fields.Integer(string="SFV Club ID", required=False)