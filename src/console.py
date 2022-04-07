from cmd import Cmd

from . import allowed_commands, BashExecutor
from .exceptions import CryptoException


class CRSConsole(Cmd):
    """
    Class of main console
    """
    prompt = "crsconsole> "
    intro = "Wellcome to CryptoSploit <3"

    def default(self, command: str) -> bool:
        try:
            command, args = self.parse_command(command)
            return command.exec(*args)
        except CryptoException as err:
            print(str(err))
            return False

    @staticmethod
    def parse_command(command: str) -> tuple:
        command, *args = command.split()
        if command not in allowed_commands.keys():
            return BashExecutor, [" ".join(([command] + args))]
        else:
            command = allowed_commands[command]
            return command, args