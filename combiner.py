#!/usr/bin/env python3
import sys

current_key = None
sum_of_ratings = 0
count_of_ratings = 0

# Process each line from standard input (stdin)
for line in sys.stdin:
    year, title, rating, count = line.strip().split('\t')
    key = year+'\t'+title
    rating = float(rating)
    count = int(count)

    if current_key is None:
        current_key = key
    
    # If the key changes, emit the result for the previous key
    if key != current_key:
        if current_key:
            # Emit the aggregated result for the previous key
            print('%s\t%s,%s' % (current_key, sum_of_ratings, count_of_ratings))
        # Update current key and reset sum and count
        current_key = key
        sum_of_ratings = 0
        count_of_ratings = 0
    
    # Accumulate sum of ratings and count of ratings for the current key
    sum_of_ratings += rating
    count_of_ratings += count

if current_key:
    print('%s\t%s,%s' % (current_key, sum_of_ratings, count_of_ratings))