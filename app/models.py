from django.db import models
from django.db.models import Model, DateTimeField, CharField, ImageField, TextField, ForeignKey, PROTECT, SET_NULL, \
    CASCADE


class BaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = CharField(max_length=255)
    image = ImageField(upload_to='post-images/', max_length=255)
    description = TextField()

    class Meta:
        db_table = 'posts'


class Comment(BaseModel):
    post = ForeignKey(Post, on_delete=CASCADE)
    description = TextField()

    class Meta:
        db_table = 'comments'
