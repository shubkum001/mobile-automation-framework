from abc import ABC, abstractmethod
from framework.config.config import MobileConfig


class BaseMobileDriver(ABC):

    def __init__(self, config: MobileConfig):
        self.config = config

    @abstractmethod
    def create_driver(self):
        pass

# abc - Abstract Base Class.
#@abstractmethod - Every concrete mobile driver must provide its own implementation of create_driver() Android will implement it one way. iOS will implement it another way.That's abstraction.
