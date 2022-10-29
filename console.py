#!/usr/bin/python3
''''''
import cmd


class HBNBCommand(cmd.Cmd):
    ''''''
    prompt = '(hbnb) '
    classes = ['BaseModel']
    storage = models.storage

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
            print("** class doesn't exist **")
            return (False)
        return (True)
        
    def check_id(self, arg):
        '''verify if arg in a class name
        '''
        dict1 = self.storage.all()
        ids = dict1.keys()
        if not arg:
            print("** instance id missing **")
            return (False)
        if arg not in ids:
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

    def do_show(self, *args):
        '''Prints the string representation of an
        instance based on the class name and id.
        '''
        if self.chek_class(agrs[0]):
            if self.check_id(args[1]):
                dict1 = self.storage.all()
                key = args[0] + "." + args[0]
                obj = dict1[key]
                print(obj)

    def do_destroy(self, *args):
        '''Deletes an instance based on the class
        name and id (save the change into the JSON file).
        '''
        if self.chek_class(agrs[0]):
            if self.check_id(args[1]):
                key = args[0] + "." + args[0]
                del self.storage.all().[key]
                storage.save()

    def do_all(self, *args):
        '''Prints all string representation of all
        instances based or not on the class name.
        '''
        obj = self.storage.all()
        if not args:
            for key in obj:
                print(obj[key])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in obj:
                keyname = str(key).split('.')
                if keyname[0] == args[0]:
                    print(obj[key])

    def do_update(self, *args):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        '''
        if self.chek_class(agrs[0]):
            if self.check_id(args[1]):
                key = args[0] + "." + args[0]
                if len(args) == 2:
                    print('** attribute name missing **')
                elif len(args) == 3:
                    print('** value missing **')
                else:
                    obj = self.storage.all()[key]
                    obj_dict = obj.to_dict()
                    if args[2] in obj_dict.keys():
                        setattr(obj, args[2], type(obj_dict[args[2]])(args[3]))
                    else:
                        setattr(obj, args[2], args[3])

            self.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
