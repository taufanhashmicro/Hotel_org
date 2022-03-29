from odoo import http, fields, models
from odoo.http import request
import json


class KamarCon(http.Controller):
    @http.route(['/kamar', '/kamar/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getKamar(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            kamar = request.env['hotel.kamar'].search([])
            for k in kamar:
                value.append({"id": k.id,
                              "tipe_kamar": k.name,
                              "fasilitas": k.fasilitas,
                              "stok_tersedia": k.stok,
                              "harga_sewa": k.harga})
            return json.dumps(value)
        else:
            kamar_id = request.env['hotel.kamar'].search(
                [('id', '=', idnya)])
            for k in kamar_id:
                value.append({"id": k.id,
                              "tipe_kamar": k.name,
                              "fasilitas": k.tipe,
                              "stok_tersedia": k.stok,
                              "harga_sewa": k.harga})
            return json.dumps(value)

    @http.route('/createkamar', auth='user', type='json', methods=['POST'])
    def createKamar(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals = {
                    'name': kw['name'],
                    'fasilitas': kw['fasilitas'],
                    'stok': kw['stok'],
                    'harga': kw['harga'],
                }
                kamarbaru = request.env['hotel.kamar'].create(vals)
                args = {'succeed': True, "ID": kamarbaru.id}
                return args
