from fastapi import APIRouter
from api.models.tableModels import TableModel
from api.services.mysql.getTables import getTables
import pandas as pd


router = APIRouter(
    prefix="/tables",
    tags=["tables"]
)

@router.get("/")
def get_table() -> list[TableModel]:
    result = getTables()

    for table in result:
        print(f"\nTabela: {table.table_name}")
        df = pd.DataFrame(table.model_dump()["columns"])
        print(df.to_string(index=False))

    return result
