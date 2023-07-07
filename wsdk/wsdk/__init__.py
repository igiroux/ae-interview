from urllib.parse import urljoin
from owmapi.dto import Station, WFData

import requests


class WXplorerSDK:
    base_url = "http://localhost:8000/"

    @classmethod
    def _url(cls, endpoint: str) -> str:
        return urljoin(cls.base_url, endpoint)

    @staticmethod
    def _method(meth: str, *args, **kwargs):
        func = getattr(requests, meth)
        resp = func(*args, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint, data):
        return self._method("post", self._url(endpoint), json=data)

    def get(self, endpoint):
        return self._method("get", self._url(endpoint))

    def list_stations(self):
        return [Station(**s) for s in self.get("/stations/")]

    def get_station_weather(self):
        return self.get("/weather/")

    def register_stations(self, stations: list[Station]):
        for s in stations:
            try:
                self.post("/stations/", data=s._asdict())
            except requests.HTTPError as e:
                print(f"Station registering {s.name} failed.\n{e}")

    def save_station_forecast(self, s: Station, wdata: list[WFData]):
        print(f"Handling staton {s.name}")
        for forecast in wdata:
            try:
                self.post(
                    "/weather/", data={"station": s.station_id, **forecast._asdict()}
                )
            except requests.HTTPError as e:
                print(
                    f"Failed to register forecast for station {s.name}.\n"
                    f"(forecast_time: {forecast.forecast_time}). \n{e}"
                )
