/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.getArtistOptions = options.Class.extend({
    start() {
        let citiesRow = this.$target.find('#tw-artist-row')

        if (citiesRow){
            this._rpc({
                route: '/tripart/artists/',
                params:{}
            }).then(data=>{
                let html = ``
                data.forEach(artist=>{
                    html += `<div class="col-lg-3 mb-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container mr-3 rounded">
                                <img class="country-image rounded" src="data:image/png;base64,${artist.name}"/>
                            </div>
                            <div>
                                <h5 class="mb-0">${artist.name}</h5>
                                <div>${artist.name}</div>
                            </div>
                        </div>
                    </div>`
                })
                citiesRow.html(html)
            })
        }
    },
})

export default {
    getArtistOptions: options.registry.getArtistOptions,
};