import os
import re
import argparse
from instabot import Bot
from dotenv import load_dotenv


def get_users_from_comment(comment):
    '''Get username from comment.'''
    return re.findall(r'@([A-Za-z0-9_]+)', comment)


def main():
    parser = argparse.ArgumentParser(description='Script can spot the winner of competition.')
    parser.add_argument('instauser', help='Name of instagram user who estableshed competition')
    parser.add_argument('name', help='URL of instagram post for finding the winner of competition.')
    args = parser.parse_args()

    bot = Bot()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    bot.login(username=username, password=password)

    instagram_post_url = args.name
    id_media = bot.get_media_id_from_link(f'{instagram_post_url}')

    instagram_user = args.instauser
    user_id = bot.get_user_id_from_username(f'{instagram_user}')

    all_comments = bot.get_media_comments_all(id_media)

    list_of_users = []
    list_of_likers = bot.get_media_likers(id_media)
    list_of_followers = bot.get_user_followers(user_id)

    #Conditions of competition checking
    for comment in all_comments:
        if get_users_from_comment(comment['text']) is not None \
        and list_of_likers.count(str(comment['user_id'])) \
        and list_of_followers.count(str(comment['user_id'])):
            list_of_users.append((comment['user_id'], comment['user']['username']))

    #Users who fulfilled all conditions
    action_users = list(set(list_of_users))
    #Existence users checking
    competition_users = [user[1] for user in action_users if bot.get_user_id_from_username(user[1])]

    print(f'____ В конкурсе участвуют: {len(competition_users)} чел. ____')
    for user in competition_users:
        print (user)


if __name__ == '__main__':
    load_dotenv()
    main()
