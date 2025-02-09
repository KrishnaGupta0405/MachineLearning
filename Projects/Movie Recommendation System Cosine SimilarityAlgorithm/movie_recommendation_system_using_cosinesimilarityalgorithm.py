"""#Import the Libraries"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""#Import thr Dataset"""

dataset = pd.read_csv('movies.csv')
list_of_all_titles = dataset['title'].tolist()
print(dataset.shape)

"""#Data Preprocessing"""

selected_features = ['genres','keywords','tagline','cast','director']

# replacing the null valuess with null string
for feature in selected_features:
  dataset[feature] = dataset[feature].fillna('')

# combining all the 5 selected features
combined_features = dataset['genres']+' '+dataset['keywords']+' '+dataset['tagline']+' '+dataset['cast']+' '+dataset['director']

"""#Convert dataset into vector format"""

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

"""#Training Cosine Similarity Algorithm

"""

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(feature_vectors)

"""#Testing the algorithm"""

import difflib

# Getting the movie name from the user
movie_name = input("Enter the name of the movie: ").strip()

# Creating a list with all movie names from the dataset
list_of_all_titles = movies_data['title'].tolist()
print(f"\nList of all the titles in the dataset-> {list_of_all_titles[:5]}...\n")

# Finding close matches for the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=3, cutoff=0.5)
print(f"List of close Matches-> {find_close_match}\n")

# Handling cases where no close match is found
if not find_close_match:
    print("No close matches found. Please check your movie name and try again.")
else:
    close_match = find_close_match[0]  # Choosing the best match i.e. the first one
    print(f"The closest One-> {close_match}\n")

    # Finding the index of the matched movie title in the dataset
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    print(f"The closest one index in dataset-> {index_of_the_movie}\n")

    # Getting a list of similar movies based on similarity scores
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # Displaying the first few similarity scores for reference
    print(f"The closest one similarity score with other movies-> {similarity_score[:5]}...\n")

    # Sorting movies based on similarity scores (Descending order)
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    print(f"Sorted similarity score-> {sorted_similar_movies[:5]}...\n")  # Display first few for readability

    # Printing the top recommended movies
    print("\nMovies suggested for you :\n")

    i = 1
    for movie in sorted_similar_movies[1:]:  # Skip the first one (itself)
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]

        if i <= 10:  # Display the first 10 recommendations
            print(f"{i} . {title_from_index}")
            i += 1