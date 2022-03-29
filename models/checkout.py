from odoo import api, fields, models


class Checkout(models.Model):
    _name = 'hotel.checkout'
    _description = 'Checkout Kamar'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    order_id = fields.Many2one('hotel.order', string='Order', domain=[
                               ('sudah_checkout', '=', False)])

    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['hotel.order'].search(
                [('id', '=', record.order_id.id)]).mapped('pemesan').name

    tgl_checkout = fields.Date(string='', default=fields.Date.today())

    tagihan = fields.Integer(compute='_compute_tagihan', string='tagihan')

    orderkamardetails_ids = fields.One2many(
        related='order_id.orderkamardetail_ids', string='Order Kamar Detail')

    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.model
    def create(self, vals):
        record = super(Checkout, self).create(vals)
        if record.tgl_checkout:
            self.env['hotel.order'].search([('id', '=', record.order_id.id)]).write({
                'sudah_checkout': True})
            self.env['hotel.akunting'].create(
                {'kredit': record.tagihan, 'name': record.name})
            for i in record.orderkamardetails_ids:
                self.env['hotel.kamar'].search([('id', '=', i.kamar_id.id)]).write({
                    'stok': i.kamar_id.stok + i.qty})
            return record

    def unlink(self):
        for un in self:
            self.env['hotel.order'].search([('id', '=', un.order_id.id)]).write({
                'sudah_checkout': False})

        record = super(Checkout, self).unlink()
