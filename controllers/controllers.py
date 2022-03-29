# -*- coding: utf-8 -*-
# from odoo import http


# class HotelOrg(http.Controller):
#     @http.route('/hotel_org/hotel_org/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_org/hotel_org/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_org.listing', {
#             'root': '/hotel_org/hotel_org',
#             'objects': http.request.env['hotel_org.hotel_org'].search([]),
#         })

#     @http.route('/hotel_org/hotel_org/objects/<model("hotel_org.hotel_org"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_org.object', {
#             'object': obj
#         })
