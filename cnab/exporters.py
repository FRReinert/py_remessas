from io import StringIO
from typing import Generator
from cnab.interfaces import ICnabFactory, ICnabLine


class StreamSyncExporter(ICnabFactory):
    @staticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
        iostream: StringIO | None = None,
    ) -> StringIO:
        if not iostream:
            iostream = StringIO()
        iostream.write(header_factory.make_line() + '\n')
        for contract in contracts:
            iostream.write(contract.make_line() + '\n')
        iostream.write(trail_factory.make_line() + '\n')
        return iostream


class GeneratorExporter(ICnabFactory):
    @staticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
    ) -> Generator[str, any, None]:
        yield header_factory.make_line()
        for contract in contracts:
            yield contract.make_line()
        yield trail_factory.make_line()


class FileExporter(ICnabFactory):
    @staticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
        file_path: str,
    ) -> None:
        with open(file_path, "w") as fopen:
            fopen.write(header_factory.make_line() + '\n')
            for contract in contracts:
                fopen.write(contract.make_line() + '\n')
            fopen.write(trail_factory.make_line() + '\n')
