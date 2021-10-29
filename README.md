### Up environment
.\venv\Scripts\activate

# Installing
* **Environment variables:** pip install python-dotenv

### Install custom package version
pip install "flask<2"
### Set environment variables
set FLASK_APP=microblog.py
### Run initial migration 
flask db init
### create and apply migration
`flask db migrate -m "users table"`
 -m: command to add some description or verboese to migration
NEXT: `flask db upgrade` -> to apply migration
 `You will find that it has two functions called upgrade() and downgrade(). The upgrade() function applies the migration, and the downgrade() function removes it. `
### Apply migration
flask db upgrade

## Config email server 
### Add enviroments

set MAIL_PORT=8025
set MAIL_SERVER=localhost

### Run email server in another terminal
python -m smtpd -n -c DebuggingServer localhost:8025

## Translate 
1. Install packages: flask_babel 
2. use _('word to translate') or _l('Word to traslate in lazy mode')
3. from flask_babel import _ or from flask_babel import lazy_gettext as _l
4. *Extract text to translate:* pybabel extract -F babel.cfg -k _l -o messages.pot .
5. *Generate Catalog of lenguages:* pybabel init -i messages.pot -d app/translations -l es   (In this case Spanish)
6. *Compile text in runtime:* pybabel compile -d app/translations

Updatate the Translations
1. pybabel extract -F babel.cfg -k _l -o messages.pot .
2. pybabel update -i messages.pot -d app/translations



Notes: 
* The lenguage change is config by headers en each request you 
can use the browser, changing the lenguage or select some lenguaje for default in __init__.
* Is posible translate local hour:
    * from flask import g -> access from template
    * from flask_babel import get_locale -> local hour

## Command-Line Enhancements
Is posible create custom commands
1. Create cli.py into to application (app for this case)
2. Use @translate.command() and @app.cli.group() decorators (example in app/cli.py)

## Notes:
* Workaround: to avoid circular imports you can import package the last of module

git push https://cristhian2121@github.com/cristhian2121/flask_play_ground.git 