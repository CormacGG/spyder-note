import datetime
from Tag import Tag


class Note:

    def __init__(self, title="", content=""):
        self.title = title
        self.content = content
        self.mentions = []
        self.tags = []

        self.__createdAt__ = datetime.datetime.now().time()

    def __str__(self):
        return "%s\n%s\n%s\n" % (self.title, self.content, self.tags)

    def replacecontent(self, content):
        self.content = content

    def addtag(self, tag):
        self.tags.append(tag)
        # Log?

    def removetag(self, tag=None, title=None):
        ret = False
        if tag is None:
            for tag in self.tags:
                if tag.title.lower() == title.lower():
                    self.tags.remove(tag)
                    ret = True

        else:
            if tag in self.tags:
                self.tags.remove(tag)
                ret = True

        return ret

    def printtags(self):
        print("tags:", *self.tags)

    def addmention(self, notes):
        self.mentions.append(notes)
        # Log?

    def removemention(self, note):
        ret = False
        for mention in self.mentions:
            if mention == note:
                self.mentions.remove(mention)
                ret = True

        return ret

    def mentioncount(self):
        return len(self.mentions)

    def printmentions(self):
        print("mentions:", *self.mentions, sep="\n")
