#!/usr/bin/python3
"""Module that defines Base class."""
import json
import csv
import turtle


class Base:
    """A class representing a base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a base, with id.

        Args:
            id: Unique id for new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of object to a file."""
        with open(f"{cls.__name__}.json", 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                str_json = Base.to_json_string(list_dict)
                f.write(str_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        dummy_instance = cls(1, 1, 1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                json_str = f.read()
                dict_list = Base.from_json_string(json_str)
                inst_list = [cls.create(**dict_obj) for dict_obj in dict_list]
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Converts objects to CSV format and saves to file."""
        with open(f"{cls.__name__}.csv", mode='w', newline='') as f:
            if list_objs is None or not list_objs:
                f.write("[]")
            else:
                writer_obj = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer_obj.writerow([obj.id, obj.width, obj.height,
                                             obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer_obj.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Converts data in CSV file to Python object."""
        inst_list = []
        try:
            with open(f"{cls.__name__}.csv", mode='r', newline='') as f:
                reader_obj = csv.reader(f)
                for row in reader_obj:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]),
                                  int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]),
                                  int(row[0]))
                    inst_list.append(obj)
        except FileNotFoundError:
            return []

        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares,
        using Turtle graphics module.
        """
        turtle.Turtle()
        turtle.bgcolor("yellow")
        turtle.pensize(2)
        turtle.shape("turtle")

        for rec_obj in list_rectangles:
            turtle.showturtle()
            turtle.penup()
            turtle.goto(rec_obj.x, rec_obj.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rec_obj.width)
                turtle.right(90)
                turtle.forward(rec_obj.height)
                turtle.right(90)
            turtle.hideturtle()

        for sq_obj in list_squares:
            turtle.showturtle()
            turtle.penup()
            turtle.goto(sq_obj.x, sq_obj.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(sq_obj.size)
                turtle.right(90)
            turtle.hideturtle()
        turtle.exitonclick()
