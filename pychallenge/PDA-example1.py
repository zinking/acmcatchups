import pandas as pd
from pandas import Series, DataFrame

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('~/Downloads/ml-1m/users.dat', sep="::", header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('~/Downloads/ml-1m/ratings.dat', sep="::", header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('~/Downloads/ml-1m/movies.dat', sep="::", header=None, names=mnames)

