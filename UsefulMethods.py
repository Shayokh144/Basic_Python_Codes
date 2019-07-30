nestedDict = {'a':{'b':{'c':['aa','bb','cc']}}, '1':{'2':{'3':['32','43']}}}
def findDataFromNestedDict(nestedDict, dict_keys):
    if dict_keys in nestedDict.keys():
        return nestedDict[dict_keys]
    for key, value in nestedDict.items():
        if isinstance(value, dict):
            return  findDataFromNestedDict(value,dict_keys)
data =  findDataFromNestedDict(nestedDict, '1') print(data)
