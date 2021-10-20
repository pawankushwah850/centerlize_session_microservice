<h1>Centralized Session based microservice application </h1>

<p>We are using redis server for storing sessions and caching. 
And to maintaining user authentication we using cookies based session.</p>

<code>
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
</code>