import utils
import logging
from flask import Blueprint, jsonify

api_bp = Blueprint("api_bp", __name__)

api_logger = logging.getLogger()

api_file_handler = logging.FileHandler("./logs/log.log")

formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")

api_file_handler.setFormatter(formatter)

api_logger.setLevel(logging.INFO)
api_logger.addHandler(api_file_handler)


@api_bp.route('/posts/', methods=['GET'])
def api_posts():
    result = utils.get_posts_all()
    api_logger.info('/api/posts')
    return jsonify(result)


@api_bp.route('/posts/<int:post_id>/', methods=['GET'])
def api_post(post_id):
    result = utils.get_post_by_pk(post_id)
    api_logger.info(f'/api/posts/{post_id}')
    return jsonify(result)
