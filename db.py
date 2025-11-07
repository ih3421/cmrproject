import json

class Database:
    def __init__(self):
        self.file = 'users.json'

    def insert(self, name, email, password, user_type):
        with open(self.file, 'r') as rf:
            users = json.load(rf)

        if email in users:
            return 0

        users[email] = {
            "name": name,
            "password": password,
            "type": user_type
        }

        with open(self.file, 'w') as wf:
            json.dump(users, wf, indent=4)

        return 1

    def search(self, email, password):
        with open(self.file, 'r') as rf:
            users = json.load(rf)
        if email in users :
            if users[email]["password"] == password:
                return users[email]["type"]  # return role (pwd/Volunteer/Ngo)
        return 0
