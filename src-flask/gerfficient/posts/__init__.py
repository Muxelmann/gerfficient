from flask import Flask, Blueprint, render_template, request, abort
from .post import Post

def init(app: Flask) -> Blueprint:

    bp = Blueprint('posts', __name__, url_prefix='/posts/')

    @bp.route('/')
    def index() -> str:
        return render_template('posts/list.jinja2')
    
    @bp.route('/test')
    def get_sample() -> str:

        if request.args.get('sample') is not None:
            post = Post.lorem()
            return render_template('posts/single.jinja2', post=post)
        
        return abort(404)
    
    @bp.route('/?id=<post_id>')
    def get_post(post_id: str) -> str:

        post = Post.get_post_with_id(post_id)

        return render_template('posts/single.jinja2', post=post)

    app.register_blueprint(bp)
    return bp