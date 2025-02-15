if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path.cwd()))

from frontend.holidayapi import HolidayAPI
import pytest

# assert_exsample
national_day_tw = {
    "name": "National Day",
    "date": "2024-10-10",
    "observed": "2024-10-10",
    "public": True,
    "country": "TW",
    "uuid": "e2d66412-7d41-40f3-a41a-69d32b3a15a8",
    "weekday": {"date": {"name": "Thursday", "numeric": "4"}, "observed": {"name": "Thursday", "numeric": "4"}},
}

TW_country = {
    "code": "TW",
    "name": "Taiwan",
    "codes": {"alpha-2": "TW", "alpha-3": "TWN", "numeric": "158"},
    "languages": ["zh"],
    "currencies": [{"alpha": "TWD"}],
    "flag": "https://flagsapi.com/TW/flat/64.png",
    "subdivisions": [
        {"code": "TW-CHA", "name": "Changhua", "languages": ["zh"]},
        {"code": "TW-CYI", "name": "Chiayi", "languages": ["zh"]},
        {"code": "TW-CYQ", "name": "Chiayi", "languages": ["zh"]},
        {"code": "TW-HSQ", "name": "Hsinchu", "languages": ["zh"]},
        {"code": "TW-HSZ", "name": "Hsinchu", "languages": ["zh"]},
        {"code": "TW-HUA", "name": "Hualien", "languages": ["zh"]},
        {"code": "TW-ILA", "name": "Yilan", "languages": ["zh"]},
        {"code": "TW-KEE", "name": "Keelung", "languages": ["zh"]},
        {"code": "TW-KHH", "name": "Kaohsiung", "languages": ["zh"]},
        {"code": "TW-KIN", "name": "Kinmen", "languages": ["zh"]},
        {"code": "TW-LIE", "name": "Lienchiang", "languages": ["zh"]},
        {"code": "TW-MIA", "name": "Miaoli", "languages": ["zh"]},
        {"code": "TW-NAN", "name": "Nantou", "languages": ["zh"]},
        {"code": "TW-NWT", "name": "New Taipei", "languages": ["zh"]},
        {"code": "TW-PEN", "name": "Penghu", "languages": ["zh"]},
        {"code": "TW-PIF", "name": "Pingtung", "languages": ["zh"]},
        {"code": "TW-TAO", "name": "Taoyuan", "languages": ["zh"]},
        {"code": "TW-TNN", "name": "Tainan", "languages": ["zh"]},
        {"code": "TW-TPE", "name": "Taipei", "languages": ["zh"]},
        {"code": "TW-TTT", "name": "Taitung", "languages": ["zh"]},
        {"code": "TW-TXG", "name": "Taichung", "languages": ["zh"]},
        {"code": "TW-YUN", "name": "Yunlin", "languages": ["zh"]},
    ],
    "weekend": [{"name": "Saturday", "numeric": 6}, {"name": "Sunday", "numeric": 7}],
}


@pytest.fixture(scope="class")
def holidaysApi():
    return HolidayAPI()


class Test_HolidayAPI:

    @pytest.mark.parametrize(
        "country,year,month,day,public,subdivision,search,language,previous,upcoming,format,pretty ,error_code,expected_len, expected_result",
        [
            # test tw national day
            ("TW", 2024, 10, 10, None, None, None, None, None, None, None, None, 200, 1, [national_day_tw]),
            # test us work day
            ("US", 2024, 10, 10, None, None, None, None, None, None, None, None, 200, 0, []),
            # test wrong country
            ("Wakanda", 2024, 4, 1, None, None, None, None, None, None, None, None, 400, 0, []),
            # previous cant be with upcoming
            ("TW", 2024, 10, 10, None, None, None, None, True, True, None, None, 400, 0, []),
            # search holiday
            (
                "TW",
                2024,
                None,
                None,
                None,
                None,
                "National Day",
                None,
                None,
                None,
                None,
                None,
                200,
                1,
                [national_day_tw],
            ),
            # test previous function
            ("TW", 2024, 10, 11, None, None, None, None, True, None, None, None, 200, 1, [national_day_tw]),
            # test upcoming function
            ("TW", 2024, 10, 9, None, None, None, None, None, True, None, None, 200, 1, [national_day_tw]),
        ],
    )
    def test_get_holidays(
        self,
        holidaysApi: HolidayAPI,
        country,
        year,
        month,
        day,
        public,
        subdivision,
        search,
        language,
        previous,
        upcoming,
        format,
        pretty,
        error_code,
        expected_len,
        expected_result,
    ):
        """check holiday api respond correct"""
        respond = holidaysApi.get_holidays(
            country=country,
            year=year,
            month=month,
            day=day,
            public=public,
            subdivision=subdivision,
            search=search,
            language=language,
            previous=previous,
            upcoming=upcoming,
            format=format,
            pretty=pretty,
        )
        assert respond.status_code == error_code
        if error_code == 200:
            assert len(respond.json()["holidays"]) == expected_len
            assert respond.json()["holidays"] == expected_result

    @pytest.mark.parametrize(
        "country,search,public,format,pretty ,error_code,expected_len, expected_result",
        [
            # test normal use
            ("TW", None, None, None, None, 200, 1, [TW_country]),
            # test wrong country
            ("Wakanda", None, None, None, None, 200, 0, []),
            # test search
            (None, "Taiwan", None, None, None, 200, 1, [TW_country]),
        ],
    )
    def test_get_countries(
        self,
        holidaysApi: HolidayAPI,
        country,
        search,
        public,
        format,
        pretty,
        error_code,
        expected_len,
        expected_result,
    ):
        respond = holidaysApi.get_countries(country=country, search=search, public=public, format=format, pretty=pretty)

        assert respond.status_code == error_code
        if error_code == 200:
            assert len(respond.json()["countries"]) == expected_len
            assert respond.json()["countries"] == expected_result
