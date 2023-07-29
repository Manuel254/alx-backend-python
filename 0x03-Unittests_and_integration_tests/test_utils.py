#!/usr/bin/env python3
"""This module tests the access_nested_map function"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
