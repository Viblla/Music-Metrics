"""
Utility functions for Music Trends Time Machine
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy import stats

def normalize_features(df, features):
    """Normalize features for fair comparison"""
    df_copy = df.copy()
    scaler = StandardScaler()
    df_copy[features] = scaler.fit_transform(df_copy[features])
    return df_copy

def detect_anomalies(series, threshold=2.0):
    """Detect anomalies using z-score"""
    cleaned = series.dropna().values
    z_scores = np.abs(stats.zscore(cleaned))
    anomaly_indices = np.where(z_scores > threshold)[0]
    return anomaly_indices

def calculate_custom_score(row, weights):
    """Calculate custom score based on feature weights"""
    features = ['danceability', 'energy', 'loudness', 'acousticness', 
                'instrumentalness', 'liveness', 'valence', 'tempo', 'speechiness']
    
    score = 0
    total_weight = sum(weights.values())
    
    for feat in features:
        if feat in row and feat in weights:
            # Normalize loudness to 0-1 scale
            if feat == 'loudness':
                normalized = (row[feat] + 10) / 10
                normalized = max(0, min(1, normalized))
            else:
                normalized = row[feat]
            
            score += normalized * weights.get(feat, 0)
    
    if total_weight > 0:
        score = score / total_weight
    
    return score

def get_anomaly_insights(df, feature):
    """Generate insight messages about anomalies"""
    insights = []
    
    if len(df) < 2:
        return insights
    
    yearly_avg = df.groupby('year')[feature].mean()
    
    if len(yearly_avg) < 3:
        return insights
    
    # Calculate year-over-year change
    yoy_change = yearly_avg.diff()
    
    # Find significant jumps (> 1 std dev)
    std_change = yoy_change.std()
    threshold = std_change * 1.5
    
    anomaly_years = yoy_change[abs(yoy_change) > threshold].index
    
    for year in anomaly_years[-3:]:  # Last 3 anomalies
        change = yoy_change[year]
        direction = "increased" if change > 0 else "decreased"
        magnitude = abs(change)
        insights.append(f"Notable {direction} in {feature} in {year} ({magnitude:.2f})")
    
    return insights

def generate_story_insights(df):
    """Generate guided story mode insights"""
    stories = []
    
    # Story 1: Energy trends
    early_energy = df[df['year'] < 1970]['energy'].mean()
    recent_energy = df[df['year'] >= 2000]['energy'].mean()
    stories.append({
        'title': 'The Rise of High-Energy Music',
        'description': f'Music has become significantly more energetic over the decades. From the early 1900s (avg {early_energy:.2f}) to the 2000s (avg {recent_energy:.2f}), energy levels have increased by {((recent_energy-early_energy)/early_energy*100):.1f}%.',
        'feature': 'energy'
    })
    
    # Story 2: Danceability
    early_dance = df[df['year'] < 1970]['danceability'].mean()
    recent_dance = df[df['year'] >= 2000]['danceability'].mean()
    stories.append({
        'title': 'The Danceability Revolution',
        'description': f'Modern tracks are increasingly designed for dancing. Danceability has risen from {early_dance:.2f} in early decades to {recent_dance:.2f} in recent years.',
        'feature': 'danceability'
    })
    
    # Story 3: Acousticness decline
    early_acoustic = df[df['year'] < 1970]['acousticness'].mean()
    recent_acoustic = df[df['year'] >= 2000]['acousticness'].mean()
    stories.append({
        'title': 'The Digital Revolution: Acousticness Decline',
        'description': f'As technology advanced, music shifted from acoustic to electronic production. Acousticness dropped from {early_acoustic:.2f} to {recent_acoustic:.2f}.',
        'feature': 'acousticness'
    })
    
    # Story 4: Genre diversity by era
    stories.append({
        'title': 'Genre Evolution Across Eras',
        'description': f'Different genres dominated different eras. Early music was dominated by Classical and Jazz, while modern music spans Pop, Hip-Hop, Electronic, and more.',
        'feature': 'genre'
    })
    
    return stories
