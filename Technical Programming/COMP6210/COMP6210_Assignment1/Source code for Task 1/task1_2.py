# -*- coding: utf-8 -*-
"""
Task 1.2 Data Organization
"""
from mrjob.job import MRJob

class OlympicSort(MRJob):
    def mapper(self, _, line):
        a_id, year, country, event, medal = line.strip().split('\t')
        # Pad the a_id with zeros to ensure correct string-based sorting
        a_id = a_id.zfill(10)
        yield a_id, [year, country, event, medal]

    def reducer(self, a_id, lines):
        a_id = str(int(a_id)) # Remove padding before yielding
        for line in lines:
            yield a_id, line

if __name__ == '__main__':
    OlympicSort.run()

