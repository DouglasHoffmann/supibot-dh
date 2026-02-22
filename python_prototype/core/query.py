from typing import Any, Callable, List, Optional, TypeVar, Generic

T = TypeVar("T")

class RecordsetBuilder:
    def __init__(self):
        self._select = "*"
        self._from = ""
        self._where = []
        self._limit = None
        self._flat_col = None
        self._single = False

    def select(self, *args):
        self._select = ", ".join(args)
        return self

    def from_(self, schema: str, table: str):
        self._from = f"{schema}.{table}"
        return self

    def where(self, condition: str, *args):
        self._where.append((condition, args))
        return self

    def limit(self, n: int):
        self._limit = n
        return self

    def flat(self, col: str):
        self._flat_col = col
        return self

    def single(self):
        self._single = True
        return self

class Query:
    @staticmethod
    async def get_recordset(builder_fn: Callable[[RecordsetBuilder], RecordsetBuilder]):
        builder = builder_fn(RecordsetBuilder())
        # Mocking DB response
        print(f"DEBUG: Executing Query -> SELECT {builder._select} FROM {builder._from}")
        return []

    @staticmethod
    async def get_row(schema: str, table: str):
        print(f"DEBUG: Getting row from {schema}.{table}")
        return MockRow()

class MockRow:
    def __init__(self):
        self.values = {}

    async def load(self, id_val: Any):
        pass

    async def save(self):
        pass

query = Query()
