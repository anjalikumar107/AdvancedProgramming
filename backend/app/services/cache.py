import time

cache = {}

# get cached data if it hasn't expired
def get_cache(key):
    value = cache.get(key)
    if not value:
        return None
    expiry, data = value
    if time.time() > expiry:
        del cache[key]
        return None
    return data

# save data in cache for a set number of seconds
def set_cache(key, data, seconds):
    cache[key] = (time.time() + seconds, data)