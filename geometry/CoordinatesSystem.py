class Coordinates(object):
    def __init__(self, translation, rotation=None, parent=None):
        self.translation = translation
        self.rotation = rotation
        self.parent = parent

    @property
    def x(self):
        return self.translation[0]

    @property
    def y(self):
        return self.translation[1]

    @property
    def z(self):
        return self.translation[2]
