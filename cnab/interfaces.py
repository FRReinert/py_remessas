from abc import ABC, abstractmethod, abstractstaticmethod


class ICnabLine(ABC):
    """Cnab Line generator Interface"""

    @abstractmethod
    def make_line() -> str:  # pragma: no cover
        pass


class ICnabTrail(ABC):
    """Cnab Trail Interface"""

    contract_amount: int

    @abstractmethod
    def make_line(self) -> str:  # pragma: no cover
        pass


class ICnabName(ABC):
    """Cnab Name provider Interface"""

    @abstractmethod
    def make_name(self) -> str:  # pragma: no cover
        pass


class ICnabFactory(ABC):
    @staticmethod
    @abstractstaticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabTrail,
        contracts: list[ICnabLine],
    ):  # pragma: no cover
        pass
