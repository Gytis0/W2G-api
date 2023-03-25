class YTVideo:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.link = "https://www.youtube.com/watch?v=" + id
        self.thumb = "https://i.ytimg.com/vi/" + id + "/default.jpg"

    def encode(self):
        return self.__dict__