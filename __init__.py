# -*- coding: utf-8 -*-

from . import controllers
from . import models

def _pre_init_hook(env):
    _logger.info(f"_pre_init_hook(): Start")
    _logger.info(f"_pre_init_hook(): End")

def _post_init_hook(env):
    _logger.info(f"_post_init_hook(): Start")
    _logger.info(f"_post_init_hook(): End")

def _uninstall_hook(env):
    _logger.info(f"_uninstall_hook(): Start")
    _logger.info(f"_uninstall_hook(): End")