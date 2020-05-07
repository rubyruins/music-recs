import numpy as np
import pandas

class popularity_recommender_py():
	def __init__(self):
		self.train_data = None
		self.n_songs = None
		self.user_id = None
		self.name = None
		self.popularity_recommendations = None
		
	# Create the popularity based recommender system model
	def create(self, train_data, user_id, name):
		self.train_data = train_data
		self.user_id = user_id
		self.name = name

		# Group and count number of unique listeners for each song
		train_data_grouped = self.train_data.groupby([self.name]).agg({self.user_id: 'count'})

		# Rename user_id column so that is shows number of unique listeners for each song
		train_data_grouped.rename(columns = {'user_id': 'listens'},inplace=True)
	
		# Sort the songs based upon listen score
		train_data_sort = train_data_grouped.sort_values(['listens'], ascending=False).reset_index()
	
		# Generate a recommendation rank based upon score
		train_data_sort['rank'] = train_data_sort['listens'].rank(ascending=0, method='first')
		
		# Get the top 10 recommendations
		self.popularity_recommendations = train_data_sort
		return self.popularity_recommendations

	# Make recommendations using this model
	def recommend(self, n_songs):    
		self.n_songs = n_songs
		self.popularity_recommendations = self.popularity_recommendations.head(self.n_songs)
		return self.popularity_recommendations