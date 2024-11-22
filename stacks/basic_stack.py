
class basic_stack:
    def __init__(self):
        self.__cursor = 0
        self.__data = []
    
    def size(self):
        return self.__cursor
    
    def top(self):
        return self.__data[self.__cursor-1]

    def pop(self):
        if (self.__cursor > 0):
            t = self.__data.pop()
            self.__cursor -= 1
            return t
        else : return None

    def push(self, value):
        self.__data.append(value)
        self.__cursor += 1
        
    def reverse(self):
        st = basic_stack()
        cur = self.pop()

        while(cur != None):
            st.push(cur)
            cur = self.pop()

        return st

t = basic_stack()
t.push(1)
t.push(2)
t.push(3)
t.push(4)


rev  = t.reverse()
print(rev.size())
print(rev.pop())
print(rev.pop())
print(rev.pop())
print(rev.pop())
print(rev.pop())