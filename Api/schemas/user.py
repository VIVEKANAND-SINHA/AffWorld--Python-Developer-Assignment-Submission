

def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item['name'],
        "email":item['email'],
        "password":item['password'],
        "phone":int(item['phone']),
        "imageUrl":str(item['imageUrl']),
        "isActive": bool(item["imageUrl"]),

    }

def usersEntity(entity) ->list:
    return [userEntity(item) for item in entity]