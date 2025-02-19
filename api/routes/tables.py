from fastapi import APIRouter

router = APIRouter(
    prefix="/tables",
    tags=["tables"]
)

@router.post("/")
def create_table(table: str):
    pass