from email.policy import default
import string
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'hotel.order'
    _description = 'New Description'

    orderkamardetail_ids = fields.One2many('hotel.kamardetail',
                                           inverse_name='order_id',
                                           string='Order Detail')

    name = fields.Char(string='Kode Order')
    total = fields.Integer(compute='_compute_total', string='Total Harga')

    @api.depends('orderkamardetail_ids')
    def _compute_total(self):
        for record in self:
            record.total = record.orderkamardetail_ids.harga

    tanggal_booking = fields.Datetime(
        'Tanggal Booking', default=fields.Datetime.now())
    tanggal_checkout = fields.Date(
        'Tanggal Checkout', default=fields.Date.today())

    pemesan = fields.Many2one('res.partner', string='Pemesan', domain=[
                              ('is_customer', '=', True)])

    sudah_checkout = fields.Boolean(
        string='Sudah Checkout', default=False)


class OrderKamarDetail(models.Model):
    _name = 'hotel.kamardetail'
    _description = 'New Description'

    order_id = fields.Many2one('hotel.order', string='Order')

    kamar_id = fields.Many2one('hotel.kamar', string='Kamar')

    name = fields.Char(string='Kode Order')

    harga = fields.Integer(compute='_compute_harga', string='Harga')

    qty = fields.Integer(string='Quantity')

    @api.depends('qty', 'harga')
    def _compute_harga(self):
        for record in self:
            record.harga = record.kamar_id.harga * record.qty

    @api.model
    def create(self, vals):
        record = super(OrderKamarDetail, self).create(vals)
        if record.qty:
            self.env['hotel.kamar'].search(
                [('id', '=', record.kamar_id.id)]).write({'stok': record.kamar_id.stok-record.qty})
            return record
