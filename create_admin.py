from getpass import getpass
import sys


from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input("Import name: ")

    if User.query.filter(User.username == username).count():
        print("User already exists")
        sys.exit(0)

    password1 = getpass("Write password")
    password2 = getpass("Repeat password")

    if not password1 == password2:
        print("Passowrds don't match")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print("User id {} added".format(new_user.id))
