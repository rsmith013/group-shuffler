# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '21 Feb 2020'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

import pandas as pd
import argparse
from random import shuffle


class Table:
    def __init__(self, label):
        self.label = label
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def __repr__(self):
        table = f'\n\nTable: {self.label}'
        for m in self.members:
            table += f'\n\t{m}'

        return table


class Tables:

    def __init__(self, count):
        self.table = 0
        self.count = count
        self.tables = [Table(i) for i in range(count)]

    def get_next_table(self):
        table = self.tables[self.table]

        self.table += 1
        if self.table >= self.count:
            self.table = 0

        return table





parser = argparse.ArgumentParser()
parser.add_argument('csv')
parser.add_argument('-t','--tables', default=2, type=int)
args = parser.parse_args()


# Read the file
df = pd.read_csv(args.csv)

print(f'Total: {df.shape[0]}')

# Create the lists
grouped_staff = df.groupby('Group')

# Spit out tables
tables = Tables(args.tables)

# Loop groups
for group in grouped_staff.groups:
    # Assign a member to each table

    group = grouped_staff.get_group(group)
    indices = group.index.to_list()
    shuffle(indices)

    for i in indices:
        person = group.loc[i]['Name']
        table = tables.get_next_table()
        table.add_member(person)


for t in tables.tables:
    print(t)