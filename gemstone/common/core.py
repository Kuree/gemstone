from abc import abstractmethod
from .configurable import Configurable, ConfigurationType
from ..generator.from_magma import FromMagma
from ..generator.generator import Generator
import magma
from typing import List, Union
import mantle


class Core(Generator):
    @abstractmethod
    def inputs(self):
        pass

    @abstractmethod
    def outputs(self):
        pass

    def features(self) -> List[Union["Core", "CoreFeature"]]:
        return [self]

    def configure_model(self, instr):
        pass

    def eval_model(self, **kargs):
        return {}


class ConfigurableCore(Core, Configurable):
    def __init__(self, config_addr_width, config_data_width):
        Core.__init__(self)
        Configurable.__init__(self, config_addr_width, config_data_width)

    @abstractmethod
    def get_config_bitstream(self, instr):
        pass

    @abstractmethod
    def instruction_type(self):
        pass


class CoreFeature(Generator):
    def __init__(self,
                 parent_core: "Core",
                 index: int):
        super().__init__()

        self.__index = index
        self.__parent = parent_core

    def name(self):
        return f"{self.__parent.name()}_FEATURE_{self.__index}"

    def parent(self):
        return self.__parent

    def index(self):
        return self.__index

    def configure_model(self, instr):
        pass

    def eval_model(self, **kargs):
        return {}
