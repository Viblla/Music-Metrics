"""
Data generation and preprocessing for Music Trends Time Machine
"""
import pandas as pd
import numpy as np
import os

def generate_spotify_data(n_tracks=2000):
    """Generate synthetic Spotify-like data for demonstration"""
    np.random.seed(42)
    
    # Generate year range (1924-2024)
    years = np.random.choice(range(1924, 2025), size=n_tracks, p=None)
    
    # Generate genres
    genres = np.random.choice(
        ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'R&B', 'Latin', 'Folk'],
        size=n_tracks
    )
    
    # Generate audio features with temporal trends
    danceability = np.random.uniform(0.4, 0.9, n_tracks)
    energy = np.random.uniform(0.3, 0.95, n_tracks)
    loudness = np.random.uniform(-10, 0, n_tracks)
    speechiness = np.random.uniform(0, 0.5, n_tracks)
    acousticness = np.random.uniform(0, 1, n_tracks)
    instrumentalness = np.random.uniform(0, 0.8, n_tracks)
    liveness = np.random.uniform(0, 1, n_tracks)
    valence = np.random.uniform(0.2, 0.9, n_tracks)
    tempo = np.random.uniform(60, 200, n_tracks)
    
    # Add temporal trends
    years_norm = (years - 1924) / (2024 - 1924)
    energy = energy + (years_norm * 0.2)
    energy = np.clip(energy, 0, 1)
    danceability = danceability + (years_norm * 0.15)
    danceability = np.clip(danceability, 0, 1)
    acousticness = acousticness - (years_norm * 0.3)
    acousticness = np.clip(acousticness, 0, 1)
    
    tracks_data = {
        'track_id': [f'track_{i}' for i in range(n_tracks)],
        'track_name': [f'Track {i}' for i in range(n_tracks)],
        'artist_name': [f'Artist {np.random.randint(0, 500)}' for _ in range(n_tracks)],
        'year': years,
        'genre': genres,
        'danceability': danceability,
        'energy': energy,
        'loudness': loudness,
        'speechiness': speechiness,
        'acousticness': acousticness,
        'instrumentalness': instrumentalness,
        'liveness': liveness,
        'valence': valence,
        'tempo': tempo,
        'popularity': np.random.randint(0, 100, n_tracks),
    }
    
    return pd.DataFrame(tracks_data)

def load_or_generate_data():
    """Load data from parquet or generate if not exists"""
    if os.path.exists('tracks.parquet'):
        return pd.read_parquet('tracks.parquet')
    
    df = generate_spotify_data(n_tracks=2000)
    df.to_parquet('tracks.parquet', index=False, compression='snappy')
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
