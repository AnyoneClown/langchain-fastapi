from fastapi import APIRouter, Request

router = APIRouter()

g
@router.post("/summarize", summary="Return summary of text")
async def summarize(request: Request):
    return {"summary": "summary"}
