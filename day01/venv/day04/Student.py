class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))



ddd = Student("sdfsfs","20")
ddd.print_score()
print(type(ddd))
print(dir(ddd))
print(getattr(ddd,'age',45))
print(hasattr(ddd,'age'))