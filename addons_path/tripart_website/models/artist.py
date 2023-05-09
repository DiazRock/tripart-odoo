# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Artist(models.Model):
    _name = "tripart_website.artist"

    name = fields.Char()
    biography = fields.Html()
    profile_pic = fields.Image(string = "Profile pic")


    