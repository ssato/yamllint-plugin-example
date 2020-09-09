# -*- coding: utf-8 -*-
# Copyright (C) 2020 Satoru SATOH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# pylint: disable=missing-function-docstring
"""test cases for override-comments rule.
"""
import tests.common


class TestCase(tests.common.RuleTestCase):
    """override-comments test cases.
    """
    rule_id = 'override-comments'

    def test_disabled(self):
        conf = ('override-comments:\n'
                '  forbid: false\n')
        self.check('---\n'
                   'a: 1\n', conf)

    def test_enabled(self):
        conf = ('override-comments:\n'
                '  forbid: true\n')
        self.check('---\n'
                   '# a\n'
                   'a: 1\n', conf, problem=(2, 1))
        self.check('---\n'
                   'a: 1  # a\n', conf, problem=(2, 7))
