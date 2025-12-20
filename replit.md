# Music Trends Time Machine

## Overview

Music Trends Time Machine is an interactive data analytics dashboard that explores how musical characteristics have evolved over a century (1924-2024) using Spotify-like audio feature data. The application provides dynamic visualizations, temporal trend analysis, genre comparisons, and "what-if" scenario simulations through custom feature weighting.

The project serves as a product-like analytics application that combines exploratory data analysis with interactive simulation and automated insight generation, making complex music data accessible through a guided story mode.

## User Preferences

- **Communication Style**: Simple, everyday language
- **Design Style**: Gen-Z cool with modern Spotify theme, groovy retro aesthetics
- **Navigation**: Top tabs instead of sidebar
- **Typography**: Groovy/Righteous font for main headers
- **Emoji Usage**: None (clean, uppercase text preferred)

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit - chosen for rapid prototyping of data-focused web applications
- **Visualization**: Plotly (both graph_objects and express) for interactive, zoomable charts
- **Styling**: Custom CSS embedded in Streamlit with groovy retro theme and Spotify green color scheme
- **State Management**: Streamlit session state for page navigation and user preferences
- **Typography**: Google Fonts - Righteous for groovy, retro aesthetics

### Design Features
- **Color Palette**: Spotify green (#1DB954), dark backgrounds, purple/blue gradients, cyan accents
- **Effects**: Glowing animations, backdrop blur (glassmorphism), smooth transitions, hover states
- **Layout**: Top navigation tabs (Home, Trends, Simulator, Anomalies, Stories) with clean, modern design
- **Accessibility**: High contrast, large readable text, responsive layout

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
- **Modern UI**: Glassmorphism effects, smooth animations, responsive design

## Features Implemented

### 1. Home Page
- Overview of the dashboard with dataset statistics
- Feature cards explaining each analytics capability
- Metrics showing total tracks, time span, and genre count
- Clean, inviting entry point

### 2. Temporal Trend Analysis (Trends Tab)
- Interactive line charts showing audio feature evolution
- Year range slider for filtering data
- Genre multi-select for comparative analysis
- Feature selection dropdown (energy, danceability, valence, etc.)
- AI-powered insights about detected trend changes

### 3. What-If Simulator (Simulator Tab)
- Feature weight sliders (8 adjustable features)
- Real-time custom score calculation
- Year range filtering
- Visual representation of custom scores over time
- Genre ranking by user preferences

### 4. Anomaly Detector (Anomalies Tab)
- Statistical anomaly detection using z-score
- Sensitivity slider for tuning detection
- Visual chart with anomalies highlighted
- Detailed list of detected anomalies with explanations

### 5. Story Mode (Stories Tab)
- 4 pre-built data stories about music evolution
- Chapter-based narrative experience
- Visual representations for each story
- Interactive story selection

## External Dependencies

### Python Packages
- **streamlit**: Web application framework for data apps
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical operations and array handling
- **plotly**: Interactive visualization library
- **scikit-learn**: Machine learning utilities (StandardScaler)
- **scipy**: Statistical functions (z-score calculations)

### Fonts
- **Righteous** (Google Fonts): Groovy, retro header font

### Data Sources
- Primary: Synthetic data generation (no external API required)
- Designed to work with: Spotify Tracks dataset (tracks.csv) if available

### No External Services Required
- The application is self-contained with synthetic data generation
- No database, authentication, or third-party API integrations
- All data processing happens in-memory
- Caching uses Streamlit's built-in cache

## Deployment Status

- **Current Status**: Development (running on port 5000)
- **Framework**: Streamlit 1.52.2
- **Python Version**: 3.11
- **Ready for Deployment**: Yes - can be deployed to Replit or other platforms
