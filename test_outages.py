import unittest
from unittest.mock import patch, MagicMock

from endpoints import get_all_outages, get_site_info, update_outages, API_KEY


class OutageTests(unittest.TestCase):
    def test_get_all_outages(self):
        with patch("endpoints.requests.get") as mocked_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = [
                {
                    "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                    "begin": "2021-07-26T17:09:31.036Z",
                    "end": "2021-08-29T00:37:42.253Z",
                },
                {
                    "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                    "begin": "2022-05-23T12:21:27.377Z",
                    "end": "2022-11-13T02:16:38.905Z",
                },
                {
                    "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                    "begin": "2022-12-04T09:59:33.628Z",
                    "end": "2022-12-12T22:35:13.815Z",
                },
            ]
            mocked_get.return_value = mock_response

            outages = get_all_outages()

            self.assertEqual(outages, mock_response.json.return_value)

    def test_get_site_info(self):
        with patch("endpoints.requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = {
                "id": "kingfisher",
                "name": "KingFisher",
                "devices": [
                    {"id": "002b28fc-283c-47ec-9af2-ea287336dc1b", "name": "Battery 1"},
                    {"id": "086b0d53-b311-4441-aaf3-935646f03d4d", "name": "Battery 2"},
                ],
            }
            site_info = get_site_info("kingfisher")
            self.assertEqual(
                site_info,
                {
                    "id": "kingfisher",
                    "name": "KingFisher",
                    "devices": [
                        {
                            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                            "name": "Battery 1",
                        },
                        {
                            "id": "086b0d53-b311-4441-aaf3-935646f03d4d",
                            "name": "Battery 2",
                        },
                    ],
                },
            )

    def test_update_outages(self):
        with patch("endpoints.requests.post") as mocked_post:
            mocked_post.return_value.status_code = 200
            response = update_outages(
                "norwich-pear-tree",
                [
                    {
                        "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                        "name": "Battery 1",
                        "begin": "2022-05-23T12:21:27.377Z",
                        "end": "2022-11-13T02:16:38.905Z",
                    },
                    {
                        "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
                        "name": "Battery 1",
                        "begin": "2022-12-04T09:59:33.628Z",
                        "end": "2022-12-12T22:35:13.815Z",
                    },
                    {
                        "id": "086b0d53-b311-4441-aaf3-935646f03d4d",
                        "name": "Battery 2",
                        "begin": "2022-07-12T16:31:47.254Z",
                        "end": "2022-10-13T04:05:10.044Z",
                    },
                ],
            )
            mocked_post.assert_called_once_with(
                "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-outages/norwich-pear-tree",
                headers={"x-api-key": API_KEY},
                data='[{"id": "002b28fc-283c-47ec-9af2-ea287336dc1b", "name": "Battery 1", "begin": "2022-05-23T12:21:27.377Z", "end": "2022-11-13T02:16:38.905Z"}, {"id": "002b28fc-283c-47ec-9af2-ea287336dc1b", "name": "Battery 1", "begin": "2022-12-04T09:59:33.628Z", "end": "2022-12-12T22:35:13.815Z"}, {"id": "086b0d53-b311-4441-aaf3-935646f03d4d", "name": "Battery 2", "begin": "2022-07-12T16:31:47.254Z", "end": "2022-10-13T04:05:10.044Z"}]',
            )
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
