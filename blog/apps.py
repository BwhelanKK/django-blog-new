from django.apps import AppConfig

"""
Provides primary key type for blog app.
"""


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
