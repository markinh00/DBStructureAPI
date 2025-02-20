from fastapi import APIRouter

from api.models.tableModels import CreateTableQuery
from api.services.mysql.getTables import getTables

router = APIRouter(
    prefix="/tables",
    tags=["tables"]
)

@router.post("/")
def create_table(table: CreateTableQuery):
    getTables()
    return {'message': 'success'}