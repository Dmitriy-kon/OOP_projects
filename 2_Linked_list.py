class ObjList:

    def __init__(self, data):
        self.__next = self.__prev = None
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new):
        if type(new) == str:
            self.__data = new

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, new):
        if type(new) in (ObjList, type(None)):
            self.__prev = new

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new):
        if type(new) in (ObjList, type(None)):
            self.__next = new


class LinkedList:

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj: ObjList):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj

        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_object_by_index(self, indx):
        h = self.head
        n = 0

        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx=None):
        obj = self.__get_object_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next

        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head

        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx):
        obj = self.__get_object_by_index(indx)
        return obj.data if obj else None
