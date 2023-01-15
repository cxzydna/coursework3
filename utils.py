# Importing a library to work with JSON
import json


def get_posts_all():
    """
    The function gets a list with all posts
    :return:   - list of posts
    """
    with open("data/posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
    return posts


def get_all_comments():
    """
    The function gets a list with all the comments
    :return:   - list of comments
    """
    with open("data/comments.json", "r", encoding="utf-8") as f:
        comments = json.load(f)
    return comments


def get_posts_by_user(user_name):
    """
    The function returns a post by username
    :param user_name:  - name of the user
    :return:           - post
    """
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
    """
    The function returns comments by post id
    :param post_id:  - post id
    :return:         - list of comments
    """
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
    """
    The function returns posts by keyword
    :param query:  - keyword
    :return:       - list of posts
    """
    all_posts = get_posts_all()
    result = []

    for post in all_posts:
        if query.lower() in post["content"].lower():
            result.append(post)
    return result if len(result) <= 10 else 'Слишком много постов'


def get_post_by_pk(pk):
    """
    The function returns a post by pk
    :param pk:  - pk
    :return:    - post
    """
    all_posts = get_posts_all()
    for post in all_posts:
        if post["pk"] == pk:
            return post


def get_post_by_comment(post_id):
    """
    The function returns a post by comment
    :param post_id:  - post id
    :return:         - post
    """
    all_posts = get_posts_all()
    for post in all_posts:
        if post_id == post["pk"]:
            return post


def add_post_to_bookmarks(post):
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print(data)
    data.append(post)
    print(data)
    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def remove_post_from_bookmarks(post):
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data.remove(post)
    with open("data/bookmarks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_all_bookmarks():
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def search_for_tags(tag_name):
    posts = get_posts_all()
    result = []
    for post in posts:
        if tag_name in post["content"]:
            result.append(get_posts_with_tags(post))
    return result


def get_posts_with_tags(post):
    # for word in post["content"].split(" "):
    #     if word.startswith('#'):
    #         post["content"] = post["content"].replace(
    #             word, f'<a href="/tag/{word[1:]}">{word}</a>'
    #         )
    #
    result = []
    for word in post["content"].split(" "):
        if word.startswith('#'):
            result.append(f'<a href="/tag/{word[1:]}">{word}</a>')
        else:
            result.append(word)
    post["content"] = " ".join(result)
    return post

# def replace_tag_by_links(posts):
#     final_result = []
#     result = []
#     for post in posts:
#
#         for word in post["content"].split(" "):
#             if word.startswith('#'):
#                 result.append(f'<a href="/tag/{word}">#{word}</a>')
#             else:
#                 result.append(word)
#             post["content"] = " ".join(result)
#         final_result.append(post)
#
#     return final_result
#
#
# def update_json_content_tags():
#     with open("data/posts.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     data = replace_tag_by_links(data)
#     with open("data/posts.json", "w", encoding="utf-8") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
