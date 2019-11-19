import vk
import sys
from datetime import datetime
import json


class ParseItem:
  def __init__(self, id, deep, parentId):
    self.deep = deep
    self.id = id
    self.parentId = parentId
    self.childrens = []

class User:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def __init__(self, id, age, countPhoto, countVideo, countNotes, countGroups):
        self.id = id
        self.age = age
        self.photo = countPhoto
        self.countVideo = countVideo
        self.countNotes = countNotes
        self.countGroups = countGroups

def ParseUserFriends(Id, deep, item):
    if deep < max_deep:
        try:
            deep += 1
            friends = vk_api.friends.get(user_id=Id, order='hints', v = 5.101)
            mapItems = map(lambda fr: ParseItem(fr, deep, Id) , friends['items'])
            parseItems = list(mapItems)
            item.childrens = parseItems
        except:
            return
        parsedUsers.extend(parseItems)
        for item in item.childrens:
            ParseUserFriends(item.id, item.deep, item)
    else:
        return


def PrintTree(item):
    try:
        if item.deep == 0:
            tree.write('---' + str(item.id)+'\n')
        if item.deep == 1:
            tree.write('           ----------------'+ str(item.id)+'\n')
        if item.deep == 2:
            tree.write('                             -------------------------------------'+ str(item.id)+'\n')
        
        for child in item.childrens:
            PrintTree(child)
    except:
        return


def GetUserInfoById(Id):
    try:
        userInfo = vk_api.users.get(user_id=Id, fields='bdate, counters', v = 5.101)
        
        try:
            datestr = userInfo[0]['bdate']
            now = datetime.now()
            birthday = datetime.strptime(datestr, '%d.%m.%Y')
            age = now.year - birthday.year
        except:
            age = 0

        try:
            photos = userInfo[0]['counters']['photos']
        except:
            photos = 0

        try:
            videos = userInfo[0]['counters']['videos']
        except:
            videos = 0

        try:
            notes = userInfo[0]['counters']['notes']
        except:
            notes = 0
        try:
            groups = userInfo[0]['counters']['groups']
        except:
            groups = 0

        return User(Id, age, photos, videos, notes, groups)

    except Exception as er:
        print(er)
        return


session = vk.Session(access_token='1ea98e751ea98e751ea98e75fe1ec3dc8611ea91ea98e75426032100701925fae2131d8')
vk_api = vk.API(session)
max_deep = 2
startId = 69504867
parsedUsers = []
usersInfo = []

root = ParseItem(startId,0,0)

ParseUserFriends(startId, 0, root)

tree = open("Tree.txt","w") 
PrintTree(root)
tree.close()

for user in parsedUsers:
    us = GetUserInfoById(user.id)
    if us is not None:
        usersInfo.append(us)


with open('data.json', 'w') as outfile:
    json.dump(usersInfo, outfile, default=lambda x: x.__dict__)

