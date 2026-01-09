from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class SFVTrainerDiploma(models.Model):
    _name = 'sfv.trainer.diploma'
    _description = 'SFV Trainer Diploma'
    _order = 'category, sequence ASC, name'

    name        = fields.Char(string="Diploma Name", required=True)
    alt_names   = fields.Char(string="Alternative Diploma Names", required=False)
    code        = fields.Char(string="Internal Code", required=True)
    category    = fields.Selection([
                    ('adult', 'Adult- and Youth'),
                    ('child', 'Child'),
                    ('goal', 'Goal-Keeper'),
                    ('athletic', 'Athletic'),
                    ('futsal', 'Futsal')
                ])
    sequence    = fields.Integer(default=10)
    active      = fields.Boolean(default=True)

