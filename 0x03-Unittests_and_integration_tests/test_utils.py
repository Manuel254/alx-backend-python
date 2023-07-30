#!/usr/bin/env python3
"""This module tests the access_nested_map function"""
import unittest
from parameterized import parameterized
import utils
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """A class that has a methos that tests for a nested
    map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access nested map function for a key
        error exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class that tests a function to see if it
    returns a payload from a url
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, result):
        """Tests a function get_json"""
        with patch('utils.requests') as mock_requests:
            mock_response = Mock()
            mock_response.json.return_value = result
            mock_requests.get.return_value = mock_response

            payload = get_json(url)

            mock_requests.get.assert_called_once_with(url)
            self.assertEqual(payload, result)


class TestMemoize(unittest.TestCase):
    """Contains a memoized method"""
    def test_memoize(self):
        """Test memoize method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
