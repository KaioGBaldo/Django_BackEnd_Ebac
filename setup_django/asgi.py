import os
from django.core.asgi import get_asgi_application

# Define qual arquivo de settings o servidor deve usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup_django.settings')

# Inicializa a aplicação ASGI
application = get_asgi_application()
