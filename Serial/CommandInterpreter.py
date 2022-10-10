#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger
#

from Serial.SerialManager import SerialManager
from Serial.Stack import Stack
from Serial.SerialStates import SerialStates, compare


class CommandInterpreter:
    serial: SerialManager
    stack: Stack
    executing: bool = False

    def __init__(self, port):
        self.serial = SerialManager(port)
        self.serial.onMessage = self.handle_message
        self.command_to_execute = []

    def execute_command(self, command_generator):
        self.stack.append(command_generator)
        if not (self.executing and self.stack.is_empty):
            next(self.stack.pop_first())
            self.executing = True
        pass

    def handle_message(self, data):
        msg = convertMessage(data)
        if msg == SerialStates.END:
            return self.__handle_end()

        pass

    def __handle_end(self):
        if self.stack.is_empty:
            self.executing = False
    pass


def convertMessage(msg: str):
    return int(msg[0:len(msg)-2])
