import unittest
from unittest import TestCase
import pytest
import requests
from main import geo_logs_russia, unic_id, stats_max


class TestGeoLogs(TestCase):
    def test_is_list(self):
        result = geo_logs_russia()
        self.assertIsInstance(result, list)

    def test_russia(self):
        result = geo_logs_russia()
        self.assertEqual(set([j[1] for i in result for j in i.values()]), {'Россия'})


class TestUnicId(TestCase):
    def test_lenght_unical_ids(self):
        result = unic_id()
        self.assertEqual(len(result), 6)

    @unittest.expectedFailure
    def test_not_float_list(self):
        # не дробные числа
        result = unic_id()
        assert all([isinstance(n, float) for n in result])


class TestMaxStats(TestCase):
    def test_max_stats(self):
        result = stats_max()
        self.assertEqual(result.get('yandex'), 120)


# @pytest.mark.parametrize('str_lst', [
#     ['5.3', '10', 'девять', '20', '500'],
#     ['пять', '-1', '-13', '7', '3.9', '4'],
#     ['5ять', '15', '6.3', '2,0', 'два', '9']
# ])

@pytest.mark.parametrize('str_lst', unic_id())
class TestUnicNumbers:
    def test_is_list(self, str_lst):
        # список
        result = unic_id()
        assert isinstance(result, list)

    def test_int_in_list(self, str_lst):
        # только целые числа
        result = unic_id()
        assert all([isinstance(n, int) for n in result])

    def test_15_213(self, str_lst):
        # в диапазоне от 15 до 213
        result = unic_id()
        assert all([15 <= n <= 213 for n in result])


def create_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    TOKEN = ''
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    response = requests.put(f'{url}?path={path}', headers=headers)
    res = requests.get(f'{url}?path={path}', headers=headers)
    return res


class TestCreateYaFolder(TestCase):
    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_response200(self):
        assert create_folder('hello world').status_code == 200

    def test_folder_exists(self):
        assert create_folder('hello world').json().get('name') == 'hello world'

    @unittest.expectedFailure
    def test_error(self):
        assert create_folder('hello world').json().get('error') == 'DiskPathPointsToExistentDirectoryError'


if __name__ == '__main__':
    create_folder('hello world')
