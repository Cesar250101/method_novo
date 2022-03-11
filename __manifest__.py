# -*- coding: utf-8 -*-
{
    'name': "method_novo",

    'summary': """
        1.- Rescata facturas marcadas como descuento en liquidación de trabajdores
            para aquellas compras a nombre del trabajador 
        2.- 
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Method ERP",
    'website': "https://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_cl_hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/l10n_cl_hr_method_payroll_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}