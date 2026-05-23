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

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: dt = Field(default_factory=dt.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=3, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':

        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')

        high_rank = False
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                high_rank = True
        if not high_rank:
            raise ValueError(
                    'Mission must have at least '
                    'one Commander or Captain'
                    )

        if self.duration_days > 365:
            exp_crew = 0
            for member in self.crew:
                if member.years_experience > 4:
                    exp_crew += 1
            if exp_crew/len(self.crew) < 0.5:
                raise ValueError(
                        'Long missions (> 365 days) need'
                        ' 50% experienced crew (5+ years)'
                )
        inact_memb: list[CrewMember] = []
        for member in self.crew:
            if not member.is_active:
                inact_memb.append(member)
        if inact_memb:
            raise ValueError(
                    'All crew members must be active - '
                    f'the following member(s) is/are inactive:\n{inact_memb}'
                )
        return self


def print_mission(m: SpaceMission) -> None:

    print(f"Mission: {m.mission_name}")
    print(f"ID: {m.mission_id}")
    print(f"Destination: {m.destination}")
    print(f"Duration: {m.duration_days} days")
    print(f"Budget: ${m.budget_millions}M")  # TODO: print a single 0 for float
    print(f"Crew size: {len(m.crew)}")
    print("Crew members:")
    for memb in m.crew:
        print(
                f"- {memb.name} ({memb.rank.value})"
                f" - {memb.specialization}"
        )


def main() -> None:

    valid_mission = {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': '2024-10-01T00:00:00',
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'CM012',
                'name': 'Sarah Connor',
                'rank': 'commander',
                'age': 36,
                'specialization': 'Mission Command',
                'years_experience': 22,
                'is_active': True
            },
            {
                'member_id': 'CM013',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': 29,
                'specialization': 'Navigation',
                'years_experience': 20,
                'is_active': True
            },
            {
                'member_id': 'CM014',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': 44,
                'specialization': 'Engineering',
                'years_experience': 25,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2500
    }

    invalid_mission = {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Saturn Rings Research Mission',
        'destination': 'Saturn Rings',
        'launch_date': '2024-09-18T00:00:00',
        'duration_days': 602,
        'crew': [
            {
                'member_id': 'CM041',
                'name': 'William Davis',
                'rank': 'officer',
                'age': 35,
                'specialization': 'Medical Officer',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM042',
                'name': 'Sarah Smith',
                'rank': 'officer',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM043',
                'name': 'Elena Garcia',
                'rank': 'lieutenant',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM044',
                'name': 'Sofia Williams',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Systems Analysis',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'CM045',
                'name': 'Sarah Jones',
                'rank': 'lieutenant',
                'age': 25,
                'specialization': 'Maintenance',
                'years_experience': 11,
                'is_active': True
            },
            {
                'member_id': 'CM046',
                'name': 'Lisa Rodriguez',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Life Support',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM047',
                'name': 'Sarah Smith',
                'rank': 'cadet',
                'age': 28,
                'specialization': 'Pilot',
                'years_experience': 8,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 1092.6
    }

    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        # ** -> dict unpacking
        m1 = SpaceMission(**valid_mission)
        print_mission(m1)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        if 'ctx' in e_msg and 'error' in e_msg['ctx']:
            print(str(e_msg['ctx']['error']))
        else:
            print(e_msg['msg'])

    print("\n=========================================")

    try:
        m2 = SpaceMission(**invalid_mission)
        print_mission(m2)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        if 'ctx' in e_msg and 'error' in e_msg['ctx']:
            print(str(e_msg['ctx']['error']))
        else:
            print(e_msg['msg'])


if __name__ == '__main__':
    main()
