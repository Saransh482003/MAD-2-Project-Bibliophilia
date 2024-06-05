import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

keys = redis_client.keys('*')

for key in keys:
    print(key.decode('utf-8'))