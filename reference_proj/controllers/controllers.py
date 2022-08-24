# -*- coding: utf-8 -*-
# from odoo import http


# class ReferenceProj(http.Controller):
#     @http.route('/reference_proj/reference_proj', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reference_proj/reference_proj/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reference_proj.listing', {
#             'root': '/reference_proj/reference_proj',
#             'objects': http.request.env['reference_proj.reference_proj'].search([]),
#         })

#     @http.route('/reference_proj/reference_proj/objects/<model("reference_proj.reference_proj"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reference_proj.object', {
#             'object': obj
#         })
