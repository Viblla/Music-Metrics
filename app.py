"""
Music Trends Time Machine - Interactive Analytics Dashboard
Modern Spotify-Inspired Gen-Z Theme with Groovy Retro Vibes
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
    initial_sidebar_state="collapsed"
)

# Advanced Custom CSS for Modern Spotify Theme with Groovy Vibes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');
    
    /* Root Colors */
    :root {
        --spotify-green: #1DB954;
        --dark-bg: #0f0f0f;
        --card-bg: #1a1a1a;
        --card-light: #282828;
        --text-primary: #ffffff;
        --text-secondary: #b3b3b3;
        --accent-purple: #7c3aed;
        --accent-pink: #ff006e;
        --accent-blue: #00d9ff;
    }
    
    /* Global Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a0f2e 50%, #0f0f0f 100%) !important;
        color: var(--text-primary) !important;
        font-family: 'Circular', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Main Container */
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }
    
    /* Groovy Retro Headers */
    h1, h2, h3, h4, h5, h6 {
        background: linear-gradient(135deg, var(--spotify-green), var(--accent-blue)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-family: 'Righteous', cursive !important;
        font-weight: 900 !important;
        letter-spacing: -1px !important;
    }
    
    /* Main Header Special */
    .main-header {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        margin-bottom: 1.5rem !important;
        text-shadow: 0 0 30px rgba(29, 185, 84, 0.3) !important;
        animation: glow 2s ease-in-out infinite !important;
        text-transform: uppercase !important;
    }
    
    @keyframes glow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(29, 185, 84, 0.3)); }
        50% { filter: drop-shadow(0 0 30px rgba(124, 58, 237, 0.4)); }
    }
    
    /* Top Navigation Tabs */
    .nav-tabs-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(90deg, rgba(29, 185, 84, 0.05), rgba(124, 58, 237, 0.05)) !important;
        border-bottom: 2px solid rgba(29, 185, 84, 0.3) !important;
        border-radius: 16px !important;
        overflow-x: auto;
        scroll-behavior: smooth;
    }
    
    .nav-tab {
        padding: 12px 24px !important;
        background: rgba(29, 185, 84, 0.1) !important;
        border: 2px solid rgba(29, 185, 84, 0.2) !important;
        border-radius: 12px !important;
        color: var(--text-secondary) !important;
        font-family: 'Righteous', cursive !important;
        font-size: 0.95rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
    }
    
    .nav-tab:hover {
        background: rgba(29, 185, 84, 0.2) !important;
        border-color: var(--spotify-green) !important;
        color: var(--spotify-green) !important;
        transform: translateY(-2px) !important;
    }
    
    .nav-tab.active {
        background: linear-gradient(135deg, var(--spotify-green), #15a049) !important;
        border-color: var(--spotify-green) !important;
        color: #000 !important;
        font-weight: 800 !important;
        box-shadow: 0 8px 25px rgba(29, 185, 84, 0.4) !important;
    }
    
    /* Cards and Containers */
    .feature-card {
        background: linear-gradient(135deg, rgba(29, 185, 84, 0.1), rgba(124, 58, 237, 0.1)) !important;
        border: 1px solid rgba(29, 185, 84, 0.3) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 32px rgba(29, 185, 84, 0.1) !important;
    }
    
    .feature-card:hover {
        border-color: var(--spotify-green) !important;
        box-shadow: 0 12px 48px rgba(29, 185, 84, 0.25) !important;
        transform: translateY(-4px) !important;
    }
    
    .insight-box {
        background: linear-gradient(135deg, rgba(29, 185, 84, 0.15), rgba(0, 217, 255, 0.1)) !important;
        border-left: 4px solid var(--spotify-green) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 15px rgba(29, 185, 84, 0.15) !important;
        transition: all 0.3s ease !important;
    }
    
    .insight-box:hover {
        box-shadow: 0 8px 25px rgba(29, 185, 84, 0.25) !important;
        transform: translateX(4px) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--spotify-green), #15a049) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 24px !important;
        font-weight: 700 !important;
        padding: 12px 28px !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 15px rgba(29, 185, 84, 0.3) !important;
        font-family: 'Righteous', cursive !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-pink)) !important;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Input Elements */
    input, select, textarea {
        background: var(--card-light) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(29, 185, 84, 0.2) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
    }
    
    input:focus, select:focus, textarea:focus {
        border-color: var(--spotify-green) !important;
        box-shadow: 0 0 20px rgba(29, 185, 84, 0.3) !important;
        outline: none !important;
    }
    
    /* Slider */
    .stSlider > div > div {
        color: var(--spotify-green) !important;
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(29, 185, 84, 0.1), rgba(124, 58, 237, 0.1)) !important;
        border: 1px solid rgba(29, 185, 84, 0.2) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 15px rgba(29, 185, 84, 0.1) !important;
    }
    
    /* Text */
    p, span, label {
        color: var(--text-primary) !important;
    }
    
    .secondary-text {
        color: var(--text-secondary) !important;
        font-size: 0.95rem !important;
    }
    
    /* Scroll Bar */
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg) !important;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--spotify-green) !important;
        border-radius: 4px !important;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-purple) !important;
    }
    
    /* Animation Classes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out !important;
    }
    
    /* Plotly Chart Styling */
    .plotly-graph-div {
        background: transparent !important;
    }
    
    /* Info, Warning, Error Messages */
    [data-testid="stAlert"] {
        border-radius: 12px !important;
        border-left: 4px solid var(--spotify-green) !important;
        background: rgba(29, 185, 84, 0.1) !important;
    }
    
    /* Music Theme Elements */
    .vinyl-record {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #1DB954, #0f0f0f);
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
        margin-right: 10px;
    }
    
    .music-note {
        display: inline-block;
        font-size: 1.2rem;
        margin: 0 4px;
    }
</style>

<link href='https://fonts.googleapis.com/css2?family=Righteous&display=swap' rel='stylesheet'>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Load data
@st.cache_data(ttl=3600)
def get_data():
    return load_or_generate_data()

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Top Navigation Tabs
col_spacer, col_nav = st.columns([0.05, 0.95])
with col_nav:
    st.markdown('<div style="margin: 0; padding: 0;"></div>', unsafe_allow_html=True)
    
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
    
    pages = ['Home', 'Trends', 'Simulator', 'Anomalies', 'Stories']
    
    with nav_col1:
        if st.button('Home', use_container_width=True, key='nav_home'):
            st.session_state.current_page = 'Home'
    with nav_col2:
        if st.button('Trends', use_container_width=True, key='nav_trends'):
            st.session_state.current_page = 'Trends'
    with nav_col3:
        if st.button('Simulator', use_container_width=True, key='nav_sim'):
            st.session_state.current_page = 'Simulator'
    with nav_col4:
        if st.button('Anomalies', use_container_width=True, key='nav_anomaly'):
            st.session_state.current_page = 'Anomalies'
    with nav_col5:
        if st.button('Stories', use_container_width=True, key='nav_stories'):
            st.session_state.current_page = 'Stories'

st.markdown("---")

page = st.session_state.current_page

# ==================== HOME PAGE ====================
if page == 'Home':
    st.markdown('<h1 class="main-header">MUSIC TRENDS TIME MACHINE</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style='color: #1DB954; margin-bottom: 0.5rem;'>AN INTERACTIVE ANALYTICS DASHBOARD</h3>
        <p style='font-size: 1.1rem; color: #b3b3b3; margin-bottom: 1rem;'>
        Explore how musical characteristics have evolved over a century of sound using Spotify data. 
        From the roaring twenties to the streaming era, discover the trends that shaped our culture.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset Overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("TOTAL TRACKS", f"{len(df):,}")
    with col2:
        st.metric("TIME SPAN", f"{int(df['year'].min())}-{int(df['year'].max())}")
    with col3:
        st.metric("UNIQUE GENRES", df['genre'].nunique())
    
    st.markdown("---")
    
    # Features Grid
    st.markdown('<h2 style="text-align: center; margin-top: 2rem;">WHAT YOU CAN DO</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>TEMPORAL TRENDS</h3>
            <p style='color: #b3b3b3;'>
            Track how audio features like energy, danceability, and valence have evolved across decades. 
            Filter by genre and year to discover patterns that shaped modern music.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>ANOMALY DETECTION</h3>
            <p style='color: #b3b3b3;'>
            Discover sudden, unusual shifts in music trends. Use our anomaly detection algorithm 
            to find pivotal moments when the sound of music dramatically changed.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>WHAT-IF SIMULATOR</h3>
            <p style='color: #b3b3b3;'>
            Customize your perfect playlist by adjusting feature weights. See how different 
            recommendation strategies would rank genres across decades.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>STORY MODE</h3>
            <p style='color: #b3b3b3;'>
            Follow a guided narrative through music history. Discover key insights and pivotal moments 
            that shaped how we listen to music today.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #b3b3b3; margin-top: 2rem;'>Navigate using the tabs above to explore the full experience</p>", unsafe_allow_html=True)

# ==================== TEMPORAL TREND ANALYSIS ====================
elif page == 'Trends':
    st.markdown('<h1 class="main-header">TEMPORAL TRENDS</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #b3b3b3; font-size: 1.05rem;'>Watch how music characteristics evolve over time</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        year_range = st.slider(
            "Year Range",
            int(df['year'].min()),
            int(df['year'].max()),
            (1950, 2024),
            step=5
        )
    with col2:
        selected_genres = st.multiselect(
            "Genres",
            options=sorted(df['genre'].unique().tolist()),
            default=['Pop', 'Rock', 'Hip-Hop']
        )
    with col3:
        feature = st.selectbox(
            "Audio Feature",
            ['energy', 'danceability', 'valence', 'acousticness', 'tempo', 'loudness']
        )
    
    st.markdown("---")
    
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
        title=f'{feature.upper()} EVOLUTION',
        labels={'year': 'Year', feature: feature.capitalize()},
        markers=True,
        template='plotly_dark'
    )
    fig.update_layout(
        height=500,
        hovermode='x unified',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(29, 185, 84, 0.05)',
        font=dict(family='Arial, sans-serif', color='#ffffff')
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))
    st.plotly_chart(fig, use_container_width=True)
    
    # Show insights
    st.markdown("### AI INSIGHTS")
    insights = get_anomaly_insights(filtered_df, feature)
    if insights:
        for insight in insights:
            st.markdown(f"<div class='insight-box'>{insight}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='insight-box'>No significant anomalies detected in {feature} for the selected period.</div>", unsafe_allow_html=True)

# ==================== WHAT-IF SIMULATOR ====================
elif page == 'Simulator':
    st.markdown('<h1 class="main-header">WHAT-IF SIMULATOR</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #b3b3b3; font-size: 1.05rem;'>Design your perfect playlist recommendation algorithm</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2.2])
    
    with col1:
        st.markdown("### ADJUST WEIGHTS")
        weights = {
            'energy': st.slider('ENERGY', 0.0, 1.0, 0.5, step=0.1),
            'danceability': st.slider('DANCEABILITY', 0.0, 1.0, 0.5, step=0.1),
            'valence': st.slider('POSITIVITY', 0.0, 1.0, 0.5, step=0.1),
            'acousticness': st.slider('ACOUSTICNESS', 0.0, 1.0, 0.3, step=0.1),
            'tempo': st.slider('TEMPO', 0.0, 1.0, 0.4, step=0.1),
            'instrumentalness': st.slider('INSTRUMENTAL', 0.0, 1.0, 0.2, step=0.1),
            'liveness': st.slider('LIVENESS', 0.0, 1.0, 0.3, step=0.1),
            'speechiness': st.slider('SPOKEN WORD', 0.0, 1.0, 0.1, step=0.1),
        }
    
    with col2:
        year_range = st.slider("Year Range", int(df['year'].min()), int(df['year'].max()), (1950, 2024), key='sim_year')
        
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
        fig.add_trace(go.Scatter(
            x=yearly_scores['year'], 
            y=yearly_scores['custom_score'], 
            name='Your Score',
            mode='lines+markers',
            line=dict(color='#1DB954', width=4),
            marker=dict(size=10),
            fill='tozeroy',
            fillcolor='rgba(29, 185, 84, 0.2)'
        ))
        fig.update_layout(
            title='YOUR CUSTOM SCORE OVER TIME',
            height=400,
            xaxis_title='Year',
            yaxis_title='Score',
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(29, 185, 84, 0.05)',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### GENRE RANKINGS")
    genre_scores = sim_df.groupby('genre')['custom_score'].mean().sort_values(ascending=False)
    fig = px.bar(
        x=genre_scores.values,
        y=genre_scores.index,
        orientation='h',
        labels={'x': 'Average Score', 'y': 'Genre'},
        title='HOW GENRES MATCH YOUR PREFERENCES',
        template='plotly_dark',
        color=genre_scores.values,
        color_continuous_scale=['#7c3aed', '#1DB954']
    )
    fig.update_layout(
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(29, 185, 84, 0.05)',
    )
    st.plotly_chart(fig, use_container_width=True)

# ==================== ANOMALY DETECTOR ====================
elif page == 'Anomalies':
    st.markdown('<h1 class="main-header">ANOMALY DETECTOR</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #b3b3b3; font-size: 1.05rem;'>Discover when music fundamentally changed</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        feature = st.selectbox(
            "Select Feature",
            ['energy', 'danceability', 'valence', 'acousticness', 'tempo', 'loudness'],
            key='anomaly_feature'
        )
    with col2:
        sensitivity = st.slider("Detection Sensitivity", 1.0, 3.0, 2.0, step=0.1)
    
    st.markdown("---")
    
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
        line=dict(color='#1DB954', width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(29, 185, 84, 0.15)'
    ))
    
    if len(anomalies) > 0:
        anomaly_years = yearly.iloc[anomalies]
        fig.add_trace(go.Scatter(
            x=anomaly_years['year'],
            y=anomaly_years[feature],
            mode='markers',
            name='ANOMALIES DETECTED',
            marker=dict(size=16, color='#ff006e', symbol='star', line=dict(color='#ffffff', width=2))
        ))
    
    fig.update_layout(
        title=f'ANOMALY ANALYSIS: {feature.upper()}',
        height=500,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(29, 185, 84, 0.05)',
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Display anomaly insights
    st.markdown("### DETECTED ANOMALIES")
    if len(anomalies) > 0:
        for idx in anomalies:
            year = int(yearly.iloc[idx]['year'])
            value = yearly.iloc[idx][feature]
            st.markdown(
                f"<div class='insight-box'><b>{year}</b> — Unusual {feature} level detected ({value:.3f})</div>",
                unsafe_allow_html=True
            )
    else:
        st.markdown(
            "<div class='insight-box'>No significant anomalies detected with current sensitivity setting.</div>",
            unsafe_allow_html=True
        )

# ==================== STORY MODE ====================
elif page == 'Stories':
    st.markdown('<h1 class="main-header">STORY MODE</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #b3b3b3; font-size: 1.05rem;'>Follow music through the ages</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    stories = generate_story_insights(df)
    
    story_num = st.selectbox(
        "Select a story",
        range(len(stories)),
        format_func=lambda x: f"Chapter {x+1}: {stories[x]['title']}"
    )
    
    story = stories[story_num]
    
    st.markdown(f"""
    <div class="feature-card">
        <h2 style='color: #1DB954;'>{story['title']}</h2>
        <p style='color: #b3b3b3; font-size: 1.05rem; margin-top: 1rem;'>{story['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### VISUAL STORY")
    
    # Visualization for this story
    if story['feature'] in ['energy', 'danceability', 'acousticness', 'valence', 'tempo', 'loudness']:
        yearly = aggregate_by_year(df)
        fig = px.line(
            yearly,
            x='year',
            y=story['feature'],
            title=f'THE EVOLUTION OF {story["feature"].upper()}',
            markers=True,
            template='plotly_dark'
        )
        fig.update_traces(line=dict(color='#1DB954', width=4), marker=dict(size=10))
        fig.update_layout(
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(29, 185, 84, 0.05)',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    elif story['feature'] == 'genre':
        genre_counts = df.groupby(['year', 'genre']).size().reset_index(name='count')
        fig = px.bar(
            genre_counts,
            x='year',
            y='count',
            color='genre',
            title='GENRE DISTRIBUTION OVER TIME',
            template='plotly_dark'
        )
        fig.update_layout(
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(29, 185, 84, 0.05)',
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Chapter indicator
    st.markdown(f"""
    <div style='text-align: center; margin-top: 2rem; padding: 1rem; background: rgba(29, 185, 84, 0.1); border-radius: 12px;'>
        <p style='color: #1DB954; font-weight: bold; font-size: 1.1rem;'>CHAPTER {story_num + 1} OF {len(stories)}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #b3b3b3;'>
    <p style='font-family: Righteous, cursive; font-size: 1.2rem;'>MUSIC TRENDS TIME MACHINE</p>
    <p style='font-size: 0.9rem; margin-top: 0.5rem;'>Powered by Spotify Data | Explore 100 Years of Sound | 1924-2024</p>
</div>
""", unsafe_allow_html=True)
