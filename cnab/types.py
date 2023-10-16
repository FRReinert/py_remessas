from dataclasses import dataclass
from re import sub
from uuid import UUID


@dataclass
class Document:
    document: str

    def __str__(self):
        doc = sub(r'\D', '', self.document)
        return doc.zfill(14)


@dataclass
class CnabDate:
    day: int
    month: int
    year: int
    ddmmaa: bool = False

    def __str__(self):
        if self.ddmmaa:
            return f"{self.day}{self.month}{str(self.year)[2:]}"
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


@dataclass
class CnabDateTime:
    day: int
    month: int
    year: int
    hour: int
    minute: int
    second: int

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"


@dataclass
class Guid:
    guid: str

    def is_valid(self) -> bool:
        try:
            obj = UUID(self.guid)
            return obj.version == 4
        except Exception:
            return False

    def __str__(self):
        return self.guid[:36]


@dataclass
class Money:
    value: int | float

    def __cents_from_float(self) -> int:
        str_value = str(self.value).split('.')
        return int(f"{str_value[0]}{str_value[1][:2]}")

    def __in_cents(self):
        return self.value if isinstance(self.value, int) else self.__cents_from_float()

    def __str__(self):
        return f"{self.__in_cents():015d}"
