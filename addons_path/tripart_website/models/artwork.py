from odoo import models, fields

class PieceOfArt(models.Model):
    _name = 'tripart_website.artwork'
    _description = 'Piece of artwork data'

    name = fields.Char(string='Name', required=True)
    date_created = fields.Date(string='Creation Date')
    artist_id = fields.Many2one('tripart_website.artist', string='Artist')
    artwork_image = fields.Image(string = "Artwork Image")
    description = fields.Text(string= "Artwork description", default="Lorem ipsum qui a dolor sit amet")
