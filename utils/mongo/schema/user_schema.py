from pydantic import BaseModel, Field

class User_schema(BaseModel):
    id: int=Field(...)                         # user id
    games_won:int=Field(...,ge=0)
    total_guesses:int=Field(...,ge=0)
    total_hints_used:int=Field(...,ge=0)
