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

class item_similarity_recommender_py():
	
	def __init__(self):
		self.train_data = None
		self.user_id = None
		self.item_id = None
		self.cooccurence_matrix = None
		self.songs_dict = None
		self.rev_songs_dict = None
		self.item_similarity_recommendations = None

	# Create the item similarity based recommender system model
	def create(self, train_data, user_id, item_id):
		self.train_data = train_data
		self.user_id = user_id
		self.item_id = item_id
	
	# Get all unique users for a given item (song)
	def get_item_users(self, item):
		item_data = self.train_data[self.train_data[self.item_id] == item]
		item_users = set(item_data[self.user_id].unique())
		return item_users
		
	#Construct cooccurence matrix
	def construct_cooccurence_matrix(self, user_songs, all_songs):
			
		# Get users for every song in user_songs.
		user_songs_users = []        
		for i in range(len(user_songs)):
			user_songs_users.append(self.get_item_users(user_songs[i]))
			
		# Initialize the item cooccurence matrix of size len(user_songs) X len(songs)
		cooccurence_matrix = np.matrix(np.zeros(shape=(len(user_songs), len(all_songs))), float)
		   
		# Calculate similarity between user songs and all unique songs in the training data
		for i in range(len(all_songs)):
			# Calculate unique listeners (users) of song (item) i
			songs_i_data = self.train_data[self.train_data[self.item_id] == all_songs[i]]
			users_i = set(songs_i_data[self.user_id].unique())
			
			for j in range(0,len(user_songs)):       		
				# Get unique listeners (users) of song (item) j
				users_j = user_songs_users[j]	
				# Calculate intersection of listeners of songs i and j
				users_intersection = users_i.intersection(users_j)
				# Calculate cooccurence_matrix[i,j] as Jaccard Index
				if len(users_intersection) != 0:
					# Calculate union of listeners of songs i and j
					users_union = users_i.union(users_j)
					cooccurence_matrix[j,i] = float(len(users_intersection))/float(len(users_union))
				else:
					cooccurence_matrix[j,i] = 0

		return cooccurence_matrix

	# Use the cooccurence matrix to make top recommendations
	def generate_top_recommendations(self, user, cooccurence_matrix, all_songs, user_songs):
		print("Non zero values in cooccurence_matrix :%d" % np.count_nonzero(cooccurence_matrix))
		# Calculate a weighted average of the scores in cooccurence matrix for all user songs.
		user_sim_scores = cooccurence_matrix.sum(axis=0)/float(cooccurence_matrix.shape[0])
		user_sim_scores = np.array(user_sim_scores)[0].tolist()
 
		# Sort the indices of user_sim_scores based upon their value
		# Also maintain the corresponding score
		sort_index = sorted(((e,i) for i,e in enumerate(list(user_sim_scores))), reverse=True)
	
		# Create a dataframe from the following
		columns = ['user_id', 'song', 'score', 'rank']
		# index = np.arange(1) # array of numbers for the number of samples
		df = pandas.DataFrame(columns=columns)
		 
		# Fill the dataframe with top 10 item based recommendations
		rank = 1 
		for i in range(0,len(sort_index)):
			if ~np.isnan(sort_index[i][0]) and all_songs[sort_index[i][1]] not in user_songs and rank <= 10:
				df.loc[len(df)]=[user,all_songs[sort_index[i][1]],sort_index[i][0],rank]
				rank = rank+1
		
		# Handle the case where there are no recommendations
		if df.shape[0] == 0:
			print("The current user has no songs for training the item similarity based recommendation model.")
			return -1
		else:
			return df
 
	#Get similar items to given items
	def get_similar_items(self, item_list):
		
		user_songs = item_list
		
		# Get number of unique songs in the dataset
		all_songs = list(self.train_data[self.item_id].unique())
		print("Scanning %d songs to find the best match for you..." % len(all_songs))
		 
		# Construct item cooccurence matrix of size len(user_songs) X len(songs)
		cooccurence_matrix = self.construct_cooccurence_matrix(user_songs, all_songs)
		
		# Use the cooccurence matrix to make recommendations
		user = ""
		df_recommendations = self.generate_top_recommendations(user, cooccurence_matrix, all_songs, user_songs)
		return df_recommendations