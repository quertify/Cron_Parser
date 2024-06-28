from abc import ABC, abstractmethod

class ICronValidator(ABC):
    @abstractmethod
    def validate(self, field, field_range):
        pass

class ICronParser(ABC):
    @abstractmethod
    def parse(self, expression):
        pass

class ICronScheduler(ABC):
    @abstractmethod
    def next_iterations(self, n, output, given_time):
        pass

class ICronPrinter(ABC):
    @abstractmethod
    def print_box(self, output):
        pass
