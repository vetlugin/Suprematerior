from instabot import Bot


bot = Bot()
bot.login(username="Suprematerior", password="Vspleskroot44")
user_id = bot.get_user_id_from_username("beautybar.rus")
#user_id = bot.get_user_id_from_username("spherasveta")
user_info = bot.get_user_info(user_id)
#print(user_info['biography'])

id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BtON034lPhu/")
#id_media = bot.get_media_id_from_link("https://www.instagram.com/p/BvMQ7rSAhK0/")
print(id_media)

all_comments = bot.get_media_comments_all(id_media)
for item in range(len(all_comments)):
    print(all_comments[item]['text'])
