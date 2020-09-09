#
# Copyright (C) 2020 Satoru SATOH
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""
Use this rule to override some comments' rules.

.. rubric:: Options

* Use ``forbid`` to control comments. Set to ``true`` to forbid comments
  completely.

.. rubric:: Examples

#. With ``override-comments: {forbid: true}``

   the following code snippet would **PASS**:
   ::

    foo: 1

   the following code snippet would **FAIL**:
   ::

    # baz
    foo: 1

.. rubric:: Default values (when enabled)

.. code-block:: yaml

rules:
  override-comments:
    forbid: False

"""
from yamllint.linter import LintProblem


ID = 'override-comments'
TYPE = 'comment'
CONF = {'forbid': bool}
DEFAULT = {'forbid': False}


def check(conf, comment):
    """Check if comments are found.
    """
    if conf['forbid']:
        yield LintProblem(comment.line_no, comment.column_no,
                          'forbidden comment')
