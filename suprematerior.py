from instabot import Bot
import re
import pprint


def get_users_from_comment(comment):
    result = re.findall(r'@([A-Za-z0-9_]+)', comment)

#        if not result:
#            return None
#
    return result


def is_user_exist (username):
    bot = Bot()
    bot.login(username="Suprematerior", password="Vspleskroot44")

    try:
        user_id = bot.get_user_id_from_username(username)
    except JSONDecodeError:
        return False
    return True


def main():
    bot = Bot()
    bot.login(username="Suprematerior", password="Vspleskroot44")
    user_id = bot.get_user_id_from_username("beautybar.rus")

    id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BtON034lPhu/")
    #id_media = bot.get_media_id_from_link("https://www.instagram.com/p/Bwu6M2pgRuZ/")
    #id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BvMQ7rSAhK0/")

    all_comments = bot.get_media_comments_all(id_media)

    list_of_users = []
    list_of_likers = bot.get_media_likers(id_media)
    list_of_followers = bot.get_user_followers(user_id)

    for comment in all_comments:
        if get_users_from_comment(comment['text']) is not None \
        and list_of_likers.count(str(comment['user_id'])) \
        and list_of_followers.count(str(comment['user_id'])):
            list_of_users.append((comment['user_id'], comment['user']['username']))

    #print(f'list_of_user = {len(list_of_users)}')
    #print(f'list_of_likers = {len(list_of_likers)}')
    #print(f'list_of_followers = {len(list_of_followers)}')
    #print(f'action_users = {len(list(set(list_of_users)))}')

    action_users = list(set(list_of_users))

    for user in action_users:
        print (user[1])
    #pprint.pprint()


if __name__ == '__main__':
    main()
