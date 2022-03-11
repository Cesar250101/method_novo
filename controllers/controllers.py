# -*- coding: utf-8 -*-
from odoo import http

# class MethodNovo(http.Controller):
#     @http.route('/method_novo/method_novo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_novo/method_novo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_novo.listing', {
#             'root': '/method_novo/method_novo',
#             'objects': http.request.env['method_novo.method_novo'].search([]),
#         })

#     @http.route('/method_novo/method_novo/objects/<model("method_novo.method_novo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_novo.object', {
#             'object': obj
#         })