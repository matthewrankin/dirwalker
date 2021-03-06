# -*- coding: utf-8 -*-
# Copyright (c) 2014 The dirwalker developers. All rights reserved.
# Project site: https://github.com/questrail/dirwalker
# Use of this source code is governed by a MIT-style license that
# can be found in the LICENSE.txt file for the project.
"""Unit tests for dirwalker.py.
"""
# Try to future proof code so that it's Python 3.x ready
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import os
import unittest
import dirwalker


class TestFindingFiles(unittest.TestCase):

    def setUp(self):
        self.sample_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'sample_dir')
        self.known_sample_file_01_txt = os.path.join(
            self.sample_dir,
            'sample_file_01.txt')
        self.known_sample_file_02_txt = os.path.join(
            self.sample_dir,
            'sample_file_02.txt')
        self.known_sample_file_03_csv = os.path.join(
            self.sample_dir,
            'sample_file_03.csv')
        self.known_sample_file_04_csv = os.path.join(
            self.sample_dir,
            'sample_file_04.csv')
        self.known_sample_file_05_py = os.path.join(
            self.sample_dir,
            'sample_file_05.py')
        self.known_sample_file_06_js = os.path.join(
            self.sample_dir,
            'sample_file_06.js')
        self.known_sample_level_2_file_01_txt = os.path.join(
            self.sample_dir,
            'sample_dir_level_2',
            'sample_level_2_file_01.txt')
        self.known_sample_level_2_file_02_txt = os.path.join(
            self.sample_dir,
            'sample_dir_level_2',
            'sample_level_2_file_02.txt')
        self.known_sample_level_2_file_03_csv = os.path.join(
            self.sample_dir,
            'sample_dir_level_2',
            'sample_level_2_file_03.csv')
        self.known_sample_level_2_file_04_csv = os.path.join(
            self.sample_dir,
            'sample_dir_level_2',
            'sample_level_2_file_04.csv')
        self.known_sample_level_2_file_05_py = os.path.join(
            self.sample_dir,
            'sample_dir_level_2',
            'sample_level_2_file_05.py')

    def test_find_single_file_without_extension_period(self):
        """Find extensions that don't have a period"""
        test_set = set([self.known_sample_file_06_js])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                self.sample_dir,
                ['js']),
            test_set)

    def test_find_multiple_files_without_extension_period(self):
        """Find extensions in recursive directories"""
        test_set = set([
            self.known_sample_file_01_txt,
            self.known_sample_file_02_txt,
            self.known_sample_level_2_file_01_txt,
            self.known_sample_level_2_file_02_txt])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                self.sample_dir,
                ['txt']),
            test_set)

    def test_find_multiple_files_without_recursion(self):
        """Find extensions without recursing subdirectories"""
        test_set = set([
            self.known_sample_file_01_txt,
            self.known_sample_file_02_txt])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                self.sample_dir,
                ['txt'],
                recurse=False),
            test_set)

    def test_find_single_file_with_extension_period(self):
        """Find extensions that have a period"""
        test_set = set([self.known_sample_file_06_js])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                self.sample_dir,
                ['.js']),
            test_set)

    def test_find_multiple_extensions(self):
        """Find more than one extension"""
        test_set = set([
            self.known_sample_file_05_py,
            self.known_sample_file_06_js,
            self.known_sample_level_2_file_05_py])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                self.sample_dir,
                ['js', '.py']),
            test_set)

    def test_relative_path(self):
        test_set = set([self.known_sample_file_06_js])
        self.assertEqual(
            dirwalker.find_filenames_with_extensions(
                './tests/sample_dir/',
                ['.js']),
            test_set)


if __name__ == '__main__':
    unittest.main()
