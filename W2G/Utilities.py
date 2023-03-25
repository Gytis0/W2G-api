import json

def WriteW2G(resp, fileName):
    fileStream = open(fileName, "w", encoding="utf-8")
    fileStream.write(str(resp.__dict__))
    fileStream.close()

def WriteYT(resp, fileName):
    fileStream = open(fileName, "w", encoding="utf-8")
    jsonStr = json.dumps(resp, default = lambda o: o.encode())
    fileStream.write(jsonStr)
    fileStream.close()

def AppendYT(resp, fileName):
    fileStream = open(fileName, "a", encoding="utf-8")
    fileStream.write(str(resp))
    fileStream.close()

def ResponseW2G(resp):
    print("Status: " + str(resp.status) + "\n")
    print("Data: " + str(resp.data) + "\n")
    print("Headers: " + str(resp.headers) + "\n")

def ResponseYT(resp):
    print("Response: " + str(resp) + "\n")

def WritePageCount(count):
    fileStream = open("pageCount.txt", "w", encoding="utf-8")
    fileStream.write(str(count))
    fileStream.close()

def ReadPageCount():
    fileStream = open("pageCount.txt", "r", encoding="utf-8")
    ans = fileStream.readline()
    fileStream.close()

    return int(ans)

def Read50VideosFromJSON(page, fileName):
    f = open(fileName, "r")
    jsonData = f.read()
    f.close()

    videoList = json.loads(jsonData, object_hook=customDecoder)
    ans = []
    for i in range(50*page, 50*(page+1)):
        ans.append(videoList[i])


    return ans