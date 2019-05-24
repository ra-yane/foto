import json

from peewee import *

from ..core import db


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    admin = BooleanField(default=False)
    team_leader = BooleanField(default=False)

    def get_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email,
                "admin": self.admin, "team_leader": self.team_leader}

    def get_small_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "admin": self.admin,
                "team_leader": self.team_leader}

    def add_credentials(self, credentials):
        from .gcredentials import GCredentials
        data = credentials.copy()
        data['user'] = self.id
        data['scopes'] = json.dumps(data['scopes'])
        try:
            with db.atomic():
                GCredentials.create(**data)
        except IntegrityError:
            with db.transaction():
                GCredentials.delete().where(GCredentials.user == self.id).execute()
                GCredentials.create(**data)

    def get_credentials(self):
        from .gcredentials import GCredentials
        gcredentials = list(GCredentials.select().where(GCredentials.user == self.id).dicts())
        data = gcredentials[0].copy()
        data['scopes'] = json.loads(data['scopes'])
        del data['user']
        del data['id']
        return data

    class Meta:
        database = db


with db:
    User.create_table(fail_silently=True)
