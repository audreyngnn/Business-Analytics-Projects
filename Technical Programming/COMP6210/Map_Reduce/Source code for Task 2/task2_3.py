# -*- coding: utf-8 -*-
"""
Task 2.3 Top three events with highest medal counts for each decade:
"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class TopEventsByDecade(MRJob):

    def mapper(self, _, line):
        _, country, year, event, medal = line.strip().split('\t')
        year = int(year)

        # Determine the decade based on the year
        if year <= 1989:
            decade = "1980-1989"
        elif year <= 1999:
            decade = "1990-1999"
        elif year <= 2009:
            decade = "2000-2009"
        else:
            decade = "2010-2020"

        # Yield the decade and the country-event-medal information
        yield decade, (country, event, medal)

    def reducer_count_medals(self, decade, values):
        # A dictionary to count medals for each (country, event) pair
        event_medal_counts = {}
        
        for country, event, medal in values:
            key = (country, event)
            
            if key not in event_medal_counts:
                event_medal_counts[key] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

            if medal in event_medal_counts[key]:
                event_medal_counts[key][medal] += 1

        # Yield the total medal count per (country, event) in each decade
        for (country, event), medal_count in event_medal_counts.items():
            total_medals = sum(medal_count.values())
            yield decade, [country, event, total_medals]

    def reducer_find_top_three(self, decade, event_medal_counts):
        # Sort the events within each decade by their total medal count in descending order
        sorted_events = sorted(event_medal_counts, key=lambda x: x[2], reverse=True)

        # Yield the top three events with their medal counts for the current decade
        for country, event, total_medals in sorted_events[:3]:
            yield decade, [country, event, total_medals]  

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count_medals),
            MRStep(reducer=self.reducer_find_top_three)
        ]

if __name__ == '__main__':
    TopEventsByDecade.run()
