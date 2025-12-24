# 🎵 Music Metrics: Time Machine

A comprehensive interactive dashboard for exploring 121 years of music evolution through data visualization and statistical analysis.

## Project Overview

Music Metrics is an advanced web-based analytics platform that analyzes **586,672 music tracks** spanning from **1900 to 2021**. It leverages audio feature data (energy, danceability, acousticness, valence, tempo, loudness) to uncover fascinating trends and patterns in music history.

Built with **HTML/CSS/JavaScript** and **Plotly.js**, this modern dashboard offers superior interactivity and performance compared to traditional Streamlit apps.

### Key Highlights
- ✅ 7 interactive visualizations
- ✅ Click-based detailed tooltips
- ✅ Real-time genre filtering
- ✅ Anomaly detection with adjustable sensitivity
- ✅ 4 narrative story modes
- ✅ Full 586K+ track dataset
- ✅ Responsive design (desktop/mobile)
- ✅ Dark theme with professional styling

---

## 📊 Dataset Description

### Source
- **Spotify Audio Features Dataset** (Public Dataset)
- Extracted tracks and artist information with audio metrics

### Data Coverage
- **Time Period**: 1900 - 2021 (121 years)
- **Total Tracks**: 586,672
- **Unique Artists**: 1,162,095+
- **Genres**: Pop, Rock, Hip-Hop, Jazz, Classical, Electronic, and more

### Key Audio Features
The dataset includes audio metrics for each track:

1. **Danceability** (0.0 - 1.0): How suitable a track is for dancing
2. **Energy** (0.0 - 1.0): Intensity and activity of a track
3. **Loudness** (-60 to 0 dB): Overall loudness in decibels
4. **Acousticness** (0.0 - 1.0): Likelihood the track is acoustic
5. **Valence** (0.0 - 1.0): Musical positivity (happy/cheerful)
6. **Tempo** (BPM): Speed in beats per minute
9. **Tempo** (BPM): Overall speed of the track

### Data Files
- `tracks.csv` - Track information and audio features
- `artists.csv` - Artist details and genre information

---

## ✨ Features

### 📊 7 Interactive Visualizations

1. **Temporal Trends** - Track audio feature evolution over decades
2. **Perfect Hit** - Correlation analysis for hit songs by era
3. **Genre Deep Dive** - Compare features across 5 genres
4. **Hit Song Blueprint** - Discover perfect feature combinations
5. **Feature Space Explorer** - Multi-dimensional scatter analysis
6. **Anomaly Detector** - Find statistical outliers (adjustable sensitivity)
7. **Story Mode** - 4 narrative journeys through music history:
   - The Great Acoustic Decline
   - Rising Energy Levels
   - The Dance Revolution
   - Mood Swings in Music

### 🎯 Interactive Controls

- **Click-Based Tooltips** - Detailed insights on any data point
- **Genre Filtering** - Pop, Rock, Hip-Hop, Electronic, Jazz
- **Dynamic Sliders** - Year ranges, sensitivity thresholds
- **Feature Dropdowns** - Select any audio metric
- **Responsive Design** - Desktop, tablet, mobile friendly
- **Dark Theme** - Professional teal/blue color scheme

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5 + CSS3 (Grid, Flexbox, Gradients)
- JavaScript ES6+
- Plotly.js 2.26.0 (Interactive charts)
- Lenis 1.1.13 (Smooth scrolling)
- GSAP 3.12.2 (Animations)

**Backend:**
- Python HTTP Server (Development)
- CSV data processing

