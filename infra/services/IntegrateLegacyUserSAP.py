from application.usecases.createuser.protocols.AbsIntegrateLegacyUser import AbsIntegrateLegacyUser
import redis
import json
from redis.commands.json.path import Path


def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

class IntegrateLegacyUserSAP(AbsIntegrateLegacyUser):
  def integrate(self, user):
    client = redis.Redis(
      host="redis-14456.c240.us-east-1-3.ec2.cloud.redislabs.com", 
      port=14456, 
      password="Z94ktX55ssB05mPRq2mRWQdERcqbRB6m",
      decode_responses=True
    )

    output = {
      f"user":{
      "id": user.id,
      "name": user.name,
      "cpf": user.cpf
      }
    }

   
    
    #if (client.json().get(f"pendingusers") == None):
    #  print("pendingusers not found.creating...")
    #  client.execute_command('JSON.SET', f'pendingusers', '.', json.dumps({}))
    #  #client.json().set(f"pendingusers", Path.rootPath(), "")
    # # else:
    # #   print("creting new user")
    # client.json().set(f'usuario_{user.id}', Path.rootPath()+"\pending", output)
    #client.set("users", output)

    #r = redis.StrictRedis()
    data = {}
    try:
      data = json.loads(client.execute_command('JSON.GET', 'pendingUsers'))
    except:
      data={}
    
    newData = merge_two_dicts(data,output)

    print(newData)
    client.execute_command('JSON.SET', "pendingUsers", ".", json.dumps(newData))

    return super().integrate(user)