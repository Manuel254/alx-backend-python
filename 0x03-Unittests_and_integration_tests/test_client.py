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
