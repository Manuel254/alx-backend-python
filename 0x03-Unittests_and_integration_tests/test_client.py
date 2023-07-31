#!/usr/bin/env python3
"""This module handles client testing"""
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """A class that tests the Github organizations client"""
    @parameterized.expand([
        ("google", ),
        ("abc", )
    ])
    @patch('client.get_json')
    def test_org(self, text, mock_get_json):
        """Test org method"""
        obj = GithubOrgClient(text)
        obj.org.return_value = mock_get_json
        mock_get_json.assert_called_once_with(obj.ORG_URL.format(org=text))

    def test_public_repos_url(self):
        """Tests the _public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_org:
            url = "https://api.github.com/orgs/google/repos"
            mock_org.return_value = { 
                    "repos_url": url
            }
            self.assertEqual(
                    GithubOrgClient('google')._public_repos_url, url
            )
    """
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        #Test public_repos method
        payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart"
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib"
                }
            ]
        }

        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = payload['repos_url']
            self.assertEqual(GithubOrgClient('google').public_repos(), 
                    [
                        "episodes.dart",
                        "cpp-netlib"
                    ])
    """
    @parameterized.expand([
        ({"key": "my_license"}, "my_license", True),
        ({"key": "other_license"}, "my_license", False)
    ])
    def test_has_license(self, my_dict, license, expected):
        """Test if repo has license"""
        with patch('client.GithubOrgClient.has_license') as mock_has_license:
            org = GithubOrgClient('google')
            mock_has_license.return_value = expected
            self.assertEqual(org.has_license(my_dict, license), expected)
