from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):

    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    time_stamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1400)
    witnesses_count: int = Field(ge=1, le=100)
    message_recieved: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> 'AlienContact':
        errors = []
        if not self.contact_id.startswith('AC'):
            errors.append('contact_id must start with "AC"')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errors.append('Physical contact reports must be verified')
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witnesses_count < 3:
                errors.append('Telepathic contact requires at least 3 witnesses')
        if self.signal_strength > 7.0 and self.message_recieved is None:
            errors.append('Strong signals (>7.0) should include received messages')
        if errors:
            raise ValueError(errors)
        return self


def main() -> None:
    print('ALien Contact Log Validation')
    valid = AlienContact(
        contact_id='AC_2024_001',
        time_stamp=datetime.now(),
        location='Area 51, Nevada',
        contact_type='radio',
        signal_strength=8.5,
        duration_minutes=45,
        witnesses_count=5,
        message_recieved='Greetings from Zeta Reticuli',
        is_verified=True
    )
    print('=======================================')
    print('Valid contact report:')
    print(f'ID: {valid.contact_id}')
    print(f'Type: {valid.contact_type}')
    print(f'Location: {valid.location}')
    print(f'Signal: {valid.signal_strength}/10')
    print(f'Duration: {valid.duration_minutes} minutes')
    print(f'Witnesses: {valid.witnesses_count}')
    print(f'Message: {valid.message_recieved}')

    print('=======================================')
    try:
        invalid = AlienContact(
            contact_id='AC_2024_001',
            time_stamp=datetime.now(),
            location='Area 51, Nevada',
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witnesses_count=2,
            message_recieved='Greetings from Zeta Reticuli',
            is_verified=True
        )
        if invalid.is_verified:
            print('Verified')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
