nestedDict = {'a':{'b':{'c':['aa','bb','cc']}}, '1':{'2':{'3':['32','43']}}}
def findDataFromNestedDict(nestedDict, dict_keys):
    if dict_keys in nestedDict.keys():
        return nestedDict[dict_keys]
    for key, value in nestedDict.items():
        if isinstance(value, dict):
            return  findDataFromNestedDict(value,dict_keys)
data =  findDataFromNestedDict(nestedDict, '1') print(data)

#find any data from nested dict having list using key:

data = {"friendslist":{"friends":[{"steamid":"7656xxxxxxx80x76","relationship":"friend","friend_since":1552765824},{"steamid":"76561xxxxxxx4xx89","relationship":"friend","friend_since":1508594830},{"steamid":"765xxxxxxxxxxx3194","relationship":"friend","friend_since":1543773569}]}}
def getDataFromNestedDict(data, dictKey):
    if isinstance(data, dict):
        if dictKey in data.keys():
            steamDataList.append(data[dictKey])
        for key, value in data.items():
            if isinstance(value, dict):
                getDataFromNestedDict(value, dictKey)
            elif isinstance(value, list):
                for item in value:
                    getDataFromNestedDict(item,dictKey)

    elif isinstance(data, list):
        for item in data:
            getDataFromNestedDict(item,dictKey)
steamDataList = []
getDataFromNestedDict(data, 'steamid')
print(steamDataList)
