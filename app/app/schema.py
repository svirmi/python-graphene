import graphene
import tracks.schema

# inherites tracks schema
class Query(tracks.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)