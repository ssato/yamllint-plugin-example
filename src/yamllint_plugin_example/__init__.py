#
# Copyright (C) 2020 Satoru SATOH
#
"""YAML Lint plugin entry point
"""
from __future__ import absolute_import
from . import override_comments


RULES_MAP = {
    override_comments.ID: override_comments
}
OVERRIDE = False
