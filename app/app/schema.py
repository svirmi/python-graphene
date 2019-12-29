import graphene
import tracks.schema
import users.schema

# inherites tracks schema
class Query(tracks.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,tracks.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)