#this python code module cover strings in python
import redis

r = redis.Redis(
    host = 'localhost', 
    port = 6379, 
    db = 0 #the default Redis database index
)

r.set("mykey", "hello from Windows")

value = r.get("mykey")
print(value)

print(value.decode())

r.delete("mykey")

"""we instantiate a redis client, connect it to localhost and then store a string
under the mykey, we retrieve it and convert bytes to string, then we delete it"""