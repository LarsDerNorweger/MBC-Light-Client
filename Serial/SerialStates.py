#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger
#

from enum import Enum


class SerialStates(Enum):

    END = 1024

    UNKOWN_ERROR = 2048
    ARGUMENT_ERROR = 2049

    NEXT = 4096

    def __eq__(self, o):
        if type(o) is SerialStates:
            return self is o
        return self.value == o
    pass
