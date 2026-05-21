#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError  # type: ignore
from datetime import datetime


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    last_maintenance: datetime = Field(default_factory=datetime.now)

    is_operational: bool = Field(default=True)
    notes: None | str = Field(default=None, max_length=200)


def print_station(
        station: SpaceStation,
        maintenance: bool) -> None:

    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")

    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Out of service")

    if maintenance:
        formatted = station.last_maintenance.strftime("%B %d, %Y at %I:%M %p")
        print(f"Last maintenance done in {formatted}")

    if station.notes:
        print(f"Notes: {station.notes}")


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")

    # Create a valid station
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level="85.5",
            oxygen_level=92.3,
            is_operational=True,
            notes=None
        )
        print_station(valid_station, False)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        print(e_msg['msg'])

    print("\n========================================")

    # Create station with invalid crew size
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="National Space Station",
            crew_size=50,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            notes=None
        )
        print_station(invalid_station, False)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        print(e_msg['msg'])

    # print("\n========================================")

    # An extra station to print timestamp and notes
    # try:
    #    extra_station = SpaceStation(
    #        station_id="ISS005",
    #        name="Emergency Space Station",
    #        crew_size=15,
    #        power_level=0.0,
    #        oxygen_level=65.3,
    #        is_operational=False,
    #        notes=(
    #            "This station was created for emergency evacuation\n"
    #            "cenarios in case of nuclear disaster, it has been\n"
    #            "inactive since 1953.\nMaintenance is still"
    #            "done regularly for historical preservation motives"
    #            )
    #    )
        # print_station(extra_station, True)

    # except ValidationError as e:
    #    e_msg = e.errors()[0]
    #    print("Expected validation error:")
    #    print(e_msg['msg'])


if __name__ == '__main__':
    main()
