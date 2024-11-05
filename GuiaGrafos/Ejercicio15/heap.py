

class HeapMax():

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index-1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] > self.elements[left_child]:
                    max = right_child
            if self.elements[index] < self.elements[max]:
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        self.elements = elements
        for i in range(len(self.elements)):
            self.float(i)

    def sort(self):
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index
    
    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.float(index)
            elif new_priority < previous_priority:
                self.sink(index)


class HeapMin():

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index-1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            min = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] < self.elements[left_child]:
                    min = right_child
            if self.elements[index] > self.elements[min]:
                self.interchange(index, min)
                index = min
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        self.elements = elements
        for i in range(len(self.elements)):
            self.float(i)

    def sort(self):
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority < previous_priority:
                self.float(index)
            elif new_priority > previous_priority:
                self.sink(index)


