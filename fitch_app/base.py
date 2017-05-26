__all__ = ['Base']

class Base(object):
    """ Base object for fitch. """ 

    def __str__(self):
        #return '{type}: {attrib}'.format(type=self.type, attrib=str(self.__getattribute__()))
        return 'type = {type}\r\n{doc}\r\n\r\n{attributes}'.format(
            type=self.__type, 
            doc=self.__doc__, 
            attributes='\r\n'.join(dir(self))
        )