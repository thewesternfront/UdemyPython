
class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)