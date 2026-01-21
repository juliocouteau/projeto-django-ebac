from django.contrib import admin
from .models import Post  # Importa o modelo que você criou

admin.site.register(Post)  # Registra ele no Admin