# -*- coding: utf-8 -*-
"""
Task 2.2 Top three countries with most gold medals
"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class TopCountries(MRJob):
    def mapper(self, _, line):
        # Split the input line into fields
        _, country, _, _, medal = line.strip().split('\t')
        # Yield country and the type of medal (Gold, Silver, Bronze)
        yield country,medal

    def reducer_count_medals(self, country, medals):
        # Initialize a dictionary to count medals by type
        medal_counts = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        # Count the medals for each country
        for medal in medals:
            if medal in medal_counts:
                medal_counts[medal] += 1
        # Yield the country and the count of Gold, Silver, and Bronze medals
        yield None, (country, medal_counts['Gold'], medal_counts['Silver'], medal_counts['Bronze'])

    def reducer_find_top_three(self, _, country_medal_counts):
        # Sort countries based on Gold medal count (descending order)
        sorted_countries = sorted(country_medal_counts, key=lambda x: x[1], reverse=True)
        # Yield the top three countries with their medal counts
        for country, gold, silver, bronze in sorted_countries[:3]:
            yield country, {'Gold': gold, 'Silver': silver, 'Bronze': bronze}

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count_medals),
            MRStep(reducer=self.reducer_find_top_three)
        ]

if __name__ == '__main__':
    TopCountries.run()
