from odoo import api, fields, models


class Kasur(models.Model):
    _name = 'hotel.kasur'
    _description = 'New Description'

    name = fields.Char(string='Tipe Kasur', required=True)
    harga = fields.Integer(string='Harga Kasur')
    deskripsi = fields.Char(string='Deskripsi Kasur')
