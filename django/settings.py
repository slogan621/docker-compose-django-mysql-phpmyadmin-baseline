import os
import dj_database_url
from pathlib import Path

# ... other settings ...

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# ...
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
# ...

