#!/usr/bin/python3
"""Module console

This Module for HBNBCommand Class
"""

import cmd
import importlib
import json
import re
from typing import cast

from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB clone console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """prevents default behavior of cmd to ignore running command on
        empty line plus enter
        """
        pass

    def do_EOF(self, line):
        """Exist the console using Ctrl + D"""
        print()
        return True

    def do_create(self, line):
        """creates a new object and saves it"""
        class_obj = self.get_class_from_input(line)
        if class_obj is not None:
            object_new = class_obj()
            object_new.save()
            print(object_new.id)

    def do_show(self, line):
        """prints the string representation of an instance based on name and id
        """
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().get(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            print(saved_obj)

    def do_destroy(self, line):
        """deletes an instance based on the class name and id and saves the
        change into the JSON file
        """
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().pop(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            storage.save()

    def get_class(self, name):
        """ returns a class from models module using its name"""
        try:
            sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
            module = importlib.import_module(f"models.{sub_module}")
            return getattr(module, name)
        except Exception:
            print("** class doesn't exist **")
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
