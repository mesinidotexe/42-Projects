from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class Rank(Enum):

    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


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
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self):
        error = []
        in_charge = 0
        xp = 0
        if not self.mission_id.startswith('M'):
            error.append('Mission ID must start with "M"')

        for i, member in enumerate(self.crew):
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                in_charge += 1
            if i == len(self.crew) - 1 and not in_charge:
                error.append('Must Have one Commander or Captain')

        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    xp += 1
            if xp < len(self.crew) / 2:
                error.append('Long missions (> 365 dias) need '
                             '50\\% xp crew (5+years)')

        for member in self.crew:
            if not member.is_active:
                error.append('All crew must be active')
        if error:
            raise ValueError(error)
        return self


def main():

    print('Space Mission Crew Validation')
    print('=========================================')

    mission_crew = [
        CrewMember(
            member_id='000',
            name='Sarah Connor',
            rank=Rank.COMMANDER,
            age=67,
            specialization='Mission Command',
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id='001',
            name='John Smith',
            rank=Rank.LIEUTENANT,
            age=76,
            specialization='Navigation',
            years_experience=4,
            is_active=True
        ),
        CrewMember(
            member_id='002',
            name='Alice Johnson',
            rank=Rank.OFFICER,
            age=24,
            specialization='Engineering',
            years_experience=7,
            is_active=True
        )
    ]
    mission = SpaceMission(
        mission_name='Mars Colony Establishment',
        mission_id='M2024_MARS',
        destination='Mars',
        launch_date=datetime.now(),
        duration_days=900,
        budget_millions=2500.0,
        crew=mission_crew
    )
    print('Valid mission created:')
    print(f'Mission: {mission.mission_name}')
    print(f'ID: {mission.mission_id}')
    print(f'Destination: {mission.destination}')
    print(f'Duration: {mission.duration_days}')
    print(f'Crew size: {len(mission.crew)}')

    for member in mission.crew:
        print(f'{member.name} {member.rank} - {member.specialization}')

    try:
        sabor_mission_crew = [
            CrewMember(
                member_id='000',
                name='Sarah Connor',
                rank=Rank.CADET,
                age=67,
                specialization='Mission Command',
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id='001',
                name='John Smith',
                rank=Rank.LIEUTENANT,
                age=76,
                specialization='Navigation',
                years_experience=4,
                is_active=True
            ),
            CrewMember(
                member_id='002',
                name='Alice Johnson',
                rank=Rank.OFFICER,
                age=24,
                specialization='Engineering',
                years_experience=7,
                is_active=True
            )
        ]

        sabor_mission = SpaceMission(
            mission_name='Mars Colony Establishment',
            mission_id='M2024_MARS',
            destination='Mars',
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=sabor_mission_crew
        )
        print(sabor_mission.crew)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
