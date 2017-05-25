import midi

class Show():
    """ Show """
    __sets = []    
    
    def addSet(self):
        """ """
    def removeSet(self):
        """ """
    def editShow(self):
        """ """
    def reorderSets(self):
        """ """
    def Save(self):
        """ """
class Set():
    """ Set: """
    __songs = []
    def addSong(self):
        """ """
    def removeSong(self):
        """ """
    def editSet(self):
        """ """
    def reorderSongs(self):
        """ """
    def Save(self):
        """ """
        
class Song():
    """ Song """
    __parts = []
    
class SongPart():
    """ SongPart """
    __midiMsgPackages = []
    def Save(self):
        """ """
    def Undo(self):
        """ """
    
class Sequence():
    """ """
    

class Library():
    """ Library """
    __songs = []
    