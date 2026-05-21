#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime as dt
from enum import Enum


class Rank(str, Enum):
    
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    
    member_id: str = Field(min_length=3, max_length=10) #3-10 characters
    name: str = Field(min_length=2, max_length=50) # , 2-50 characters
    rank: Rank
    age: int = Field(ge=18, le=80)# Integer, 18-80 years
    specialization: str = Field(min_length=3, max_length=30)# String, 3-30 characters
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True) # Boolean, defaults to True


class SpaceMission(BaseModel): 
    
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: dt = Field(default_factory=dt.now)
    duration_days: int = Field(ge=1, le=3650) # 1-3650 days (max 10 years)
    crew: list[CrewMember] = Field(min_length=5, max_length=12)
    mission_status: str = Field(default="planned") # String, defaults to "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0) #  1.0-10000.0

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        
        if not self.mission_id.startswith('M'):
             raise ValueError('Mission ID must start with "M"')
        
        high_rank = False
        for member in crew:   
            if member == Rank.CAPITAIN or member == Rank.COMMANDER:
                high_rank = True
        if not high_rank:
            raise ValueError('Must have at least one Commander or Captain')

        if duration_days > 365:
    # Long missions (> 365 days) need 50% experienced crew (5+ years)
    # All crew members must be active
