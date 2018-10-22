# This file is part party_accise module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party', 'PartyIdentifier']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    accise_identifier = fields.Function(fields.Many2One(
            'party.identifier', 'Accise Identifier'),
        'get_accise_identifier', searcher='search_accise_identifier')

    def get_accise_identifier(self, name):
        for identifier in self.identifiers:
            if identifier.type == 'accise':
                return identifier.id

    @classmethod
    def search_accise_identifier(cls, name, clause):
        _, operator, value = clause
        domain = [
            ('identifiers', 'where', [
                    ('code', operator, value),
                    ('type', '=', 'accise'),
                    ]),
            ]
        # Add party without accise identifier
        if ((operator == '=' and value is None)
                or (operator == 'in' and None in value)):
            domain = ['OR',
                domain, [
                    ('identifiers', 'not where', [
                            ('type', '=', 'accise'),
                            ]),
                    ],
                ]
        return domain


class PartyIdentifier(metaclass=PoolMeta):
    __name__ = 'party.identifier'

    @classmethod
    def get_types(cls):
        types = super(PartyIdentifier, cls).get_types()
        types += [('accise', 'Accise')]
        return types
