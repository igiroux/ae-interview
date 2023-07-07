import dataclasses
import enum
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Union

import benedict
import pandas as pd


@dataclasses.dataclass
class WFField:
    field_path: str
    factory: Callable[[Any], Any] = lambda x: x


class WFFields(WFField, enum.Enum):
    forecast_time = ("dt", datetime.utcfromtimestamp)
    temperature = ("main.temp", float)
    humidity = ("main.humidity", int)
    cloudiness = ("clouds.all", int)


@dataclasses.dataclass
class WFData:
    forecast_time: datetime
    temperature: float
    humidity: int
    cloudiness: int

    def _asdict(self):
        data = dataclasses.asdict(self)
        data["forecast_time"] = self.forecast_time.astimezone().isoformat()
        return data

    @classmethod
    def _from_owm(cls, owm_resp: benedict.benedict) -> list["WFData"]:
        return [
            cls(
                **{
                    field.name: field.factory(row[field.field_path])
                    for field in WFFields
                }
            )
            for row in owm_resp["list"]
        ]


@dataclasses.dataclass
class Station:
    station_id: int
    name: str
    latitude: str
    longitude: str
    altitude: str

    def _asdict(self):
        return dataclasses.asdict(self)

    @staticmethod
    def from_csv(path: Union[str, Path]) -> list["Station"]:
        return [Station(*row) for row in pd.read_csv(path).values.tolist()]
