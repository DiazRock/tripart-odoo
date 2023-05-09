# -*- coding: utf-8 -*-
from odoo import http


class TripartWebsite(http.Controller):
    @http.route('/tripart/artists', auth="public", type="json", methods=['POST'])
    def tripart_artists(self, **kw):
        Artist = http.request.env['tripart_website.artist']
        return Artist.search_read([], Artist.fields_get_keys())

    # @http.route('/tripart/artists/<name>', auth='public', website=True)
    # def artist(self, name):
    #     return '<h1>{}</h1>'.format(name)

    @http.route('/tripart/artists/<model("tripart_website.artist"):artist>', auth='public', website=True)
    def artist(self, artist):
        return http.request.render('tripart_website.biography', {
            'person': artist
        })

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
