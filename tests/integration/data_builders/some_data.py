class SomeDataBuilder(object):

    def __init__(self):
        self.something = None

    def build(self):
        return self.something

    def generate(self, name='something'):
        self.something = {
            'name': name,
            'date_of_creation': None,
        }
        return self
