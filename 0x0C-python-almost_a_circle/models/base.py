#!/usr/bin/python3
"""Defines the Base class"""
import json
import csv
import turtle
import tkinter


class Base:
    """A base class for the models package"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializates the Base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Transforms a dictionary representation to a JSON string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to a file"""
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as save:
            element_list = []
            if list_objs is not None:
                for element in list_objs:
                    element_list.append(cls.to_dictionary(element))
            save.write(cls.to_json_string(element_list))

    @staticmethod
    def from_json_string(json_string):
        """Transforms a JSON string to a list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            instance = cls(1, 1)
        if cls.__name__ is "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        obj_list = []
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as load:
                load_str = load.read()
                load_list = cls.from_json_string(load_str)
                for element in load_list:
                    obj_list.append(cls.create(**element))
            return obj_list
        except:
            return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the CSV representation of the list of objects"""
        with open(cls.__name__ + ".csv", mode="w", newline="") as save:
            if cls.__name__ is "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            if cls.__name__ is "Square":
                fieldnames = ["id", "size", "x", "y"]
            save_str = csv.DictWriter(save, fieldnames=fieldnames)
            for element in list_objs:
                save_str.writerow(cls.to_dictionary(element))

    @classmethod
    def load_from_file_csv(cls):
        """Loads the list of objects from a CSV file"""
        objs_list = []
        with open(cls.__name__ + ".csv", newline="") as load:
            if cls.__name__ is "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            if cls.__name__ is "Square":
                fieldnames = ["id", "size", "x", "y"]
            load_str = csv.DictReader(load, fieldnames=fieldnames)
            for element in load_str:
                for key in element:
                    element[key] = int(element[key])
                objs_list.append(cls.create(**element))
        return objs_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all rectangles and squares given in the lists"""
        root = tkinter.Tk()
        myCanvas = tkinter.Canvas(root, bg="white", height=768, width=1024)
        t = turtle.RawTurtle(myCanvas)
        colors = ["blue", "red", "green", "purple", "pink", "brown",
                  "lightblue", "yellow", "orange", "grey", "black"]
        i = 0
        t.shape("turtle")
        t.penup()
        t.setpos(-500, 300)
        for rectangle in list_rectangles:
            t.pencolor(colors[i % len(colors)])
            t.fillcolor(colors[i % len(colors)])
            i += 1
            t.forward(rectangle.x)
            t.right(90)
            t.forward(rectangle.y)
            t.left(90)
            t.pendown()
            for a in range(2):
                t.forward(rectangle.width)
                t.right(90)
                t.forward(rectangle.height)
                t.right(90)
            t.penup()
            t.backward(rectangle.x)
            t.right(90)
            t.forward(rectangle.height + 1)
            t.left(90)
        for square in list_squares:
            t.pencolor(colors[i % len(colors)])
            t.fillcolor(colors[i % len(colors)])
            i += 1
            t.forward(square.x)
            t.right(90)
            t.forward(square.y)
            t.left(90)
            t.pendown()
            for a in range(4):
                t.forward(square.size)
                t.right(90)
            t.penup()
            t.backward(square.x)
            t.right(90)
            t.forward(square.size + 1)
            t.left(90)
        myCanvas.pack()
        root.mainloop()
