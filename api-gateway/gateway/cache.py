from datetime import datetime, timedelta
from config import CACHE_EXPIRATION  # Import CACHE_EXPIRATION from config

cache = {}

def cache_response(key, data, expiration=CACHE_EXPIRATION):
    cache[key] = (data, datetime.now() + timedelta(seconds=expiration))

def get_cached_response(key):
    if key in cache:
        data, expiration = cache[key]
        if datetime.now() < expiration:
            return data
        else:
            del cache[key]
    return None
