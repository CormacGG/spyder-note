
from Note import Note
from Tag import Tag


# Test creating
testNote = Note("I'm a Note", "Somebody wrote about me")
testMention = Note("I'm mentioned", "Somebody mentioned me")
testMention2 = Note("I'm mentioned again", "Somebody mentioned me again")

# Test Mentions and Note edits
testMention.printmentions()
testNote.addmention(testMention2)

print(testNote)
print(testMention)

testNote.printmentions()
testMention.printmentions()

testNote.replacecontent("I'm replaced content")
print(testNote)
print(testMention2)

print("Mention Count: %s\n" % testNote.mentioncount())
testNote.removemention(testMention)

# Test Tags
testTag = Tag("Code", 0)
testTag2 = Tag("Movie", 16711680)

testNote.addtag(testTag)
testMention.addtag(testTag2)

testNote.printtags()
testMention.printtags()

testNote.removetag(title="cOdE")
testMention.removetag(testTag2)
testNote.printtags()
testMention.printtags()