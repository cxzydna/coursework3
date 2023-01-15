import utils

from flask import Flask, render_template, request, redirect
from api_bp.api_bp import api_bp

app = Flask(__name__, static_folder='./static')
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/', methods=['GET'])
def main_page():
    posts = utils.get_posts_all()
    bookmarks_count = utils.get_all_bookmarks()
    count = len(list({post['pk']: post for post in bookmarks_count}.values()))
    return render_template(
        'index.html', posts=posts, bookmarks_count=count
    )


@app.route('/post/<int:post_id>/', methods=['GET'])
def post_page(post_id):
    comments = utils.get_comments_by_post_id(post_id)
    post = utils.get_post_by_comment(post_id)
    new_post = utils.get_posts_with_tags(post)
    counter = len(comments)
    return render_template(
        'post.html', comments=comments, post=new_post, comments_count=counter
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


@app.route('/bookmarks/add/<int:post_id>/', methods=['GET'])
def add_bookmarks(post_id):
    post = utils.get_post_by_pk(post_id)
    utils.add_post_to_bookmarks(post)
    return redirect('/', code=302)


@app.route('/bookmarks/remove/<int:post_id>/', methods=['GET'])
def remove_bookmarks(post_id):
    post = utils.get_post_by_pk(post_id)
    utils.remove_post_from_bookmarks(post)
    return redirect('/', code=302)


@app.route('/bookmarks/', methods=['GET'])
def bookmarks_page():
    bookmarks = utils.get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@app.route('/tag/<tag_name>/')
def tag_page(tag_name):
    posts = utils.search_for_tags('#' + tag_name)
    return render_template('tag.html', posts=posts, tag_name=tag_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_500_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
