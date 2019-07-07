from mongoengine import Document, StringField, DateTimeField
class GoogleResult(Document):
    url = StringField(max_length=1024, required=True)
    # retrieved_at = DateTimeField(required=True)
    # updated_at = DateTimeField(required=True)