from typing import List
from pydantic import BaseModel


class Hour(BaseModel):
    datetime: str
    temp: float
    conditions: str
    icon: str


class WeatherData(BaseModel):
    datetime: str
    hours: List[Hour]
