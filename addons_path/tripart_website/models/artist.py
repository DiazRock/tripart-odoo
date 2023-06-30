# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Artist(models.Model):
    _name = "tripart_website.artist"
    _description = 'Artist person data'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    nationality = fields.Char(string='Nationality')
    biography = fields.Html(string="Biography")
    profile_pic = fields.Image(string = "Profile pic")
    artwork_ids = fields.One2many(
                        'tripart_website.artwork', 
                        'artist_id',
                        string='Pieces of Art')



    