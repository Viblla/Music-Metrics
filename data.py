"""
Data generation and preprocessing for Music Trends Time Machine
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_spotify_data(n_tracks=5000):
    """Generate synthetic Spotify-like data for demonstration"""
    np.random.seed(42)
    
    # Generate year range (1924-2024)
    years = np.random.choice(range(1924, 2025), size=n_tracks, p=None)
    
    # Generate genres
    genres = np.random.choice(
        ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'R&B', 'Latin', 'Folk'],
        size=n_tracks
    )
    
    # Generate audio features with some temporal trends
    tracks_data = {
        'track_id': [f'track_{i}' for i in range(n_tracks)],
        'track_name': [f'Track {i}' for i in range(n_tracks)],
        'artist_name': [f'Artist {np.random.randint(0, 500)}' for _ in range(n_tracks)],
        'year': years,
        'genre': genres,
        'danceability': np.random.uniform(0.4, 0.9, n_tracks),
        'energy': np.random.uniform(0.3, 0.95, n_tracks),
        'loudness': np.random.uniform(-10, 0, n_tracks),
        'speechiness': np.random.uniform(0, 0.5, n_tracks),
        'acousticness': np.random.uniform(0, 1, n_tracks),
        'instrumentalness': np.random.uniform(0, 0.8, n_tracks),
        'liveness': np.random.uniform(0, 1, n_tracks),
        'valence': np.random.uniform(0.2, 0.9, n_tracks),
        'tempo': np.random.uniform(60, 200, n_tracks),
        'popularity': np.random.randint(0, 100, n_tracks),
    }
    
    df_tracks = pd.DataFrame(tracks_data)
    
    # Add some temporal trends (gradually increasing energy over time)
    years_norm = (df_tracks['year'] - 1924) / (2024 - 1924)
    df_tracks['energy'] = df_tracks['energy'] + (years_norm * 0.2)
    df_tracks['energy'] = df_tracks['energy'].clip(0, 1)
    
    # Increase danceability in recent years
    df_tracks['danceability'] = df_tracks['danceability'] + (years_norm * 0.15)
    df_tracks['danceability'] = df_tracks['danceability'].clip(0, 1)
    
    # Decrease acousticness over time
    df_tracks['acousticness'] = df_tracks['acousticness'] - (years_norm * 0.3)
    df_tracks['acousticness'] = df_tracks['acousticness'].clip(0, 1)
    
    return df_tracks

def load_or_generate_data():
    """Load data from parquet or generate if not exists"""
    if os.path.exists('tracks.parquet'):
        return pd.read_parquet('tracks.parquet')
    
    print("Generating synthetic Spotify data...")
    df = generate_spotify_data(n_tracks=5000)
    df.to_parquet('tracks.parquet', index=False)
    return df

def aggregate_by_year(df, features=None):
    """Aggregate features by year"""
    if features is None:
        features = ['danceability', 'energy', 'loudness', 'speechiness', 
                   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    
    agg_dict = {feat: 'mean' for feat in features}
    agg_dict['popularity'] = 'mean'
    
    yearly = df.groupby('year').agg(agg_dict).reset_index()
    return yearly

def aggregate_by_genre_year(df, features=None):
    """Aggregate features by genre and year"""
    if features is None:
        features = ['danceability', 'energy', 'loudness', 'speechiness', 
                   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    
    agg_dict = {feat: 'mean' for feat in features}
    agg_dict['popularity'] = 'mean'
    
    genre_yearly = df.groupby(['year', 'genre']).agg(agg_dict).reset_index()
    return genre_yearly
