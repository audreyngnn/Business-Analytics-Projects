# -*- coding: utf-8 -*-
"""
Task 2.1 Top 3 athletes with most medals in each category
"""

from mrjob.job import MRJob
from mrjob.step import MRStep

class TopAthletesPerMedal(MRJob):

    def mapper(self, _, line):
        athlete_id, _, _, _, medal = line.strip().split('\t')
        yield (athlete_id, medal), 1

    def combiner(self, key, counts):
        yield key, sum(counts)

    def reducer_count(self, key, counts):
        athlete_id, medal = key
        total = sum(counts)
        yield medal, (athlete_id, total)

    def reducer_top_three(self, medal, athlete_counts):
        sorted_athletes = sorted(athlete_counts, key=lambda x: x[1], reverse=True)
        for athlete_id, count in sorted_athletes[:3]:
            yield medal, f"{athlete_id}: {count}"

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer_count),
            MRStep(reducer=self.reducer_top_three)
        ]

if __name__ == '__main__':
    TopAthletesPerMedal.run()