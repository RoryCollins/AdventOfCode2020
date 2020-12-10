from abc import ABC, abstractmethod


class ValidatorBase(ABC):
    def is_valid(self, value):
        return value is not None and self.additional_validation(value)

    @staticmethod
    @abstractmethod
    def additional_validation(value):
        return False
