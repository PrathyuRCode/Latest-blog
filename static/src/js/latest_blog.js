odoo.define('latest_blog.blog_template_id', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           var self = this;
           rpc.query({
                route: '/latest_blog',
                params: {},
           }).then(function(result){
           var name=result;
           $('.qweb_blog').append(Qweb.render('latest_blog.latest_blog_template', {name}));
           });
        },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});
