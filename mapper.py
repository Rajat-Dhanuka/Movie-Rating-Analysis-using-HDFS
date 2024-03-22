#!/usr/bin/env python3
import sys
import os

# Check if years.txt is empty
if os.stat('years.txt').st_size == 0:
    included_years = set()  # Empty set to include all years
else:
    # Load the years that should be included in the analysis
    with open('years.txt', 'r') as f:
        included_years = set(f.read().split())

# Process each line of input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into individual fields
    uid, title, genres, year, rating = line.strip().split('\t')
    rating = float(rating)
    # Check if the movie's year is included in years.txt
    if not included_years or year in included_years:
        # Split the genres field by '|' to handle multiple genres
        count = len(genres.split('|'))
        print('%s\t%s\t%s\t%s' % (year, title, count*rating, count))