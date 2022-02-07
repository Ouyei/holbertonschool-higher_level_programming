#!/usr/bin/python3
# rectangle.py
# Oscar Bedat <3961@holbertonschool.com>
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: Class define rectangle
    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialized constuctor
        Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter value for width
        """
        return self.__width

    @width.setter
    def width(self, param):
        """Setter value for width
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """Getter value for height
        """
        return self.__height

    @height.setter
    def height(self, param):
        """Setter value for height
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """Getter value for x
        """
        return self.__x

    @x.setter
    def x(self, param):
        """Setter value for x"
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """Getter value for y
        """
        return self.__y

    @y.setter
    def y(self, param):
        """Setter value for y
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """area: area rectangle
        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """display: prints in stdout the Rectangle instance
        with the character #
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """__str__ print information for rectangle
        Returns:
            [str]: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """update use args and kwargs
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
