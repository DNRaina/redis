import redis

r = redis.Redis(
    host= 'localhost',
    port = 6379,
    db = 0 
)

# r.hset("user:1001", "name", "alice")
# r.hset("user:1001", "email", "alice@exampleusage.com")


# #retrieving the email now
# email = r.hget("user:1001", "email")
# print(email.decode('uf-8'))


# # deleting a user email
# r.hdel("user:1001", "email")

def create_user_profile(id, name, email):
    """
    creates a user profile in Redis """

    user_key = f"user:{id}"
    r.hset(user_key, mapping= {"name": name, "email" : email})

def get_user_profile(id):
    """retrieves and returns the field in the user profile"""

    user_key = f"user:{id}"
    profile_data = r.hgetall(user_key)
    return {k.decode('utf-8') : v.decode('utf-8') for k,v in profile_data.items()}

def delete_user_profile(id):
    """delete a user profile and all the attributes of it from the redis"""

    user_key = f"user:{id}"
    r.delete(user_key)

create_user_profile(1002, "Bob", "bob@example.com")
print(get_user_profile(1002))
delete_user_profile(1002)

