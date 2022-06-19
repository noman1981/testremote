import abc


class StackMeta(metaclass=abc.ABCMeta):
    """
    Declaring Interface for Stack.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'size') and
                callable(subclass.size) and
                hasattr(subclass, 'push') and
                callable(subclass.push) and
                hasattr(subclass, 'empty') and
                callable(subclass.empty) and
                hasattr(subclass, 'pop') and
                callable(subclass.pop) and
                hasattr(subclass, 'peek') and
                callable(subclass.peek)
                )

    @abc.abstractmethod
    def size(self):
        """ return size of stack """
        raise NotImplementedError

    @abc.abstractmethod
    def push(self, value):
        """Insert data into stack"""
        raise NotImplementedError

    @abc.abstractmethod
    def empty(self):
        """Tells if stack is empty or Not"""
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        """Delete last value and returns it"""
        raise NotImplementedError

    @abc.abstractmethod
    def peek(self):
        """Return Last value without deleting"""
        raise NotImplementedError


class Stack(StackMeta):
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, value):
        if value:
            if isinstance(value, int):
                self.stack.append(value)
                return True
            else:
                raise ValueError('Only allow int values')
        else:
            raise TypeError()

    def empty(self):
        if self.size():
            return False
        else:
            return True

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            raise IndexError('EmptyStackException')

    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            raise IndexError('EmptyStackException')


