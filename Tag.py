class Tag:

    def __init__(self, title="", color=0):
        self.title = title
        self.color = color

    def __str__(self):
        return "{%s, %i}" % (self.title, self.color)

    def hex(self):
        print(hex(self.color))

    def colortohuman(self):
        return "Placeholder: %s" % self.color
        # TODO   Implement actual method logic
