class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
		    print self.lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

#print lyrics

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "printing the init func"
happy_bday.__init__(Song)

