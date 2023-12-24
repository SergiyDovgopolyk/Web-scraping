from mongoengine import Document, StringField, ListField, ReferenceField, connect

connect(
    db='my-data-base',
    username='admin',
    password='51252cenia',
    host='cluster0.xvs4vtf.mongodb.net',
    port=27017,
    authentication_source='admin',
    retryWrites=True,
    w='majority'
)

class AuthorItem(Document):
    fullname = StringField(required=True)
    date_born = StringField()
    location_born = StringField()
    bio = StringField()

class QuoteItem(Document):
    keywords = ListField(StringField())
    author = ReferenceField(AuthorItem, required=True)
    quote = StringField()