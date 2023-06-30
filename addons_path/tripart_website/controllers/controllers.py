# -*- coding: utf-8 -*-
from odoo import http
import json

class TripartWebsite(http.Controller):
    @http.route('/tripart/artists', auth="public", type="json", methods=['POST'])
    def tripart_artists(self, **kw):
        Artist = http.request.env['tripart_website.artist']
        return Artist.search_read([], Artist.fields_get_keys())

    @http.route('/tripart/artist-detail-and-work',
                auth='public',
                type="json",
                methods=['POST'])
    def artist_detail_and_work(self, **kw):
        Artist = http.request.env['tripart_website.artist']
        Artwork = http.request.env['tripart_website.artwork']
        response = Artist.search_read([kw['artist_id']], Artist.fields_get_keys())
        response['artwork_ids'] = Artwork.search_and_read([artwork_id for artwork_id in response['artwork_ids']], Artwork.fields_fields())
        return json.dumps(response) 

    @http.route('/tripart/artists/<model("tripart_website.artist"):artist>',
                auth='public', website=True)
    def artist(self, artist):
        Artist = http.request.env['tripart_website.artist']
        Artwork = http.request.env['tripart_website.artwork']
        response = Artist.search_read(artist, Artist.fields_get_keys())
        response['artwork_ids'] = Artwork.search_and_read(
                                [artwork_id for artwork_id in response['artwork_ids']],
                                Artwork.fields_fields())
        return json.dumps(response)

    @http.route('/tripart_website/tripart_website/objects', auth='public')
    def list(self, **kw):
        return http.request.render('tripart_website.listing', {
            'root': '/tripart_website/tripart_website',
            'objects': http.request.env['tripart_website.tripart_website'].search([]),
        })

    @http.route('/tripart_website/tripart_website/objects/<model("tripart_website.tripart_website"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tripart_website.object', {
            'object': obj
        })
