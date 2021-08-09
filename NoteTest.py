import unittest
from Note import Note
from Tag import Tag


class NoteTest(unittest.TestCase):
    def testconstruct(self):
        note = Note()
        self.assertEqual(note.title, "")
        self.assertEqual(note.content, "")
        self.assertEqual(len(note.mentions), 0)
        self.assertEqual(len(note.tags), 0)

    def testconstructtitle(self):
        note = Note("Title")
        self.assertEqual(note.title, "Title")
        self.assertEqual(note.content, "")
        self.assertEqual(len(note.mentions), 0)
        self.assertEqual(len(note.tags), 0)

    def testconstructcontent(self):
        note = Note("", "Content")
        self.assertEqual(note.title, "")
        self.assertEqual(note.content, "Content")
        self.assertEqual(len(note.mentions), 0)
        self.assertEqual(len(note.tags), 0)

    def testreplacetitle(self):
        note = Note("Title", "Content")
        note.replacetitle("New Title")
        self.assertEqual(note.title, "New Title")

    def testreplacecontent(self):
        note = Note("Title", "Content")
        note.replacecontent("New Content")
        self.assertEqual(note.content, "New Content")

    def testaddtag(self):
        note = Note("Title", "Content")
        note.addtag(Tag("Red", 100))
        self.assertEqual(note.tags[0].color, 100)
        self.assertEqual(note.tags[0].title, "Red")

    def testremovetag(self):
        note = Note("Title", "Content")
        note.addtag(Tag("Red", 100))
        note.addtag(Tag("Blue", 10))
        self.assertEqual(note.removetag("Red"), True)
        self.assertEqual(note.removetag(Tag("Blue", 10)), True)

    def testaddmention(self):
        note = Note("Title", "Content")
        note.addmention(Note("Mention Title", "Mention Content"))
        self.assertEqual(note.mentions[0].title, "Mention Title")
        self.assertEqual(note.mentions[0].content, "Mention Content")

    def testremovemention(self):
        note = Note("Title", "Content")
        mention = Note("Mention Title", "Mention Content")
        note.addmention(mention)

        self.assertEqual(note.removemention(mention), True)


if __name__ == '__main__':
    unittest.main()
