{
    'name': 'Latest Blogs',
    'version': '16.0.1.0.0',
    'summary': 'Latest Blogs',
    'sequence': -12,
    'installable': True,
    'application': True,

    'depends': ['base', 'website'],
    'data': [
        'views/blog_snippet.xml',
        'views/latest_blog.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'latest_blog/static/src/js/latest_blog.js',
            'latest_blog/static/src/xml/latest_blog.xml',
            'latest_blog/static/src/css/latest_blog.scss',
        ]
    },
}
