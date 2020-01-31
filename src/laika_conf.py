from dataclasses import dataclass
from typing import Tuple, List
from csv import DictReader


@dataclass
class LaikaProbe:
    id_: str
    desc: str
    latitude: float
    longitude: float
    online: bool = True

    @property
    def coordinates(self) -> Tuple:
        """
        Return the coordinates of the LaikaProbe
        :return:
        """
        return self.latitude, self.longitude

    def __repr__(self):
        return f"{self.id_} is {'online' if self.online else 'offline'} at {self.coordinates}"


def get_probes(file_name: str) -> List[LaikaProbe]:
    with open(file_name, newline='') as file_:
        reader = DictReader(file_)
        probes = [LaikaProbe(id_=row['ID'], desc=row['Description'],
                             latitude=row['Latitude'], longitude=row['Longitude']) for row in reader]
    return probes


if __name__ == "__main__":
    probes = get_probes('data/laika_config.csv')
    for probe in probes:
        print(probe)