"""A finite mealy state machine. """

from base import *
from __builtin__ import property

class EndState(Base):
    """ The base state."""   
    def __init__(self,name):
        self.name = name

class State(EndState):
    """ The Starting point """
    def __init__(self, name):
        super(self.__class__, self).__init__(name)
        self.__transitions = []

class StartState(State):
    """ The Starting point """
    def __init__(self, name):
        super(self.__class__,self).__init__(name)
        self.__transitions = []

class Signal(Base):
    """ """
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Type {type}: {name}'.format(type=type(self),name=self.name)

class InputSignal(Signal):
    """ """
    def __init__(self):
        assert 0, 'Input Signal not implemented yet.'
class OutputSignal(Signal):
    """ """
    def __init__(self,name):
        super(self.__class__,self).__init__(name)
    
        

class InputSignalList(list):

    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(self.__class__, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, InputSignal):
            super(self.__class__, self).append(item)
        else:
            raise ValueError('InputSignals allowed only')

    def insert(self, index, item):
        if isinstance(item, InputSignal):
            super(self.__class__, self).insert(index, item)
        else:
            raise ValueError('InputSignals allowed only')

    def __add__(self, item):
        if isinstance(item, InputSignal):
            super(self.__class__, self).__add__(item)
        else:
            raise ValueError('InputSignals allowed only')

    def __iadd__(self, item):
        if isinstance(item, InputSignal):
            super(self.__class__, self).__iadd__(item)
        else:
            raise ValueError('InputSignals allowed only')

class OutputSignalList(list):

    def __init__(self, iterable=None):
        """Override initializer which can accept iterable"""
        super(self.__class__, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        if isinstance(item, OutputSignal):
            super(self.__class__, self).append(item)
        else:
            raise ValueError('OutputSignals allowed only')

    def insert(self, index, item):
        if isinstance(item, OutputSignal):
            super(self.__class__, self).insert(index, item)
        else:
            raise ValueError('OutputSignals allowed only')

    def __add__(self, item):
        if isinstance(item, OutputSignal):
            super(self.__class__, self).__add__(item)
        else:
            raise ValueError('OutputSignals allowed only')

    def __iadd__(self, item):
        if isinstance(item, OutputSignal):
            super(self.__class__, self).__iadd__(item)
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
    
    def __init__(self):
        """ """
        self.__nextState = None    
        self.__inputSignals = InputSignalList()
        self.__outputSignals = OutputSignalList()
    
    def __getInputSignals(self):
        return self.__inputSignals
    def __getOutputSignals(self):
        return self.__outputSignals
    
    
    def __setNextState(self, state):
        if type(state)=='State' or type(state)=='EndState':
            self.__nextState = state
        elif type(state)=='StartState':
            raise ValueError('States of type StartState cannot be used as transition target.')
        else:
            raise ValueError('Setting to state failed due to wrong datatype. Type={type}'.format(type=state.type()))
    def __getNextState(self):
        return self.__nextState
    
    nextState = property(__getNextState, __setNextState, None, 'nextState')
    
    outputSignals = property(__getOutputSignals, None, None, 'outputSignals')
    inputSignals = property(__getInputSignals, None, None, 'inputSignals')

class StateMachine(Base):
    def __init__(self,initialState, tranTable):
        self.state = initialState
        self.transitionTable = tranTable


t = Transition()
t.outputSignals.append(OutputSignal('signal one'))
t.outputSignals.append(OutputSignal('signal two'))

print t.outputSignals[0]

