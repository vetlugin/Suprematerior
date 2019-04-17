from instabot import Bot
import re


def get_users_from_comment(comment):
        result = re.findall(r'@([A-Za-z0-9_]+)', comment)
        return result


def is_user_exist (username):
    bot = Bot()
    bot.login(username="Suprematerior", password="Vspleskroot44")

    try:
        user_id = bot.get_user_id_from_username(username)
    except JSONDecodeError:
        return

    return user_id

def main():
    bot = Bot()
    bot.login(username="Suprematerior", password="Vspleskroot44")
    user_id = bot.get_user_id_from_username("beautybar.rus")
    #user_id = bot.get_user_id_from_username("spherasveta")
    user_info = bot.get_user_info(user_id)
    #print(user_info['biography'])

    id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BtON034lPhu/")
    #id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BvMQ7rSAhK0/")

    #all_comments = bot.get_media_comments_all(id_media)

    print(is_user_exist('lkspherasveta'))
#    for item in range(len(all_comments)):
#        print(get_users_from_comment(all_comments[item]['text']))


if __name__ == '__main__':
    main()
