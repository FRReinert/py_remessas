# Python Factory for CNAB 400
Generate CNAB 400 files

## Support
- Contracts
- Data for liquitation
- Receivable Units

## Development and Test
to either develop or test the library please install pipenv and run

```sh
pipenv run shell
pipenv install
```

to run tests in Linux\WSL\OSX run the following command in the root folder
```sh
make test
```

## Validation
You can use the following links to test files:

https://wspf.bradesco.com.br/wsValidadorTeleBanco/ValidadorRemessa.aspx

https://wspf.banco.bradesco/wsValidadorUniversal/validadorgeral

## Basic usage

```python
from io import SringIO

from cnab.cnab import CnabHeader, CnabReceivableUnitData, CnabTrail
from cnab.enums import EArrangement
from cnab.exporters import FileExporter
from cnab.types import CnabDate, Document, Guid, Money

# Create properties
unique_id = Guid("12345678-1234-1234-1234-123456789abc")
contract_key = Guid("12345678-1234-1234-1234-123456789abc")
receivable_unit_key = Guid("12345678-1234-1234-1234-123456789abc")
customer_document = Document("11111111111")
transferror_document = Document("11111111111")
accreditor_document = Document("11111111111")
holder_document = Document("11111111111")
arrengement_code = EArrangement.AMEX_CREDIT_CARD
date_liquidation = CnabDate(1, 12, 2022)  # 1/12/2022
receivable_unit_value = Money(1000)  # R$ 10,00
commited_contract_value = Money(1000)  # R$ 10,00
contract_priority = 1

# Instantiate Header factory
header = CnabHeader(customer_document, unique_id)

# Instantiate Trail Factory
trail = CnabTrail(1)

# Instantiate Record Factory with properties
contract_one = CnabReceivableUnitData(
    contract_key=contract_key,
    receivable_unit_key=receivable_unit_key,
    transferror_document=transferror_document,
    accreditor_document=accreditor_document,
    holder_document=holder_document,
    arrengement_code=arrengement_code,
    date_liquidation=date_liquidation,
    receivable_unit_value=receivable_unit_value,
    commited_contract_value=commited_contract_value,
    contract_priority=contract_priority,
)

# You can export the content using one of the exporters
# provided by the library or create your own

# Export to file
FileExporter.export(header, trail, [contract_one], "./")

# Return a Generator for further usage
GeneratorExporter.export(header, trail, [contract_one])

# Attach content to a pre declared StringIO
iostream = StringIO()
StreamSyncExporter.export(header, trail, [contract_one], iostream)

# Return a fresh StringIO instance
StreamSyncExporter.export(header, trail, [contract_one])
```

## Building you own Exporter

```python
from socket import socket, AF_INET, SOCK_STREAM

from cnab.cnab import CnabHeader, CnabReceivableUnitData, CnabTrail
from cnab.interfaces import ICnabFactory

# Create your own exporter by using the ICnabFactory interface
# in this (untested) example we can generate the CNAB content
# and send to a socket server

class SocketExporter(ICnabFactory):

    @staticmethod
    def export(
        header_factory: ICnabLine,
        trail_factory: ICnabLine,
        contracts: list[ICnabLine],
        host: str,
        port: int
    ):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.send(header_factory.make_line())
            
            for contract in contracts:
                sock.send(contract.make_line())
            
            sock.send(trail_factory.make_line())


# Example of exporter usage
header = CnabHeader(...)
trail = CnabTrail(...)
contract_one = CnabReceivableUnitData(...)
SocketExporter.export(header, trail, [contract_one], "127.0.0.1", 8080)
```