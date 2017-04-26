import redis


class Cache(object):

    def get(self, key):
        pass

    def set(self, key, value):
        pass


class RedisCache(Cache):
    db = redis.StrictRedis(host='localhost', port=6379, db=1)

    def get(self, key):
        return RedisCache.db.get(key)

    def set(self, key, value):
        return RedisCache.db.set(key, value)

    def sort(self):
        return sorted(RedisCache.db.keys())
