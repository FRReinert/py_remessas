from abc import ABC, abstractmethod, abstractstaticmethod


class ICnabLine(ABC):
    """Cnab Line generator Interface"""

    @abstractmethod
    def make_line() -> str:
        raise NotImplementedError()


class ICnabFactory(ABC):
    @staticmethod
    @abstractstaticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
    ):
        raise NotImplementedError()
