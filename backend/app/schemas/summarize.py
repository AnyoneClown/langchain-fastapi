from pydantic import BaseModel


class TextSummarize(BaseModel):
    text : str | None = None
