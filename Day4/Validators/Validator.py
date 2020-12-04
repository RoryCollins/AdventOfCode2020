from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return self.value is not None and self.additional_validation()

    @abstractmethod
    def additional_validation(self):
        return True
