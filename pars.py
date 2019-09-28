import vk
session = vk.Session(access_token='1ea98e751ea98e751ea98e75fe1ec3dc8611ea91ea98e75426032100701925fae2131d8')
vk_api = vk.API(session)
max_deep = 2
startId = 69504867
parsedUsers = []

class ParseItem:
    deep = 0
    friends = []

def ParseUserFriends(Id, deep):
    if deep <= max_deep:
        try:
            friends = vk_api.friends.get(user_id=Id, order='hints', v = 5.101)
        except:
            return

        friends = vk_api.friends.get(user_id=Id, order='hints', v = 5.101)
        parsedUsers.extend(friends['items'])
        deep += 1
        item = ParseItem()
        item.deep = deep
        item.friends = friends
        for friend in item.friends['items']:
            ParseUserFriends(friend, item.deep)
    else:
        return

ParseUserFriends(startId, 0)

print(parsedUsers)

