import requests


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path.cwd()))
from env_setup import API_KEY


class HolidayAPI:
    def __init__(self):
        self.base_url = "https://holidayapi.com/"

    def get_holidays(
        self,
        country: str,
        year: int = None,
        month: int = None,
        day: int = None,
        public: bool = None,
        subdivision: bool = None,
        search: str = None,
        language: str = None,
        previous: bool = None,
        upcoming: bool = None,
        format: str = None,
        pretty: bool = None,
    ) -> requests.Response:
        api = "v1/holidays"
        method = "GET"
        params = {
            "year": year,
            "country": country,
            "month": month,
            "day": day,
            "public": public,
            "subdivision": subdivision,
            "search": search,
            "language": language,
            "previous": previous,
            "upcoming": upcoming,
            "format": format,
            "pretty": pretty,
            "key": API_KEY,
        }
        url = f"{self.base_url}{api}"
        response = requests.request(method, url, params=params)
        return response

    def get_countries(
        self, country=None, search=None, public=None, format=None, pretty: bool = None
    ) -> requests.Response:
        api = "v1/countries"
        method = "GET"
        params = {
            "country": country,
            "search": search,
            "public": public,
            "format": format,
            "pretty": pretty,
            "key": API_KEY,
        }
        url = f"{self.base_url}{api}"
        response = requests.request(method, url, params=params)
        return response


if __name__ == "__main__":
    holiday = HolidayAPI()
    print(holiday.get_holidays(2024, month=10, day=10))
