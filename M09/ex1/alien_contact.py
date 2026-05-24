#!/usr/bin/env python3
from enum import Enum
from datetime import datetime as dt
from pydantic import (  # type: ignore
        BaseModel,
        Field,
        model_validator,
        ValidationError
        )


class ContactType(str, Enum):

    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: dt = Field(default_factory=dt.now)

    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: None | str = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contact_validator(self) -> 'AlienContact':

        if not self.contact_id.startswith('AC'):
            raise ValueError('Contact ID must start with "AC"')

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                    'Physical contact reports must be verified'
            )

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                    'Telepathic contact requires at least 3 witnesses'
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    'Strong signals (> 7.0) should include'
                    ' received messages'
            )
        return self


def print_contact(contact: AlienContact, extra: bool) -> None:

    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")
    else:
        print("Message: -")
    if extra:
        print("Verified contact: ", end="")
        if contact.is_verified:
            print("YES")
        else:
            print("NO")
        formatted = contact.timestamp.strftime("%B %d, %Y at %I:%M %p")
        print(f"Last contact at: {formatted}")


def main() -> None:

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    try:
        c1 = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print_contact(c1, False)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        if 'ctx' in e_msg and 'error' in e_msg['ctx']:
            print(str(e_msg['ctx']['error']))
        else:
            print(e_msg['msg'])

    print("\n======================================")

    try:
        c2 = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
        print_contact(c2, False)

    except ValidationError as e:
        e_msg = e.errors()[0]
        print("Expected validation error:")
        if 'ctx' in e_msg and 'error' in e_msg['ctx']:
            print(str(e_msg['ctx']['error']))
        else:
            print(e_msg['msg'])


#    print("\n======================================")
#    try:
#        c3 = AlienContact(
#            contact_id="AC_2025_001",
#            contact_type="telepathic",
#            location="The Amazon, Brazil",
#            signal_strength="8.5",
#            duration_minutes="45",
#            witness_count="15",
#            message_received="Bow to the great civilization of Ratanabá"
#        )
#        print_contact(c3, True)
#
#    except ValidationError as e:
#        e_msg = e.errors()[0]
#        print("Expected validation error:")
#        print(e_msg['msg'])


if __name__ == '__main__':
    main()
