#!/usr/bin/env python3
#
# Copyright 2021-2022 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt


import logging
import sys
import pexpect
from assessment import solution_check_simple


def run_p1(binary):
    """Run part-1"""
    status = True
    values = (
                ('ham', 'rye', 'mayo'),
                ('tuna', 'wheat', 'mustard'),
                ('roast beef', 'kaiser roll', 'horse radish and mayo'),
            )
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p1(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))

    i = 0
    try:
        proc.expect(
            r'(?i)\s*Enter\s+protein.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter protein: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s+bread.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter bread: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s+condiment.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter condiment: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        all_words = [word for val in values for word in val.split(' ')]
        if len(all_words) > 3:
            values = all_words[:3]
        regex = r'(?i)\s*Your\s+order.?\s+A\s+{}\s+sandwich\s+on\s+{}\s+with\s+{}.?\s*'.format(*values)
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error(f'Expected:"Your order:\nA {values[0]} sandwich on {values[1]} with {values[2]}."')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


def run_p2(binary):
    """Run part-2"""
    status = True
    values = (
                ('100', '20.28\d*', '6.76\d*', '3.38\d*', '0.42\d*'),
                ('23', '4.66\d*', '1.55\d*', '0.77\d*', '0.09\d*'),
                ('-10', '-2.02\d*', '-0.67\d*', '-0.33\d*', '-0.04\d*'),
                ('1.234', '0.25\d*', '0.08\d*', '0.04\d*', '0.00\d*'),
                ('-11.432', '-2.31\d*', '-0.77\d*', '-0.38\d*', '-0.04\d*'),
                ('0', '0\.?\d*', '0\.?\d*', '0\.?\d*', '0\.?\d*'),
            )
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p2(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    # values = list(map(str, values))
    i = 0
    try:
        proc.expect(
            r'(?i)\s*Enter\s+ml.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter ml: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        regex = r'(?i)\s*{}\s*ml\s*=\s*{}\s*tsp\s*=\s*{}\s*tbsp\s*=\s*{}\s*oz\s*=\s*{}\s*cups\s*'.format(*values)
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "{} ml = {} tsp  = {} tbsp  = {} oz  = {} cups"'.format(*values))
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


def run_p3(binary):
    """Run part-3"""
    status = True
    values = (
                (42, 23, r'Too\s+low', 45, 'Incorrect, the secret number was 42, you lose.'),
                (42, 45, r'Too\s+high', 23, 'Incorrect, the secret number was 42, you lose.'),
                (42, 1, r'Too\s+low', 42, 'Correct, you win!'),
                (42, 42, r'Correct.?\s+you\s+win!', None),
                (-6, 5, r'Too\s+high', 4, 'Incorrect, the secret number was -6, you lose.'),
                (-6, 5, r'Too\s+high', -6, 'Correct, you win!')
            )
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p3(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p3(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))

    i = 0
    try:
        proc.expect(
            r'(?i)\s*Player\s+1,\s+enter\s+the\s+secret\s+number.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Player 1, enter the secret number: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1
    
    try:
        proc.expect(
            r'(?i)\s*Player\s+2,\s+enter\s+your\s+first\s+guess.?\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Player 2, enter your first guess: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1
    
    if values[3] != 'None':
        try:
            regex = r'(?i){}\s+Player\s+2,\s+enter\s+your\s+second\s+guess.?\s+'.format(values[i])
            proc.expect(regex)
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            logging.error('Expected: "Player 2, enter your second guess: "')
            logging.error('Could not find expected output.')
            logging.debug("%s", str(exception))
            logging.debug(str(proc))
            return status

        i += 1
        proc.sendline(values[i])
        i += 1
    
    if values[0] == values[3] or values[0] == values[1]:
        regex = r'(?i)\s*Correct.?\s+you\s+win.?\s+'
        expected_response = '"Correct, you win!"'
    else:
        regex = r'(?i)\s*Incorrect.?\s+the\s+secret\s+number\s+was\s+{}.?\s+you\s+lose.?\s+'.format(values[0])
        expected_response = '"Incorrect, the secret number was {}, you lose."'.format(values[0])
    try:
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error(f'Expected: {expected_response}')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


if __name__ == '__main__':
    tidy_opts = (
        '-checks="*,-misc-unused-parameters,'
        '-modernize-use-trailing-return-type,-google-build-using-namespace,'
        '-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers"'
        ' -config="{CheckOptions: [ {key: readability-identifier-naming.VariableCase, value: lower_case},'
        ' { key: readability-identifier-naming.FunctionCase, value: CamelCase }, '
        '{key: readability-identifier-naming.GlobalConstantCase,  value: UPPER_CASE}, '
        '{key: readability-identifier-naming.GlobalConstantPrefix, value: k} ]}"'
    )
    if sys.argv[1] == 'part-1':
        solution_check_simple(
            run=run_p1, files=['sandwich.cc'],
            tidy_options=tidy_opts,
            skip_compile_cmd=True,
        )
    elif sys.argv[1] == 'part-2':
        solution_check_simple(
            run=run_p2,
            files=['units.cc'],
            tidy_options=tidy_opts,
            skip_compile_cmd=True,
        )
    elif sys.argv[1] == 'part-3':
        solution_check_simple(
            run=run_p3,
            files=['hilo.cc'],
            tidy_options=tidy_opts,
            skip_compile_cmd=True,
        )
    else:
        print('Error: no match.')
