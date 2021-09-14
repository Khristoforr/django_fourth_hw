from django.core.management.base import BaseCommand
from articles.models import Tag

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for tag in ['Культура', 'Город', 'Наука', 'Здоровье', 'Международные отношения', 'Космоc']:
            some_tag = Tag(name=tag)
            some_tag.save()