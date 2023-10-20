from flask import Flask, Blueprint, render_template, request, abort
from .post import Post

def make_bp(app: Flask, posts_dir: str = '/home/posts') -> Blueprint:

    Post.posts_dir = posts_dir

    bp = Blueprint('posts', __name__, url_prefix='/posts/')

    @bp.route('/')
    def index() -> str:
        if request.args.get('sample-post') is not None:
            post = Post.lorem()
            return render_template('posts/single.jinja2', post=post)
        
        return render_template('posts/list.jinja2')
    
    @bp.route('/<post_id>')
    @bp.route('/<post_id>/')
    def get_post(post_id: str) -> str:

        post = Post.get_post_with_id(post_id)
        if post is None:
            return abort(404)

        return render_template('posts/single.jinja2', post=post)

    app.register_blueprint(bp)
    return bp