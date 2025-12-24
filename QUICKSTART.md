# Music Metrics - Quick Start Guide

Get your dashboard running in 5 minutes! 🚀

## For Local Testing

### 1. Start Server
```bash
cd d:\GIKI\7\ Sem\Viz\Music-Metrics\docs
python -m http.server 8000
```

### 2. Open Dashboard
```
http://localhost:8000/dashboard.html
```

Done! Dashboard is live. 🎵

---

## For Deployment (Choose One)

### Option A: Netlify (Easiest, Recommended)
1. Push code to GitHub
2. Go to netlify.com → "New site from Git"
3. Connect GitHub account
4. Select your music-metrics repo
5. Click "Deploy"
6. Wait 2 minutes
7. Your site is live!

→ See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

### Option B: GitHub Pages
1. Push code to GitHub
2. Settings → Pages
3. Select "main" branch
4. Wait 1-2 minutes
5. Site live at `https://USERNAME.github.io/music-metrics/`

### Option C: Vercel
1. Go to vercel.com
2. Import GitHub repository
3. Click Deploy
4. Site live instantly!

---

## First Time Using Dashboard?

### 1. Explore Trends
- Go to "Temporal Trends" section
- Move year sliders
- Select different features
- Click any point to see details

### 2. Check Anomalies
- Scroll to "Anomaly Detector"
- Adjust sensitivity slider
- Click outlier points
- See Z-scores and statistics

### 3. Read Stories
- Scroll to bottom "Story Mode"
- Click each story button
- Read narratives
- View decade-by-decade breakdown

### 4. Filter by Genre
- Use genre checkboxes
- Mix Pop, Rock, Hip-Hop, Electronic, Jazz
- Watch charts update instantly

---

## Dashboard Map

```
┌─────────────────────────────────┐
│        HOME / HERO SECTION      │ ← Stats & Overview
├─────────────────────────────────┤
│      TEMPORAL TRENDS            │ ← Year-by-year feature analysis
├─────────────────────────────────┤
│      PERFECT HIT                │ ← Hit song correlation
├─────────────────────────────────┤
│      GENRE DEEP DIVE            │ ← Genre comparison
├─────────────────────────────────┤
│      HIT SONG BLUEPRINT         │ ← Feature success factors
├─────────────────────────────────┤
│      FEATURE SPACE EXPLORER     │ ← Multi-dimensional analysis
├─────────────────────────────────┤
│      ANOMALY DETECTOR           │ ← Statistical outliers
├─────────────────────────────────┤
│      STORY MODE                 │ ← Narrative exploration
└─────────────────────────────────┘
```

---

## Key Features at a Glance

| Feature | What It Does | Try This |
|---------|-------------|----------|
| **Year Sliders** | Filter by time period | Drag to 2000-2020 |
| **Genre Checkboxes** | Choose music types | Uncheck Pop |
| **Feature Dropdown** | Pick metric to analyze | Select "Energy" |
| **Click on Charts** | Get detailed info | Click any dot |
| **Sensitivity Slider** | Find outliers | Drag to 2σ |
| **Story Buttons** | Read narratives | Click "Dance Revolution" |

---

## Common Actions

### I want to see Pop music trends
1. Uncheck Rock, Hip-Hop, Electronic, Jazz
2. Keep only Pop checked
3. Watch Temporal Trends update

### I want to find weird songs
1. Go to Anomaly Detector
2. Select a feature
3. Increase sensitivity to 2σ
4. Click the anomalies

### I want to learn about music history
1. Scroll to Story Mode
2. Click a story button
3. Read the insights
4. Click chart points for details

### I want to compare eras
1. Use year sliders
2. Set 1900-1950 and record observations
3. Set 2000-2021 and compare
4. Notice differences

---

## Need Help?

**Dashboard not loading?**
- Ensure CSV files are present
- Check browser console (F12)
- Refresh page (Ctrl+F5)

**Charts blank?**
- Check browser console for errors
- Ensure JavaScript is enabled
- Try different browser

**Slow?**
- Close other tabs
- Use Chrome or Firefox
- Check internet connection

**Want to deploy?**
- See [DEPLOYMENT.md](DEPLOYMENT.md)
- Takes 10 minutes

**Want to learn more?**
- Read [FEATURES.md](FEATURES.md)
- Check [README.md](README.md)

---

## What's Inside

- **586,672 tracks** from Spotify
- **121 years** of music (1900-2021)
- **7 visualizations** with interactions
- **Click-based tooltips** for details
- **5 genre categories** for filtering
- **4 story narratives** for learning

---

## Share Your Link

Once deployed, share with others:

```
🎵 Check out my Music Metrics dashboard!
Explore 121 years of music evolution with interactive charts.
Built with HTML, CSS, JavaScript and Plotly.js.

[Your deployed URL here]
```

---

## Tech Stack (For Nerds)

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Charts**: Plotly.js
- **Styling**: Dark theme with teal accents
- **Animation**: Smooth scrolling (Lenis) + transitions
- **Data**: CSV parsing, real-time aggregation
- **Hosting**: Any static host (GitHub Pages, Netlify, Vercel, Firebase)

---

## That's It! 🚀

Your dashboard is ready. Explore, enjoy, and share!

**Questions?** Check the other documentation files:
- README.md - Full overview
- FEATURES.md - Detailed features
- DEPLOYMENT.md - How to deploy

---

**Happy exploring!** 🎵📊
