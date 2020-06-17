from django.db import models

class Task:
    
    def __init__(self, title, content, cover):
        self.title = title
        self.content = content
        self.cover = cover
