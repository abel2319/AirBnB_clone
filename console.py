#!/usr/bin/python3
''''''
import cmd


class HBNBCommand(cmd.Cmd):
    ''''''
    prompt = '(hbnb) '

    #def do_help(self, arg):
     #   '''get all commandes
      #  '''
       # self.help()

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
