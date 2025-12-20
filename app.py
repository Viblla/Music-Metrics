"""
Music Trends Time Machine - Interactive Analytics Dashboard
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from data import load_or_generate_data, aggregate_by_year, aggregate_by_genre_year
from utils import (
    normalize_features, detect_anomalies, calculate_custom_score,
    get_anomaly_insights, generate_story_insights
)

# Page config
st.set_page_config(
    page_title="Music Trends Time Machine",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; color: #1DB954; margin-bottom: 1rem; }
    .feature-card { padding: 1rem; border-radius: 0.5rem; background-color: #f0f0f0; margin: 0.5rem 0; }
    .insight-box { padding: 1rem; border-left: 4px solid #1DB954; background-color: #f9f9f9; margin: 0.5rem 0; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Load data
@st.cache_data(ttl=3600)
def get_data():
    return load_or_generate_data()

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar Navigation
with st.sidebar:
    st.markdown("# 🎧 Music Trends Time Machine")
    page = st.radio(
        "Navigate to:",
        ['Home', 'Temporal Analysis', 'What-If Simulator', 'Anomaly Detector', 'Story Mode'],
        key='page_radio'
    )

# ==================== HOME PAGE ====================
if page == 'Home':
    st.markdown('<h1 class="main-header">🎧 Music Trends Time Machine</h1>', unsafe_allow_html=True)
    st.write("""
    ### An Interactive Analytics Dashboard for Exploring a Century of Music Evolution
    
    Explore how musical characteristics have evolved over time using Spotify data spanning from 1924 to 2024.
    
    **What you can do:**
    - 📈 **Temporal Trend Analysis** - Track how audio features change over decades
    - 🎛️ **What-If Simulator** - Adjust feature weights and see how recommendations change
    - 🚨 **Anomaly Detector** - Discover unusual shifts in music trends
    - 📖 **Story Mode** - Follow a guided narrative of music evolution
    
    **Dataset:** {:,} tracks across {} genres
    """.format(len(df), df['genre'].nunique()))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tracks", f"{len(df):,}")
    with col2:
        st.metric("Time Span", f"{df['year'].min():.0f}-{df['year'].max():.0f}")
    with col3:
        st.metric("Unique Genres", df['genre'].nunique())

# ==================== TEMPORAL TREND ANALYSIS ====================
elif page == 'Temporal Analysis':
    st.markdown('<h1 class="main-header">📈 Temporal Trend Analysis</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        year_range = st.slider(
            "Select Year Range",
            int(df['year'].min()),
            int(df['year'].max()),
            (1950, 2024),
            step=5
        )
    with col2:
        selected_genres = st.multiselect(
            "Select Genres",
            options=df['genre'].unique().tolist(),
            default=['Pop', 'Rock', 'Hip-Hop']
        )
    
    feature = st.selectbox(
        "Select Feature to Analyze",
        ['energy', 'danceability', 'valence', 'acousticness', 'tempo', 'loudness']
    )
    
    # Filter data
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    if selected_genres:
        filtered_df = filtered_df[filtered_df['genre'].isin(selected_genres)]
    
    # Create trend line
    yearly_data = filtered_df.groupby(['year', 'genre'])[feature].mean().reset_index()
    
    fig = px.line(
        yearly_data,
        x='year',
        y=feature,
        color='genre',
        title=f'{feature.capitalize()} Trend Over Time',
        labels={'year': 'Year', feature: feature.capitalize()},
        markers=True
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Show insights
    st.subheader("📊 Insights")
    insights = get_anomaly_insights(filtered_df, feature)
    if insights:
        for insight in insights:
            st.info(insight)
    else:
        st.info(f"No significant anomalies detected in {feature} for the selected period.")

# ==================== WHAT-IF SIMULATOR ====================
elif page == 'What-If Simulator':
    st.markdown('<h1 class="main-header">🎛️ What-If Simulator</h1>', unsafe_allow_html=True)
    
    st.write("Adjust the importance (weights) of different audio features to simulate custom recommendation strategies.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Feature Weights")
        weights = {
            'energy': st.slider('Energy', 0.0, 1.0, 0.5),
            'danceability': st.slider('Danceability', 0.0, 1.0, 0.5),
            'valence': st.slider('Valence (Positivity)', 0.0, 1.0, 0.5),
            'acousticness': st.slider('Acousticness', 0.0, 1.0, 0.3),
            'tempo': st.slider('Tempo', 0.0, 1.0, 0.4),
            'instrumentalness': st.slider('Instrumentalness', 0.0, 1.0, 0.2),
            'liveness': st.slider('Liveness', 0.0, 1.0, 0.3),
            'speechiness': st.slider('Speechiness', 0.0, 1.0, 0.1),
        }
    
    with col2:
        year_range = st.slider("Year Range", int(df['year'].min()), int(df['year'].max()), (1950, 2024))
        
        # Filter and calculate scores
        sim_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])].copy()
        sim_df['custom_score'] = sim_df.apply(lambda row: calculate_custom_score(row, weights), axis=1)
        
        # Aggregate by year
        yearly_scores = sim_df.groupby('year').agg({
            'custom_score': 'mean',
            'energy': 'mean',
            'danceability': 'mean',
            'valence': 'mean',
        }).reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=yearly_scores['year'], y=yearly_scores['custom_score'], 
                                 name='Custom Score', mode='lines+markers', line=dict(color='#1DB954', width=3)))
        fig.update_layout(title='Your Custom Music Score Over Time', height=400, xaxis_title='Year', yaxis_title='Score')
        st.plotly_chart(fig, use_container_width=True)
    
    # Genre rankings by custom score
    st.subheader("Genre Rankings by Your Preferences")
    genre_scores = sim_df.groupby('genre')['custom_score'].mean().sort_values(ascending=False)
    fig = px.bar(x=genre_scores.values, y=genre_scores.index, orientation='h', 
                 labels={'x': 'Average Score', 'y': 'Genre'}, title='Top Genres by Your Preferences')
    st.plotly_chart(fig, use_container_width=True)

# ==================== ANOMALY DETECTOR ====================
elif page == 'Anomaly Detector':
    st.markdown('<h1 class="main-header">🚨 Anomaly Detector</h1>', unsafe_allow_html=True)
    
    st.write("Automatically detect unusual spikes or drops in musical trends.")
    
    feature = st.selectbox(
        "Select Feature to Analyze",
        ['energy', 'danceability', 'valence', 'acousticness', 'tempo', 'loudness'],
        key='anomaly_feature'
    )
    
    sensitivity = st.slider("Detection Sensitivity", 1.0, 3.0, 2.0, step=0.1)
    
    # Calculate yearly averages
    yearly = aggregate_by_year(df)
    
    # Detect anomalies
    anomalies = detect_anomalies(yearly[feature], threshold=sensitivity)
    
    # Plot with anomalies highlighted
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=yearly['year'],
        y=yearly[feature],
        mode='lines+markers',
        name='Trend',
        line=dict(color='#1DB954', width=2)
    ))
    
    if len(anomalies) > 0:
        anomaly_years = yearly.iloc[anomalies]
        fig.add_trace(go.Scatter(
            x=anomaly_years['year'],
            y=anomaly_years[feature],
            mode='markers',
            name='Anomalies',
            marker=dict(size=12, color='red', symbol='star')
        ))
    
    fig.update_layout(title=f'Anomaly Detection in {feature.capitalize()}', height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Display anomaly insights
    st.subheader("🔍 Detected Anomalies")
    if len(anomalies) > 0:
        for idx in anomalies:
            year = yearly.iloc[idx]['year']
            value = yearly.iloc[idx][feature]
            st.warning(f"**{year}**: Unusual {feature} level detected ({value:.3f})")
    else:
        st.info("No significant anomalies detected with current sensitivity setting.")

# ==================== STORY MODE ====================
elif page == 'Story Mode':
    st.markdown('<h1 class="main-header">📖 Story Mode</h1>', unsafe_allow_html=True)
    
    st.write("Follow a guided narrative through music's evolution over the past century.")
    
    stories = generate_story_insights(df)
    
    story_num = st.selectbox("Select Story", range(len(stories)), format_func=lambda x: f"Story {x+1}: {stories[x]['title']}")
    
    story = stories[story_num]
    
    st.subheader(story['title'])
    st.markdown(f"<div class='insight-box'>{story['description']}</div>", unsafe_allow_html=True)
    
    # Visualization for this story
    if story['feature'] in ['energy', 'danceability', 'acousticness', 'valence', 'tempo', 'loudness']:
        yearly = aggregate_by_year(df)
        fig = px.line(yearly, x='year', y=story['feature'], 
                     title=f'The {story["title"]} - {story["feature"].capitalize()} Over Time',
                     markers=True)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    elif story['feature'] == 'genre':
        genre_counts = df.groupby(['year', 'genre']).size().reset_index(name='count')
        fig = px.bar(genre_counts, x='year', y='count', color='genre',
                    title='Genre Distribution Over Time')
        st.plotly_chart(fig, use_container_width=True)
    
    st.info(f"This is Story {story_num + 1} of {len(stories)}")

# Footer
st.markdown("---")
st.markdown("🎧 **Music Trends Time Machine** | A data analytics project exploring Spotify music evolution")
