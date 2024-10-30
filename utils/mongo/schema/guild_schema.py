from pydantic import BaseModel, Field
from utils.constants import MAX_GAME_NUMBER,MIN_GAME_NUMBER

# Define a schema using Pydantic
class Guild_schema(BaseModel):
    id: int=Field(...)     # guild id
    current_game_no:int=Field(...,ge=MIN_GAME_NUMBER,le=MAX_GAME_NUMBER)
    games_completed:int=Field(...,ge=0)