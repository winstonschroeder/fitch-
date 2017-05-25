"""A finite mealy state machine. """

from base import *
from __builtin__ import property

class EndState(Base):
    """ The base state."""        
    __type = 'State'
    name = ''
    def __init__(self,name):
        self.name = name

class State(EndState):
    """ The Starting point """
    __type = 'EndState'
    __transitions = []

class StartState(State):
    """ The Starting point """
    __type = 'StartState'

class Signal(Base):
    """ """
    __type = 'Signal'
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Type {type}: {name}'.format(type=self.__type,name=self.name)

class InputSignal(Signal):
    """ """
    __type = 'InputSignal'
    def __init__(self):
        assert 0, 'Input Signal not implemented yet.'
class OutputSignal(Signal):
    """ """
    __type = 'OutputSignal'
        

class InputSignalList(list):

    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(InputSignalList, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, InputSignal):
            super(InputSignalList, self).append(item)
        else:
            raise ValueError('InputSignals allowed only')

    def insert(self, index, item):
        if isinstance(item, InputSignal):
            super(InputSignalList, self).insert(index, item)
        else:
            raise ValueError('InputSignals allowed only')

    def __add__(self, item):
        if isinstance(item, InputSignal):
            super(InputSignalList, self).__add__(item)
        else:
            raise ValueError('InputSignals allowed only')

    def __iadd__(self, item):
        if isinstance(item, InputSignal):
            super(InputSignalList, self).__iadd__(item)
        else:
            raise ValueError('InputSignals allowed only')

class OutputSignalList(list):

    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(OutputSignalList, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, OutputSignal):
            super(OutputSignalList, self).append(item)
        else:
            raise ValueError('OutputSignals allowed only')

    def insert(self, index, item):
        if isinstance(item, OutputSignal):
            super(OutputSignalList, self).insert(index, item)
        else:
            raise ValueError('OutputSignals allowed only')

    def __add__(self, item):
        if isinstance(item, OutputSignal):
            super(OutputSignalList, self).__add__(item)
        else:
            raise ValueError('OutputSignals allowed only')

    def __iadd__(self, item):
        if isinstance(item, OutputSignal):
            super(OutputSignalList, self).__iadd__(item)
        else:
            raise ValueError('OutputSignals allowed only')

class Condition(Base):
    """ """
    operator = ()
    valueToCompare = object()
    __inputSignal = None
    def condition(self,signal,operator,value):
        assert 0, "condition not implemented yet"

class Transition(Base):
    
    __type = 'Transition'
    __nextState = None    
    __inputSignals = InputSignalList()
    __outputSignals = OutputSignalList()   
    
    def __init__(self):
        """ """
        
    def __getInputSignals(self):
        return self.__inputSignals
    def __getOutputSignals(self):
        return self.__outputSignals
    
    
    def __setNextState(self, state):
        if state.type()=='State' or state.type()=='EndState':
            self.__nextState = state
        elif state.type()=='StartState':
            raise Exception('States of type StartState cannot be used as transition target.')
        else:
            raise Exception('Setting to state failed due to wrong datatype. Type={type}'.format(type=state.type()))
    def __getNextState(self):
        return self.__nextState
    
    nextState = property(__getNextState, __setNextState, None, 'nextState')
    
    outputSignals = property(__getOutputSignals, None, None, 'outputSignals')
    inputSignals = property(__getInputSignals, None, None, 'inputSignals')
    


t = Transition()
t.outputSignals.append(OutputSignal('signal one'))
t.outputSignals.append(OutputSignal('signal two'))

print t.outputSignals[0]

