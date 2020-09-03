#
# Copyright (C) 2020 Satoru SATOH
#
"""YAML Lint plugin entry point
"""
from __future__ import absolute_import
from . import flow_sequence, flow_mapping


RULES_MAP = {
    flow_sequence.ID: flow_sequence,
    flow_mapping.ID: flow_mapping
}
OVERRIDE = False
