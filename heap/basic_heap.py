
from math import *

class basic_heap:
    def __init__(self):
        self.__data=[]
        self.__sz = 0
    
    def get_height(self):
        return floor(log(self.__sz, 2))

    def parent_index(self, level, segment):
        rindex = int((pow(2, level) -1 ) + segment)
        return rindex

    def get_parent_segment(self):
        level_start_index = pow(2, self.get_height()) - 1
        level_size = (self.__sz - level_start_index)
        #   0         1       2
        # [1, 2]  [3, 4]  [5, 6]
        return floor((level_size-1) / 2)

    def random_access(self, index_level, segment_index):
        if (index_level < 0):
            return None
        if (index_level == 0):
            if (self.__sz == 0):
                return None
            else:
                return self.__data[0]
        rindex = self.parent_index(index_level, segment_index)
        return self.__data[rindex]

    def add(self, el):
        self.__data.append(el)
        self.__sz += 1

        par_index = self.get_parent_segment()
        level = self.get_height()
        parent = self.random_access(level-1, par_index)

        el_index = self.__sz-1
        #par_index = self.parent_index(level, par_index)
        print(f"Tg={el} el={el_index} par={par_index} V(el)={self.__data[el_index]} V(par)={self.__data[par_index]}")

        while(parent != None):
            if (parent < el):
                # swap
                print(f"___Tg={el} el={el_index} par={par_index} V(el)={self.__data[el_index]} V(par)={self.__data[par_index]}")
                (self.__data[el_index], self.__data[par_index]) = (self.__data[par_index], self.__data[el_index])


                
                level -= 1
                el_index = par_index
                par_index = self.parent_index(level, par_index)
                parent = self.random_access(level, par_index)
                
                #(el, parent) = (parent, el)

            else: 
                break

        #print(f"added: e={el} level_start={level_start_index} Lsize={level_size} LSeg={level_segment}")

    def as_list(self):
        ls = []
        for el in self.__data:
            ls.append(el)

        return ls

def make_heap(arr=[]):
    for i in range(0, len(arr)):
        index = i
        while(index != 0):
            parent = int((index-1)/2)
            
            if (arr[index] <= arr[parent]):
                break

            (arr[index], arr[parent]) = (arr[parent], arr[index])
            index = parent

t = basic_heap()

t1 = [1,2,3, -3, 4]
make_heap(t1)
print(t1)
