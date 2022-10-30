#!/usr/bin/python3
''''''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''''''
    prompt = '(hbnb) '
    classes = ['BaseModel']

    #def do_help(self, arg):
     #   '''get all commandes
      #  '''

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        exit()

    def do_EOF(self, arg):
        '''EOF command to exit the program
        '''
        exit()

    def emptyline(self):
        '''to do not execute last command while prompt and empty line
        '''
        pass

    def check_class(self, arg):
        '''verify if arg in a class name
        '''
        if not arg:
            print('** class name missing **')
            return (False)
        elif arg not in self.classes:
            print(arg)
            print("** class doesn't exist **")
            return (False)
        return (True)
        
    def check_id(self, arg):
        '''verify if arg in a class name
        '''
        dict1 = storage.all()
        ids = dict1.keys()
        if not arg:
            print("** instance id missing **")
            return (False)
        if arg not in ids:
            print(arg)
            print('** no instance found **')
            return (False)
        return (True)

    def do_create(self, arg):
        '''create a new instance of BaseModel
        Args:
            arg (class): class name
        '''
        if self.check_class(arg):
            base = BaseModel()
            base.save()
            print('{}'.format(base.id))

    def do_show(self, arg):
        '''Prints the string representation of an
        instance based on the class name and id.
        '''
        args = arg.split(' ')
        if self.check_class(args[0]):
            if len(args) == 2:
                dict1 = storage.all()
                key = args[0] + "." + args[1]
                if key in dict1.keys():
                    obj = dict1[key]
                    print(obj)
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')

    def do_destroy(self, arg):
        '''Deletes an instance based on the class
        name and id (save the change into the JSON file).
        '''
        args = arg.split(' ')
        if self.check_class(args[0]):
            if len(args) >= 2 and self.check_id(args[0] + "." + args[1]):
                key = args[0] + "." + args[1]
                objs = storage.all()
                del objs[key]
                storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name.
        '''
        args = arg.split(' ')
        obj = storage.all()
        if not arg:
            for key in obj:
                print(obj[key])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            tmp1 = {}
            for key in obj:
                keyname = str(key).split('.')
                if keyname[0] == args[0]:
                    tmp1[key] = obj[key]
            tmp = tmp1.values()
            print([str(i) for i in tmp])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        '''
        args = arg.split(' ')
        if self.check_class(args[0]):
            if len(args) >= 2 and self.check_id(args[0] + "." + args[1]):
                key = args[0] + "." + args[1]
                if len(args) == 2:
                    print('** attribute name missing **')
                elif len(args) == 3:
                    print('** value missing **')
                else:
                    obj = storage.all()[key]
                    obj_dict = obj.to_dict()
                    if args[2] in obj_dict.keys():
                        setattr(obj, args[2], type(obj_dict[args[2]])(args[3]))
                    else:
                        setattr(obj, args[2], args[3])

            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
