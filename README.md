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


## Notes:
* Workaround: to avoid circular imports you can import package the last of module