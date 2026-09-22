""" this code examples shows you how to store and retrieve user sessions"""

import uuid
import redis

r = redis.Redis(
    host = "localhost",
    port = 6379,
    db = 0
)

def store_user_session(user_id):
    """generates a unique identifier for a user and stores it
    the session is stored in the pattern : user : {user_id} : session"""

    session_key = f"user : {user_id} : session"
    token = str(uuid.uuid4())
    r.set(session_key, token)
    return token

def get_user_session(user_id):
    """retrieves the user session from the redis for the given user_id
    return none if the sessions doesn't exist or is expired"""

    session_key = f"user : {user_id} : session"
    token = r.get(session_key)
    return token.decode('utf-8') if token else None

def delete_user_session(user_id):
    """deletes the entry from redis for the specified user_id"""

    session_key = f"user : {user_id} : session"
    r.delete(session_key)

#usage demo

session_token = store_user_session(1001)
print(f"stored session token : {session_token}")

retrieved_token = get_user_session(1001)
print(retrieved_token)

delete_user_session(1001)
print(f"session after delete : {get_user_session(1001)}")
