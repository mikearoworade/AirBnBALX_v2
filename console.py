#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

def parse_value(value):
    """Parses a string value to appropriate Python type"""
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1].replace('_', ' ')
        return value
    if '.' in value:
        try:
            return float(value)
        except ValueError:
            return None
    try:
        return int(value)
    except ValueError:
        return None

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)"""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        for param in args[1:]:
            if '=' not in param:
                continue
            key, value = param.split('=', 1)
            parsed_val = parse_value(value)
            if parsed_val is not None:
                setattr(new_instance, key, parsed_val)

        # 🔍 Add this debug block
        # print("DEBUG - Instance values before save:")
        # print(new_instance.__dict__)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        all_objs = storage.all()
        obj_list = []

        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            for key, value in all_objs.items():
                if key.startswith(arg + '.'):
                    obj_list.append(str(value))
        else:
            for obj in all_objs.values():
                obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Convert to appropriate type
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            else:
                attr_value = float(attr_value)
        except ValueError:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Handle commands in the form <class name>.<command>(<args>)"""
        try:
            if "." in line and "(" in line and ")" in line:
                class_name, method_call = line.split(".", 1)
                command_name, args = method_call.split("(", 1)
                args = args.strip(")")

                if command_name == "all":
                    self.do_all(class_name)

                elif command_name == "count":
                    count = sum(1 for obj in storage.all().values()
                                if obj.__class__.__name__ == class_name)
                    print(count)

                elif command_name == "show":
                    self.do_show(f"{class_name} {args.strip('\"')}")

                elif command_name == "destroy":
                    self.do_destroy(f"{class_name} {args.strip('\"')}")

                elif command_name == "update":
                    import ast

                    parsed = args.split(", ", 1)
                    obj_id = parsed[0].strip("\"")

                    # Dictionary-based update
                    if len(parsed) > 1 and parsed[1].startswith("{") and parsed[1].endswith("}"):
                        attr_dict = ast.literal_eval(parsed[1])
                        for key, value in attr_dict.items():
                            self.do_update(f"{class_name} {obj_id} {key} {value}")
                    else:
                        # Handle update with single attribute
                        parsed_args = args.split(", ")
                        if len(parsed_args) == 3:
                            attr_name = parsed_args[1].strip("\"")
                            attr_value = parsed_args[2].strip("\"")
                            self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")
                else:
                    print(f"*** Unknown command: {line}")
            else:
                print(f"*** Unknown syntax: {line}")
        except Exception as e:
            print(f"*** Error: {e}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
