#!/usr/bin/python3
# square.py
# Oscar Bedat <3961@holbertonschool.com>
"""Define Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square: Class define square
    Args:
        Rectangle (class): parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ print information for square
        Returns:
            [str]: [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter value for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter value for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update use args and kwargs
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary with values for rectangle
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
