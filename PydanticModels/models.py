from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class PostParams(BaseModel):
    title: str
    content: str
    published: str

