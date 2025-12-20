# Music Trends Time Machine

## Overview

Music Trends Time Machine is an interactive data analytics dashboard that explores how musical characteristics have evolved over a century (1924-2024) using Spotify-like audio feature data. The application provides dynamic visualizations, temporal trend analysis, genre comparisons, and "what-if" scenario simulations through custom feature weighting.

The project serves as a product-like analytics application that combines exploratory data analysis with interactive simulation and automated insight generation, making complex music data accessible through a guided story mode.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit - chosen for rapid prototyping of data-focused web applications
- **Visualization**: Plotly (both graph_objects and express) for interactive, zoomable charts
- **Styling**: Custom CSS embedded in Streamlit for branded appearance (Spotify green theme)
- **State Management**: Streamlit session state for page navigation and user preferences

### Data Layer
- **Data Generation**: Synthetic Spotify-like data generation when real data unavailable
- **Features Tracked**: Audio features including danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo
- **Temporal Range**: 100 years of music data (1924-2024)
- **Genre Categories**: 10 genres (Pop, Rock, Hip-Hop, Electronic, Classical, Jazz, Country, R&B, Latin, Folk)
- **Caching**: Streamlit's `@st.cache_data` decorator with 1-hour TTL for performance

### Analytics Engine
- **Normalization**: scikit-learn's StandardScaler for feature comparison
- **Anomaly Detection**: Z-score based detection with configurable threshold
- **Custom Scoring**: Weighted feature aggregation for "what-if" simulations
- **Aggregation**: Year-level and genre-year level data aggregation functions

### Application Structure
```
├── app.py          # Main Streamlit application with UI and navigation
├── data.py         # Data generation, loading, and preprocessing
├── utils.py        # Analytics utilities (normalization, anomalies, scoring)
```

### Design Patterns
- **Separation of Concerns**: Data handling, utilities, and UI in separate modules
- **Caching Strategy**: Data cached at application level to avoid regeneration
- **Error Handling**: Graceful error display with `st.error()` and `st.stop()`

## External Dependencies

### Python Packages
- **streamlit**: Web application framework for data apps
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical operations and array handling
- **plotly**: Interactive visualization library
- **scikit-learn**: Machine learning utilities (StandardScaler)
- **scipy**: Statistical functions (z-score calculations)

### Data Sources
- Primary: Synthetic data generation (no external API required)
- Designed to work with: Spotify Tracks dataset (tracks.csv) if available

### No External Services Required
- The application is self-contained with synthetic data generation
- No database, authentication, or third-party API integrations
- All data processing happens in-memory