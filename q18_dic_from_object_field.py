'''write a python program to get a dictionary from an object`s field.'''

class dictobj(object):
    def _init_(self):
        self.x='red'
        self.y='yellow'
        self.z='green'
    def do_nothing(self):
        pass
test= dictobj()
print(test)