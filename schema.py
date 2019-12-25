import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_users(self, info):
        return [
            User(id='1', username="John", created_at=datetime.now()),
            User(id='2', username="Bill", created_at=datetime.now()),
            User(id='3', username="Donald", created_at=datetime.now()),
        ]

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True


schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        users {
            id
            username
            createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))
