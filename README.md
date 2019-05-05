# Suprematerior - Находит победителей конкурсов в Инстаграмме.

Скрипт принимает на вход URL поста в инстаграмме. А на выходе создаёт список пользователей инстаграмма, которые удовлетворяют нескольким критериям:
- пользователь прокомментировал пост, и в комментарии указал другого пользователя;
- поставил лайк этому посту;
- является подписчиком аккаунта.

### Как установить

Для подключения к Инстаграмму необходим рабочий аккаунт физического лица. Аккаунт лучше завести специальный для работы этого скрипта, так как акаунт может быть забаннен.

Название аккаунта и пароль к нему прописываются в файле `.env` например,таким образом:
```
USERNAME=Suprematerior
PASSWORD=dhsjH)J7&Kd
```
Файл .env лежит в той же папке что и скрипт.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Скрипт запускается из терминала и в качестве аргумента передаётся ссылка на нужный пост:
```
python suprematerior.py https://www.instagram.com/p/BtON034lPhu/
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
