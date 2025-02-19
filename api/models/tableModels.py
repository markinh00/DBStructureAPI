from pydantic import BaseModel


class CreateTableQuery(BaseModel):
    table: str
