from abc import ABC, abstractmethod, abstractstaticmethod


class ICnabLine(ABC):
    """Cnab Line generator Interface"""

    @abstractmethod
    def make_line() -> str:
        pass


class ICnabName(ABC):
    """Cnab Name provider Interface"""

    @abstractmethod
    def make_name(self):
        pass


class ICnabFactory(ABC):
    @staticmethod
    @abstractstaticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
    ):
        pass
