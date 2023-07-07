import typing
from collections.abc import Mapping
from typing import Any
from urllib.parse import urljoin

import benedict
import requests

from owmapi.dto import WFData


class IResponse(typing.Protocol):
    def raise_for_status() -> None:
        ...

    def json() -> dict[str, Any]:
        ...


class IHTTPAgent(typing.Protocol):
    def get(url, params: dict[str, str]) -> IResponse:
        ...


class SimpleOWMApi:
    base_url: str = "https://api.openweathermap.org/data/2.5/"
    appid: str

    def __init__(self, appid: str, agent: IHTTPAgent = None):
        self.appid = appid
        self.agent = agent or requests

    @classmethod
    def _url(cls, endpoint: str) -> str:
        return urljoin(cls.base_url, endpoint)

    def _get(self, *, endpoint: str, **params) -> Mapping[str, Any]:
        try:
            response = self.agent.get(
                self._url(endpoint), params={"appid": self.appid, **params}
            )
            response.raise_for_status()
        except requests.HTTPError:
            raise
        else:
            return benedict.benedict(response.json())

    def forecast(self, *, lon, lat, units="metric") -> list[WFData]:
        data = self._get(endpoint="forecast", lon=lon, lat=lat, units=units)
        return WFData._from_owm(data)
