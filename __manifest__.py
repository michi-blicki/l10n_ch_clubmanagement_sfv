# -*- coding: utf-8 -*-
{
    'name': "l10n_ch_clubmanagement_sfv",

    'summary': "Clubmanagement: Swiss Football Association",

    'description': """
This is a small Addon for Football Clubs within the Swiss Football Association.
This Addon enhances the clubmanagement suite, available at https://github.com/michi-blicki/Odoo_Clubmanagement.git.
Please note, that the Addon l10n_ch_clubmanagement is required, too.
    """,

    #
    # Issuer Specification
    'author': "Michael Blickenstorfer",
    'website': "https://www.blicki.ch",
    'license': "AGPL-3",
    #'price': 30.00,
    #'currency': "CHF",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Association',
    'version': '18.0.0.4.0',
    'application': False,
    'auto_install': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'clubmanagement',
        'l10n_ch_clubmanagement'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/club_20_view_member_form.xml',
        'views/club_50_view_team.xml',
        'views/club_80_view_club.xml',
        'views/club_80_view_sfv_trainer_diploma.xml',
        'data/sfv_trainer_diploma.xml',
    ],

    'assets': {

    },

    'translation_files': [

    ],

    # only loaded in demonstration mode
    'demo': [
        
    ],

    #
    # Hooks
    'pre_init_hook': '_pre_init_hook',
    'post_init_hook': '_post_init_hook',
    'uninstall_hook': '_uninstall_hook',

}

