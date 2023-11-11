#!/usr/bin/python3
"""Module for creating Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Updates instance of no-keyword & keyworded args"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def to_csv_row(self):
        """Return a list of attributes for CSV serialization"""
        return [self.id, self.size, self.x, self.y]