**Design:**
- Dark mode with teal (#00d9a3) and blue (#00b8ff) accents
- Modern glassmorphism effects
- Responsive grid layout

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

1. **Navigate to project**
```bash
cd d:\GIKI\7\ Sem\Viz\Music-Metrics
```

2. **Activate virtual environment**
```bash
.\.venv\Scripts\activate
```

3. **Start server**
```bash
cd docs
python -m http.server 8000
```

4. **Open dashboard**
```
http://localhost:8000/dashboard.html
```

---

## 📖 Usage Guide

### Exploring Temporal Trends
1. Go to "Temporal Trends" section
2. Adjust year range sliders
3. Select feature from dropdown
4. Choose genres to filter
5. Click any point for detailed year insights

### Analyzing Anomalies
1. Navigate to "Anomaly Detector"
2. Select feature to analyze
3. Adjust sensitivity slider (1σ to 2σ)
4. Click anomaly points for Z-score details

### Discovering Hit Songs
1. Open "Hit Song Blueprint"
2. Select era/decade
3. View hit vs non-hit feature comparisons
4. Click points for feature relationships

### Story Mode
1. Click story buttons at bottom
2. Read trend narratives
3. View decade-by-decade timeline
4. Click chart points for deeper context

---

## 📁 Project Structure

```
Music-Metrics/
├── docs/
│   ├── dashboard.html              # Main dashboard
│   ├── dashboard-script-cwm.js      # JavaScript logic
│   ├── dashboard-styles-cwm.css     # Styling
│   ├── tracks.csv                   # 586K tracks
│   └── artists.csv                  # Artist data
├── README.md                         # This file
├── requirements.txt                  # Dependencies
├── pyproject.toml                    # Config
└── .venv/                            # Virtual env
```

---

## 🔍 Key Insights

### The Great Acoustic Decline
Acoustic instruments dominated early music but declined 1980s-2000s as digital production became mainstream.

### Rising Energy Levels
Modern tracks (2010s) show 30%+ higher energy than 1900s, reflecting faster pace of contemporary life.

### Dance Revolution
EDM/pop explosion created peak danceability in 2010s with standardized 4/4 beats and electronic production dominance.

### Mood Swings
Valence follows economic cycles - happier music in prosperous times, darker moods during uncertainty.

---

## 🌐 Deployment Options

Coming next! We'll help you deploy to:
- **GitHub Pages** (Free, no backend needed)
- **Netlify** (Free with CI/CD)
- **Vercel** (Free, optimized for speed)
- **Firebase Hosting** (Free with authentication)

---

## 🐛 Troubleshooting

### Dashboard not loading?
- Ensure server is running: `python -m http.server 8000`
- Clear cache: Ctrl+F5
- Verify CSV files in docs/ folder

### Charts not rendering?
- Open console (F12) for errors
- Enable JavaScript
- Check network tab for failed requests

### Slow performance?
- Close other tabs
- Use modern browser (Chrome/Firefox)
- Reduce other background processes

---

## 📝 Future Enhancements

- [ ] Export charts as PNG/PDF
- [ ] Advanced correlation analysis
- [ ] ML-powered predictive features
- [ ] Audio sample playback
- [ ] User accounts & saved analyses
- [ ] Real-time Spotify API integration
- [ ] Collaborative features
- [ ] Mobile app version

---

## 📞 Support

For issues or questions:
1. Check browser console (F12) for errors
2. Verify all CSV files are present
3. Try clearing browser cache
4. Ensure Python server is running

---

## 📄 License

Educational project - Open for learning and modification.

---

## 👨‍💼 Project Information

- **Course**: Data Visualization (Semester 7)
- **University**: GIKI (Ghulam Ishaq Khan Institute)
- **Dataset**: 586,672 Spotify tracks (1900-2021)
- **Status**: Complete ✅

---

**Built with passion for music and data** 🎵📊
# On Windows:
.\.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:5000` (or the URL shown in terminal)

---

## 📱 Dashboard Features

### 🏠 Home Page
- Project overview and description
- Dataset statistics (total tracks, time span, genres, artists)
- Feature highlights for all dashboard sections

### 📈 Trends Analysis
- **Temporal Visualizations**: Line charts showing feature evolution over time
- **Interactive Filters**:
  - Year range slider (1900-2021)
  - Multi-select genre picker
  - Audio feature selector
- **AI-Powered Insights**: Automatic detection and description of significant trends

### 🎮 What-If Simulator
- **Custom Weight Adjustment**: Sliders for 8 audio features
  - Energy, Danceability, Positivity (Valence)
  - Acousticness, Tempo, Instrumentalness
  - Liveness, Spoken Word (Speechiness)
- **Real-time Score Calculation**: See how your preferences match different eras
- **Genre Rankings**: Discover which genres match your preferences
- **Visual Feedback**: Dynamic charts updating as you adjust weights

### 🔍 Anomaly Detection
- **Statistical Analysis**: Identifies unusual patterns in audio features
- **Sensitivity Control**: Adjustable threshold for anomaly detection
- **Visual Highlighting**: Stars mark detected anomalies on timeline
- **Detailed Insights**: Specific years and values for anomalies found

### 📖 Story Mode
- **Guided Narratives**: Pre-written stories about music evolution
- **Chapter Navigation**: Browse through curated insights
- **Visual Storytelling**: Charts and visualizations supporting each story
- **Key Moments**: Discover pivotal decades in music history

---

## 📊 Exploratory Data Analysis (EDA)

### Key Findings

#### 1. Temporal Distribution
- Exponential growth in recorded music post-1980
- Significant data increase after 2000 with streaming era
- Coverage across entire 121-year period

#### 2. Feature Evolution
- **Energy**: Relatively stable but shows genre-specific variations
- **Danceability**: Increases in modern pop/electronic genres
- **Acousticness**: Declining trend in mainstream music
- **Valence**: Genre-dependent with pop maintaining higher values
- **Tempo**: Relatively consistent across decades with genre variation

#### 3. Genre Distribution
- Pop, Rock, and Hip-Hop dominate the dataset
- Classical and Jazz well-represented in historical periods
- Emergence of Electronic and EDM in recent decades
- Multiple subgenres providing rich categorical diversity

#### 4. Audio Feature Correlations
- Energy and Loudness: Strong positive correlation
- Acousticness and Energy: Negative correlation
- Danceability: Genre-specific patterns
- Valence: Independent of most features

#### 5. Missing Data
- Minimal missing values after preprocessing
- Most tracks have complete feature sets
- Some historical data points sparse before 1950

---

## 🎯 Key Insights & Stories

### Story 1: The Rise of Danceability
Modern music increasingly optimized for clubs and dance floors. From 1980 onwards, danceability scores show significant increase, peaking in electronic and pop genres.

### Story 2: Acoustic Decline
While acoustic music persists, mainstream trends show decreasing acousticness over time. Traditional instruments replaced by electronic production.

### Story 3: Energy Paradox
Despite stereotypes, modern music isn't necessarily "louder" - energy levels remain relatively stable with genre-specific variations.

### Story 4: The Electronic Revolution
Electronic and synth-based music emergence in 1980s marked by distinct audio feature signatures - high tempo, high energy, low acousticness.

---

## 📁 Project Structure

```
Music-Metrics/
├── app.py                 # Main Streamlit application
├── data.py               # Data loading and preprocessing
├── utils.py              # Utility functions for analysis
├── test_data.py          # Data testing utilities
├── tracks.csv            # Spotify tracks dataset
├── artists.csv           # Spotify artists dataset
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── EDA.md               # Exploratory Data Analysis document
├── .gitignore           # Git ignore file
└── .venv/               # Virtual environment (not in repo)
```

---

## 🔧 Technical Implementation

### Data Pipeline
1. **Data Loading**: CSV import with error handling
2. **Preprocessing**: Date parsing, null value handling, genre extraction
3. **Aggregation**: Yearly and genre-based calculations
4. **Caching**: Streamlit cache decorators for performance

### Visualization Strategy
- **Plotly** for interactive charts with hover information
- **Custom color schemes** matching Spotify brand colors
- **Responsive layouts** for mobile compatibility
- **Real-time updates** based on user selections

### Performance Optimization
- Cached data loading (1 hour TTL)
- Efficient pandas operations
- Lazy rendering for hidden sections
- Optimized filter operations

---

## 🎬 Video Walkthrough

A video demonstration of the dashboard is available showing:
- Navigation through all sections
- Interactive feature demonstrations
- Data filtering and analysis
- Anomaly detection in action
- Story mode exploration

**[Link to Video](https://youtube.com/yourvideolink)** *(Update with actual video link)*

---

## 🔗 Links

- **GitHub Repository**: [https://github.com/yourusername/Music-Metrics](https://github.com/yourusername/Music-Metrics)
- **Project Website**: [https://yourusername.github.io/Music-Metrics](https://yourusername.github.io/Music-Metrics)
- **Streamlit Dashboard**: *(Update with deployment link if published)*

---

## 📈 Future Enhancements

- [ ] Add collaborative filtering recommendations
- [ ] Implement user preference saving
- [ ] Add export functionality (PDF reports)
- [ ] Create mood-based playlist suggestions
- [ ] Add social media sharing features
- [ ] Implement audio playback preview
- [ ] Add artist comparison tools
- [ ] Create advanced statistical models

---

## 📝 License

This project is open source and available under the MIT License. See LICENSE file for details.

---

## 🙏 Acknowledgments

- Spotify for the comprehensive audio feature dataset
- Streamlit community for the excellent framework
- Plotly for interactive visualization tools
- OpenAI for insights on data analysis and storytelling

---

## 📧 Contact & Support

For questions, suggestions, or collaboration inquiries, please contact:
- **Email**: youremail@example.com
- **GitHub Issues**: [Open an issue](https://github.com/yourusername/Music-Metrics/issues)

---

**Last Updated**: December 24, 2025

*Built with ❤️ for music lovers and data enthusiasts*
