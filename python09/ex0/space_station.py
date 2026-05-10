from pydantic import BaseModel, Field

class SpaceStationModel(BaseModel):
        station_id: str = Field(min_len=3, max_len=10)
        name: str = Field(min_len=1, max_len=50)
        crew_size: int = Field(min_len=1, max_len=)


if __name__ == '__main__':
    
