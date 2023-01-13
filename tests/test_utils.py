import json

import utils
import pytest


def test_get_posts_all():
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        result = json.load(file)
    assert utils.get_posts_all() == result, 'Ошибка джейсончика для постов(('


def test_get_all_comments():
    with open('./data/comments.json', 'r', encoding='utf-8') as file:
        result = json.load(file)
    assert utils.get_all_comments() == result, 'Ошибка для комментов(('


def test_get_posts_by_user_true():
    assert utils.get_posts_by_user('leo') != [], 'Не находит пользователя'


def test_get_posts_by_user_false():
    assert utils.get_posts_by_user('asdas') == [], \
        'ошибка несуществующего юзера'


def test_get_comments_by_post_id_true():
    assert utils.get_comments_by_post_id(1) != [], 'Не находит комменты'


def test_get_comments_by_post_id_false():
    assert utils.get_comments_by_post_id(1000) == [], \
        'Ошибка несуществующего коммента'


def test_search_for_posts_true():
    assert utils.search_for_posts('ага') != [], 'Не находит пост по слову'


def test_search_for_posts_false():
    assert utils.search_for_posts('asd') == [], \
        'Ошибка с несуществующим словом'


def test_get_post_by_pk_true():
    assert utils.get_post_by_pk(1) is not None, 'Не находит пост по pk'


def test_get_post_by_pk_false():
    assert utils.get_post_by_pk(100000) is None, \
        'ошибка с несуществующим постом'


def test_get_post_by_comment_true():
    assert utils.get_post_by_comment(1) is not None, \
        'Не находит пост по комменту'


def test_get_post_by_comment_false():
    assert utils.get_post_by_comment(10000) is None, \
        'ошибка с несуществующим постом'
