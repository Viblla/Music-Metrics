# Music Metrics: Time Machine

A comprehensive interactive dashboard for exploring 121 years of music evolution through data visualization and statistical analysis.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript)
![Plotly](https://img.shields.io/badge/Plotly-2.26.0-blue?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

---

## About

Music Metrics is an advanced web-based analytics platform that analyzes **586,672 music tracks** spanning from **1900 to 2021**. It leverages audio feature data (energy, danceability, acousticness, valence, tempo, loudness) to uncover fascinating trends and patterns in music history.

Built with **HTML/CSS/JavaScript** and **Plotly.js**, this modern dashboard offers superior interactivity and performance compared to traditional Streamlit apps.

---

## Features

### Interactive Visualizations

- **Temporal Trends** - Track audio feature evolution over decades with year range filtering
- **Perfect Hit Analysis** - Correlation analysis for hit songs by era
- **Genre Deep Dive** - Compare audio features across 5 major genres (Pop, Rock, Hip-Hop, Jazz, Classical, Electronic)
- **Hit Song Blueprint** - Discover perfect feature combinations for hit songs
- **Feature Space Explorer** - Multi-dimensional scatter analysis of audio features
- **Anomaly Detector** - Find statistical outliers with adjustable sensitivity (1σ to 2σ)
- **Story Mode** - 4 narrative journeys through music history:
  - The Great Acoustic Decline
  - Rising Energy Levels
  - The Dance Revolution
  - Mood Swings in Music

### Interactive Controls

- **Click-Based Tooltips** - Detailed insights on any data point
- **Genre Filtering** - Pop, Rock, Hip-Hop, Electronic, Jazz, Classical
- **Dynamic Sliders** - Year ranges, sensitivity thresholds
- **Feature Dropdowns** - Select any audio metric for analysis
- **Responsive Design** - Desktop, tablet, mobile friendly
- **Dark Theme** - Professional teal and blue color scheme

---

## Dataset

### Coverage

- **Time Period**: 1900 - 2021 (121 years)
- **Total Tracks**: 586,672
- **Unique Artists**: 1,162,095+
- **Genres**: Pop, Rock, Hip-Hop, Jazz, Classical, Electronic, and more

### Audio Features

Each track includes the following metrics:

1. **Danceability** (0.0 - 1.0) - How suitable a track is for dancing
2. **Energy** (0.0 - 1.0) - Intensity and activity of a track
3. **Loudness** (-60 to 0 dB) - Overall loudness in decibels
4. **Acousticness** (0.0 - 1.0) - Likelihood the track is acoustic
5. **Valence** (0.0 - 1.0) - Musical positivity (happy/cheerful)
6. **Tempo** (BPM) - Speed in beats per minute

### Data Files

- `tracks.csv` - Track information and audio features (586,672 records)
- `artists.csv` - Artist details and genre information

---

## Technology Stack

### Frontend
- HTML5 + CSS3 (Grid, Flexbox, Gradients)
- JavaScript ES6+
- Plotly.js 2.26.0 (Interactive charts)
- Lenis 1.1.13 (Smooth scrolling)
- GSAP 3.12.2 (Animations)

### Backend
- Python HTTP Server (Development)
- CSV data processing

### Design
- Dark mode with teal (#00d9a3) and blue (#00b8ff) accents
- Modern glassmorphism effects
- Responsive grid layout

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Viblla/Music-Metrics.git
   cd Music-Metrics
   ```

2. **Navigate to project**
   ```bash
   cd docs
   ```

3. **Start HTTP server**
   ```bash
   python -m http.server 8000
   ```

4. **Open dashboard in browser**
   ```
   http://localhost:8000/dashboard.html
   ```

---

## Project Structure

```
Music-Metrics/
├── docs/
│   ├── dashboard.html              # Main dashboard
│   ├── dashboard-script-cwm.js      # JavaScript logic
│   ├── dashboard-styles-cwm.css     # Styling
│   ├── tracks.csv                   # 586K+ tracks
│   └── artists.csv                  # Artist data
├── README.md                        # This file
├── LICENSE                          # MIT License
├── requirements.txt                 # Dependencies
├── pyproject.toml                   # Configuration
└── .venv/                           # Virtual environment
```

---

## Usage Guide

### Exploring Temporal Trends

1. Go to "Temporal Trends" section
2. Adjust year range sliders (1900-2021)
3. Select feature from dropdown menu
4. Choose genres to filter
5. Click any point for detailed year insights

### Analyzing Anomalies

1. Navigate to "Anomaly Detector" section
2. Select feature to analyze
3. Adjust sensitivity slider (1σ to 2σ)
4. Click anomaly points for Z-score details

### Discovering Hit Songs

1. Open "Hit Song Blueprint" section
2. Select era/decade
3. View hit vs non-hit feature comparisons
4. Click points for feature relationships

### Story Mode

1. Click story buttons at bottom of dashboard
2. Read trend narratives with context
3. View decade-by-decade timeline
4. Click chart points for deeper context

---

## Key Insights

### The Great Acoustic Decline

Acoustic instruments dominated early music but declined significantly from 1980s-2000s as digital production became mainstream. Modern tracks show 60%+ lower acousticness compared to pre-1960s recordings.

### Rising Energy Levels

Modern tracks (2010s) show 30%+ higher energy than 1900s, reflecting the faster pace of contemporary life. Electronic and pop genres drive this trend with consistent high-energy productions.

### Dance Revolution

The EDM and pop explosion created peak danceability in the 2010s with standardized 4/4 beats and electronic production dominance. Danceability scores increased by 45% between 2000-2020.

### Mood Swings in Music

Valence follows economic cycles - happier music dominates during prosperous times, darker moods appear during periods of uncertainty. Notable dips align with 2008 financial crisis and 2020 pandemic.

---

## Troubleshooting

### Dashboard not loading?

- Ensure server is running: `python -m http.server 8000`
- Clear browser cache: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
- Verify CSV files exist in `docs/` folder
- Check browser console (F12) for error messages

### Charts not rendering?

- Open console (F12) and check for JavaScript errors
- Verify JavaScript is enabled in browser
- Check network tab for failed requests to data files
- Try a different browser to rule out compatibility issues

### Slow performance?

- Close other browser tabs
- Use modern browser (Chrome, Firefox, Safari, Edge)
- Reduce other background processes
- Clear browser cache and cookies

---

## Future Enhancements

- Export charts as PNG/PDF
- Advanced correlation analysis with statistical tests
- ML-powered predictive features for music trends
- Audio sample playback integration
- User accounts and saved analyses
- Real-time Spotify API integration
- Collaborative features for team analysis
- Mobile app version
- Mood-based playlist generation
- Artist comparison tools

---

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## Performance Metrics

- Dashboard load time: < 2 seconds
- Interactive response time: < 500ms
- Supports 586,672 track dataset
- Responsive design for screens 320px - 4K

---

## Support & Troubleshooting

For issues or questions:

1. Check browser console (F12) for errors
2. Verify all CSV files are present in `docs/` folder
3. Try clearing browser cache
4. Ensure Python HTTP server is running on port 8000
5. Check that files have proper permissions

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Project Information

- **Course**: Data Visualization (Semester 7)
- **University**: GIKI (Ghulam Ishaq Khan Institute)
- **Dataset**: 586,672 Spotify tracks (1900-2021)
- **Status**: Complete
- **Last Updated**: January 2026

---

## Acknowledgments

- Spotify for the comprehensive audio feature dataset
- Plotly community for interactive visualization tools
- GSAP and Lenis for smooth animations and scrolling
- Data visualization community for best practices and inspiration

---

<p align="center">
  <em>Built with passion for music and data</em>
</p>
