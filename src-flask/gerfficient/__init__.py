from flask import Flask, render_template

def make_app(secret_key: str) -> Flask:
    app = Flask(__name__)

    app.secret_key = secret_key

    @app.route('/posts/')
    def get_post_list() -> str:
        return render_template('posts/list.jinja2')
    
    @app.route('/posts/sample')
    def get_post() -> str:
        return render_template('posts/single.jinja2')

    return app
