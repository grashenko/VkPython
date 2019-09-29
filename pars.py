import vk
import sys
from datetime import datetime

class ParseItem:
  def __init__(self, id, deep, parentId):
    self.deep = deep
    self.id = id
    self.parentId = parentId

class User:
  def __init__(self, id, age, countPhoto, countVideo, countNotes, countGroups):
    self.id = id
    self.age = age
    self.photo = countPhoto
    self.countVideo = countVideo
    self.countNotes = countNotes
    self.countGroups = countGroups

def ParseUserFriends(Id, deep):
    if deep < max_deep:
        try:
            deep += 1
            friends = vk_api.friends.get(user_id=Id, order='hints', v = 5.101)
            mapItems = map(lambda fr: ParseItem(fr, deep, Id) , friends['items'])
            parseItems = list(mapItems)
        except:
            return

        parsedUsers.extend(parseItems)
        for item in parseItems:
            ParseUserFriends(item.id, item.deep)
    else:
        return

def GetUserInfoById(Id):
    try:
        user = vk_api.users.get(user_ids=[1,2,3], fields='bdate, counters', v = 5.101)
        datestr = user[0]['bdate']
        datetime_object = datetime.strptime(datestr, '%d.%m.%Y')
        return 
    except:
        return


session = vk.Session(access_token='1ea98e751ea98e751ea98e75fe1ec3dc8611ea91ea98e75426032100701925fae2131d8')
vk_api = vk.API(session)
max_deep = 2
startId = 69504867
parsedUsers = []

ParseUserFriends(startId, 0)

GetUserInfoById(startId)

print(parsedUsers)

