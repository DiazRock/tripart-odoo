/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.getArtist = publicWidget.Widget.extend({
    selector: '.get-artist',
    start() {
        let artistRow = this.el.querySelector('#tw-artist-row')
        if (artistRow){
            this._rpc({
                route: '/tripart/artists/',
                params:{}
            }).then(data=>{
                let html = `<div class="col-lg-12 s_media_list_item pt16 pb16" data-name="Media item"><div class="row s_nb_column_fixed s_col_no_bgcolor">`
                data.forEach((artist, index)=>{
                    html += `<div class="col-lg-12 s_media_list_item pt16 pb16">
                        <div class="row s_col_no_resize s_col_no_bgcolor align-items-center ${index %2 === 0? 'flex-row-reverse':''} o_colored_level">
                            <div class="align-self-stretch s_media_list_img_wrapper col-lg-6">
                                <img class="s_media_list_img h-100 w-100" src="data:image/png;base64,${artist.profile_pic}"/>
                            </div>
                            <div class="s_media_list_body col-lg-6">
                                <h3 class="o_default_snippet_text">${artist.name}</h3>
                                <p class="o_default_snippet_text">${artist.biography}</p>
                                <a href="#" class="btn btn-primary mb-2 o_default_snippet_text">Discover</a>
                            </div>
                        </div>
                    </div>`
                })
                html += `</div></div>`
                artistRow.innerHTML = html
            }).catch(err => console.log(err))
        }
    },
});

export default publicWidget.registry.getArtist;