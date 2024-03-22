#!/usr/bin/env python3
import sys

current_year = None
max_avg_rating = 0
top_movies = []

min_votes = 10

# Process each line from standard input (stdin)
for line in sys.stdin:
    year, title, value = line.strip().split('\t')
    sum_of_ratings, count_of_ratings = map(float, value.split(','))

    if current_year is None:
        current_year = year

    if count_of_ratings >= min_votes:
        avg_rating = sum_of_ratings / count_of_ratings if count_of_ratings > 0 else 0

        # If the year changes, output the results for the previous year
        if year != current_year:
            for movie in top_movies:
                print('%s %s %.1f' % (current_year, movie[0], movie[1]))
            # Reset variables for the new year
            current_year = year
            max_avg_rating = avg_rating
            top_movies = [(title, avg_rating)]
        else:
            # If the average rating is the same as the current maximum, add the movie to the list
            if avg_rating == max_avg_rating:
                top_movies.append((title, avg_rating))
            # If a new maximum is found, update the variables
            elif avg_rating > max_avg_rating:
                max_avg_rating = avg_rating
                top_movies = [(title, avg_rating)]

# Output the final results for the last year
if current_year:
    for movie in top_movies:
        print('%s %s %.1f' % (current_year, movie[0], movie[1]))