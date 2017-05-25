"""  """

class MIDIMessageType(object):
    
    type = 'MIDIMessageType'
    def __init__(self):
        self.__str__(self.type + " " + " test.")

class MIDIMessage(object):
    type = 'MIDIMessage'
    __dict__ = {}
    def __init__(self):
        """ MIDI Message initialized. """

class MIDIPackage(object):
    def __init__(self):
        """ MIDI Message initialized. """
        