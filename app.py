import utils

from flask import Flask, render_template, request
from api_bp.api_bp import api_bp

app = Flask(__name__, static_folder='./static')
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/', methods=['GET'])
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>/', methods=['GET'])
def post_page(post_id):
    comments = utils.get_comments_by_post_id(post_id)
    post = utils.get_post_by_comment(post_id)
    counter = len(comments)
    return render_template(
        'post.html', comments=comments, post=post, comments_count=counter
    )


@app.route('/search/', methods=['GET'])
def search_post():
    query = request.args.get("s")
    posts = utils.search_for_posts(query)
    posts_count = len(posts)
    return render_template(
        'search.html', posts=posts, posts_count=posts_count, query=query
    )


@app.route('/users/<username>/', methods=['GET'])
def user_page(username):
    posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
