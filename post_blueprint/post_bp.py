from flask import Blueprint, render_template

import utils

post_bp = Blueprint('post_bp', __name__, template_folder='templates')


@post_bp.route('/<int:post_id>', methods=['GET'])
def post_page(post_id):
    comments = utils.get_comments_by_post_id(post_id)
    return render_template('post.html')
