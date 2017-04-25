# This file is part party_accise module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import doctest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class PartyAccisaTestCase(ModuleTestCase):
    'Test Party Accisa module'
    module = 'party_accise'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PartyAccisaTestCase))
    return suite
