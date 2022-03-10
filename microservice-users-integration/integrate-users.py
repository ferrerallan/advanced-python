import redis
import json

client = redis.Redis(
      host="redis-14456.c240.us-east-1-3.ec2.cloud.redislabs.com", 
      port=14456, 
      password="Z94ktX55ssB05mPRq2mRWQdERcqbRB6m",
      decode_responses=True
    )

processed_users=[]

while(True):
  body= client.json().get('pendingUsers')
  id = body["user"]["id"]

  if id not in processed_users:
    print(f"new user added {id}")
    processed_users.append(id)
