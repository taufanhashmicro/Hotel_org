from odoo import api, fields, models


class Kamar(models.Model):
    _name = 'hotel.kamar'
    _description = 'New Description'

    name = fields.Char(string='Tipe Kamar', required=True)
    fasilitas = fields.Char(string='Fasilitas Kamar')
    harga = fields.Integer(compute='_compute_harga', string='Harga Kamar')
    stok = fields.Integer(string='Stok Kamar')

    fasilitas_ids = fields.Many2many(
        comodel_name='hotel.fasilitas', string='Fasilitas')

    kasur_ids = fields.Many2one('hotel.kasur', string='Tipe Kasur')

    @api.depends('fasilitas_ids', 'kasur_ids')
    def _compute_harga(self):
        for record in self:
            # a = sum(self.env['hotel.fasilitas'].search(
            #     [('id', '=', record.fasilitas_ids.id)]).mapped('harga'))
            a = sum(record.fasilitas_ids.mapped('harga'))
            record.harga = a + record.kasur_ids.harga


class Fasilitas(models.Model):
    _name = 'hotel.fasilitas'
    _description = 'New Description'

    name = fields.Char(string='Nama Fasilitas')
    harga = fields.Integer(string='Harga Fasilitas')
    deskripsi = fields.Char(string='Deskirpsi Fasilitas')

    kamar_ids = fields.Many2many('hotel.kamar', string='Kamar')
