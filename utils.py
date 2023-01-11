import json


def get_posts_all():
    with open("data/posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
    return posts


def get_all_comments():
    with open("data/comments.json", "r", encoding="utf-8") as f:
        comments = json.load(f)
    return comments


def get_posts_by_user(user_name):
    all_posts = get_posts_all()
    result = []
    try:
        for post in all_posts:
            if post["poster_name"].lower() == user_name.lower():
                result.append(post)
    except ValueError:
        print('Такого пользователя нет')
    return result


def get_comments_by_post_id(post_id):
    all_comments = get_all_comments()
    result = []
    try:
        for comment in all_comments:
            if comment["post_id"] == post_id:
                result.append(comment)
    except ValueError:
        print('Такого поста нет')
    return result


def search_for_posts(query):
    all_posts = get_posts_all()
    result = []

    for post in all_posts:
        if query.lower() in post["content"].lower():
            result.append(post)
    return result if len(result) <= 10 else []


def get_post_by_pk(pk):
    all_posts = get_posts_all()
    for post in all_posts:
        if post["pk"] == pk:
            return post


def get_post_by_comment(post_id):
    all_posts = get_posts_all()
    for post in all_posts:
        if post_id == post["pk"]:
            return post
