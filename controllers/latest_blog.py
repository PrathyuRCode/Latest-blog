from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug


class LatestBlogs(http.Controller):
    @http.route(['/latest_blog'], type="json", auth="public")
    def latest_blog(self):
        blog_list = []
        blogs = request.env['blog.post'].sudo().search([], order='published_date desc')
        for i in blogs:
            blog_list.append([
                i.name, i.id, slug(i), slug(i.blog_id)
            ])
        final_blog = blog_list[0:4]
        return final_blog
