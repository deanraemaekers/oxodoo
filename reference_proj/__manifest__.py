# -*- coding: utf-8 -*-
{
    'name': "reference_proj",

    'summary': """
        proj_summary_replace
        """,

    'description': """
        proj_description_replace
    """,

    'author': "proj_author_replace",
    'website': "proj_website_replace",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': 'proj_depends_list_replace',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
