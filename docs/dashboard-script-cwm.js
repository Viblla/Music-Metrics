/* ========================================
   MUSIC METRICS DASHBOARD - COMPLETE REWRITE
   ======================================== */

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Tooltip functions for clicked points
function showTooltip(title, content) {
  const tooltip = document.getElementById('pointTooltip');
  const tooltipContent = document.getElementById('tooltipContent');
  tooltipContent.innerHTML = `<h3>${title}</h3>${content}`;
  tooltip.classList.add('active');
}

function closeTooltip() {
  document.getElementById('pointTooltip').classList.remove('active');
}

// Close tooltip when clicking outside
document.addEventListener('click', (e) => {
  const tooltip = document.getElementById('pointTooltip');
  if (tooltip && !tooltip.contains(e.target) && !e.target.closest('.plotly')) {
    closeTooltip();
  }
});

// Global data store
let allData = { tracks: [], artists: [] };
let selectedGenres = new Set(['pop', 'rock', 'hip-hop']); // Default genres

console.log('Dashboard initializing...');

// Robust CSV parser - handles quoted fields properly
function parseCSV(csvText) {
  const lines = csvText.split('\n').filter(line => line.trim());
  if (lines.length < 2) return [];
  
  const headerLine = lines[0];
  const headers = [];
  let current = '';
  let inQuotes = false;
  
  // Parse header
  for (let i = 0; i < headerLine.length; i++) {
    const char = headerLine[i];
    if (char === '"') inQuotes = !inQuotes;
    else if (char === ',' && !inQuotes) {
      headers.push(current.trim().replace(/^"|"$/g, ''));
      current = '';
    } else {
      current += char;
    }
  }
  headers.push(current.trim().replace(/^"|"$/g, ''));
  
  // Parse data rows - NO LIMIT, use all data
  const data = [];
  
  for (let i = 1; i < lines.length; i++) {
    try {
      const values = [];
      let current = '';
      let inQuotes = false;
      
      for (let j = 0; j < lines[i].length; j++) {
        const char = lines[i][j];
        if (char === '"') inQuotes = !inQuotes;
        else if (char === ',' && !inQuotes) {
          values.push(current.trim().replace(/^"|"$/g, ''));
          current = '';
        } else {
          current += char;
        }
      }
      values.push(current.trim().replace(/^"|"$/g, ''));
      
      const obj = {};
      headers.forEach((header, idx) => {
        const val = values[idx] || '';
        obj[header] = (val && !isNaN(val) && val !== '') ? parseFloat(val) : val;
      });
      
      // Extract year from release_date
      if (obj.release_date && typeof obj.release_date === 'string') {
        obj.year = parseInt(obj.release_date.substring(0, 4));
      }
      
      data.push(obj);
    } catch (e) {
      continue;
    }
  }
  
  return data;
}

// Load CSV data
async function loadData() {
  try {
    const [tracksRes, artistsRes] = await Promise.all([
      fetch('./tracks.csv'),
      fetch('./artists.csv')
    ]);
    
    if (tracksRes.ok && artistsRes.ok) {
      allData.tracks = parseCSV(await tracksRes.text());
      allData.artists = parseCSV(await artistsRes.text());
      
      // Validate data
      if (allData.tracks.length > 0) {
        const sample = allData.tracks[0];
        console.log('✓ Data loaded successfully');
        console.log('Sample track:', sample);
        console.log('Track count:', allData.tracks.length);
        console.log('Year range:', Math.min(...allData.tracks.map(t => t.year || 2000)), '-', Math.max(...allData.tracks.map(t => t.year || 2000)));
      }
    } else {
      throw new Error('CSV fetch failed');
    }
  } catch (error) {
    console.error('Data load failed:', error);
    allData.tracks = generateMockTracks(5000);
  }
}

// Generate mock data
function generateMockTracks(count) {
  const tracks = [];
  for (let i = 0; i < count; i++) {
    const year = 1900 + Math.floor(Math.random() * 124);
    tracks.push({
      id: `mock_${i}`,
      name: `Track ${i}`,
      year: year,
      release_date: `${year}-${String(Math.floor(Math.random() * 12) + 1).padStart(2, '0')}-01`,
      danceability: Math.random(),
      energy: Math.random(),
      acousticness: Math.random(),
      valence: Math.random(),
      tempo: 60 + Math.random() * 140,
      loudness: -15 + Math.random() * 12,
      popularity: Math.floor(Math.random() * 100),
      speechiness: Math.random(),
      liveness: Math.random(),
      instrumentalness: Math.random()
    });
  }
  return tracks;
}

// Classify track into genre based on audio features
function classifyGenre(track) {
  const energy = track.energy || 0;
  const danceability = track.danceability || 0;
  const acousticness = track.acousticness || 0;
  const valence = track.valence || 0;
  const tempo = track.tempo || 0;
  
  // Simple heuristic-based genre classification
  if (acousticness > 0.6) return 'jazz'; // High acousticness
  if (energy > 0.7 && danceability > 0.7) return 'electronic'; // High energy & dance
  if (energy > 0.6 && danceability > 0.5 && valence < 0.6) return 'hip-hop'; // Medium-high energy, good danceability, moderate valence
  if (energy > 0.7) return 'rock'; // High energy
  if (danceability > 0.7) return 'pop'; // High danceability
  if (valence < 0.4) return 'jazz'; // Low valence
  
  return 'pop'; // Default
}

// Update hero stats
function updateHeroStats() {
  if (allData.tracks.length === 0) return;
  
  const years = allData.tracks.map(t => t.year).filter(y => y && y > 0);
  const minYear = Math.min(...years);
  const maxYear = Math.max(...years);
  
  // Update slider ranges dynamically
  document.getElementById('yearStart').min = minYear;
  document.getElementById('yearStart').max = maxYear;
  document.getElementById('yearStart').value = minYear;
  
  document.getElementById('yearEnd').min = minYear;
  document.getElementById('yearEnd').max = maxYear;
  document.getElementById('yearEnd').value = maxYear;
  
  document.getElementById('yearDisplay').textContent = `${minYear} - ${maxYear}`;
  
  document.querySelector('.hero-stats').innerHTML = `
    <div class="stat"><h3>${allData.tracks.length.toLocaleString()}</h3><p>Tracks</p></div>
    <div class="stat"><h3>${maxYear - minYear}</h3><p>Years</p></div>
    <div class="stat"><h3>${minYear}</h3><p>From</p></div>
    <div class="stat"><h3>${maxYear}</h3><p>To</p></div>
  `;
}

// TRENDS CHART
function loadTrendsChart() {
  if (allData.tracks.length === 0) {
    console.warn('No data loaded yet');
    return;
  }
  
  try {
    const yearStart = parseInt(document.getElementById('yearStart').value);
    const yearEnd = parseInt(document.getElementById('yearEnd').value);
    const feature = document.getElementById('featureSelect').value;
    
    console.log(`Trends: Filtering ${yearStart} - ${yearEnd}, feature: ${feature}`);
    
    // Filter by year range
    const filtered = allData.tracks.filter(t => {
      const year = t.year || 0;
      if (year < yearStart || year > yearEnd) return false;
      
      // Filter by selected genres
      const genre = classifyGenre(t);
      return selectedGenres.has(genre);
    });
    
    console.log(`Filtered: ${filtered.length} tracks in range`);
    
    if (filtered.length === 0) {
      console.warn('No tracks in selected range');
      return;
    }
    
    // Aggregate by year
    const yearData = {};
    filtered.forEach(track => {
      const year = track.year || 0;
      const value = track[feature];
      
      if (year > 0 && value !== undefined && !isNaN(value)) {
        if (!yearData[year]) yearData[year] = [];
        yearData[year].push(value);
      }
    });
    
    // Calculate averages
    const years = Object.keys(yearData).map(Number).sort((a, b) => a - b);
    const values = years.map(year => {
      const avg = yearData[year].reduce((a, b) => a + b, 0) / yearData[year].length;
      return Math.round(avg * 1000) / 1000;
    });
    
    console.log(`Trends: Rendering ${years.length} data points`, {
      years: years.slice(0, 5),
      values: values.slice(0, 5)
    });
    
    const trace = {
      x: years,
      y: values,
      type: 'scatter',
      mode: 'lines+markers',
      name: feature,
      line: { color: '#00d9a3', width: 2 },
      marker: { size: 4, color: '#00d9a3' },
      fill: 'tozeroy',
      fillcolor: 'rgba(0, 217, 163, 0.1)'
    };
    
    const layout = {
      title: { text: `${feature.charAt(0).toUpperCase() + feature.slice(1)} Over Time (${yearStart} - ${yearEnd})`, font: { color: '#fff', size: 16 } },
      xaxis: { 
        title: 'Year', 
        tickfont: { color: '#ccc' }, 
        gridcolor: '#2a2a2a',
        type: 'linear'
      },
      yaxis: { 
        title: feature, 
        tickfont: { color: '#ccc' }, 
        gridcolor: '#2a2a2a',
        range: [0, 1]
      },
      plot_bgcolor: '#1a1a1a',
      paper_bgcolor: '#0a0a0a',
      margin: { l: 60, r: 40, t: 40, b: 50 },
      hovermode: 'x unified'
    };
    
    Plotly.newPlot('trendsChart', [trace], layout, {responsive: true, displayModeBar: false});
    
    // Add click handler for detailed tooltips
    document.getElementById('trendsChart').on('plotly_click', (data) => {
      if (data.points.length > 0) {
        const point = data.points[0];
        const year = point.x;
        const value = point.y;
        const trackCount = yearData[year] ? yearData[year].length : 0;
        
        // Calculate additional stats for this year
        const yearTracks = yearData[year] || [];
        const min = Math.min(...yearTracks);
        const max = Math.max(...yearTracks);
        const median = yearTracks.sort((a, b) => a - b)[Math.floor(yearTracks.length / 2)];
        
        const featureName = feature.charAt(0).toUpperCase() + feature.slice(1);
        const content = `
          <p><strong>Year:</strong> ${year}</p>
          <p><strong>${featureName} Average:</strong> ${value.toFixed(3)}</p>
          <p><strong>Tracks Analyzed:</strong> ${trackCount}</p>
          <p><strong>Range:</strong> ${min.toFixed(3)} - ${max.toFixed(3)}</p>
          <p><strong>Median:</strong> ${median.toFixed(3)}</p>
          <p><strong>Trend Context:</strong> This year's ${featureName.toLowerCase()} level reflects broader music industry patterns from that era.</p>
        `;
        showTooltip(`${featureName} in ${year}`, content);
      }
    });
    console.log('✓ Trends chart rendered');
  } catch (e) {
    console.error('Trends chart error:', e);
  }
}

// ANOMALIES CHART
function loadAnomaliesChart() {
  if (allData.tracks.length === 0) return;
  
  try {
    const feature = document.getElementById('anomalyFeature').value;
    const sensitivity = parseFloat(document.getElementById('sensitivitySlider').value);
    
    const values = allData.tracks
      .map(t => t[feature])
      .filter(v => v !== undefined && !isNaN(v));
    
    if (values.length === 0) return;
    
    // Calculate statistics
    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    const variance = values.reduce((sq, n) => sq + Math.pow(n - mean, 2), 0) / values.length;
    const stdDev = Math.sqrt(variance);
    const threshold = sensitivity * stdDev;
    
    // Find anomalies
    const anomalies = allData.tracks
      .map((t, idx) => ({
        value: t[feature],
        year: t.year,
        idx: idx,
        zscore: (t[feature] - mean) / stdDev
      }))
      .filter(t => t.value !== undefined && Math.abs(t.value - mean) > threshold)
      .slice(0, 100);
    
    console.log(`Anomalies: Found ${anomalies.length} with threshold ${threshold.toFixed(3)}`);
    
    const trace = {
      x: anomalies.map((_, i) => i),
      y: anomalies.map(a => Math.round(a.value * 1000) / 1000),
      text: anomalies.map(a => `Year: ${a.year}, Z-Score: ${a.zscore.toFixed(2)}`),
      hovertemplate: '%{text}<extra></extra>',
      type: 'scatter',
      mode: 'markers',
      marker: { size: 8, color: '#ffd700' }
    };
    
    const layout = {
      title: { text: `${feature.charAt(0).toUpperCase() + feature.slice(1)} Anomalies (>${sensitivity.toFixed(1)}σ)`, font: { color: '#fff' } },
      xaxis: { title: 'Index', tickfont: { color: '#ccc' } },
      yaxis: { title: feature, tickfont: { color: '#ccc' }, gridcolor: '#2a2a2a' },
      plot_bgcolor: '#1a1a1a',
      paper_bgcolor: '#0a0a0a',
      margin: { l: 60, r: 40, t: 40, b: 50 }
    };
    
    Plotly.newPlot('anomaliesChart', [trace], layout, { responsive: true, displayModeBar: false });
    
    // Add click handler for detailed anomaly tooltips
    document.getElementById('anomaliesChart').on('plotly_click', (data) => {
      if (data.points.length > 0) {
        const point = data.points[0];
        const index = point.x;
        const anomaly = anomalies[index];
        
        if (anomaly) {
          const featureName = feature.charAt(0).toUpperCase() + feature.slice(1);
          const severity = Math.abs(anomaly.zscore) > 3 ? 'SEVERE' : Math.abs(anomaly.zscore) > 2 ? 'STRONG' : 'MODERATE';
          const direction = anomaly.zscore > 0 ? 'ABOVE' : 'BELOW';
          
          const content = `
            <p><strong>Anomaly Index:</strong> ${index + 1} / ${anomalies.length}</p>
            <p><strong>Year:</strong> ${anomaly.year}</p>
            <p><strong>${featureName} Value:</strong> ${anomaly.value.toFixed(3)}</p>
            <p><strong>Z-Score:</strong> ${anomaly.zscore.toFixed(2)}</p>
            <p><strong>Severity:</strong> ${severity}</p>
            <p><strong>Status:</strong> ${direction} average by ${Math.abs(anomaly.zscore).toFixed(2)} standard deviations</p>
            <p><strong>Threshold Applied:</strong> >${sensitivity.toFixed(1)}σ</p>
            <p><strong>Interpretation:</strong> This data point is statistically unusual for the dataset, indicating an outlier moment in music history.</p>
          `;
          showTooltip(`${featureName} Anomaly - ${anomaly.year}`, content);
        }
      }
    });
    
  } catch (e) {
    console.error('Anomalies chart error:', e);
  }
}

// STORY CHARTS
function loadStoryChart() {
  if (allData.tracks.length === 0) return;
  
  try {
    const storyType = document.querySelector('.story-btn.active').dataset.story;
    const storyMeta = {
      acoustic: {
        title: 'THE GREAT ACOUSTIC DECLINE',
        desc: 'How music shifted from acoustic to digital production over decades',
        feature: 'acousticness',
        trend: 'Acoustic instruments dominated early music production but steadily declined as technology enabled synthetic and electronic sounds. The 2000s saw a brief resurgence with indie rock, but overall trend remains downward.',
        keyPeriod: 'The steepest decline occurred between 1980s-2000s when electronic production became mainstream.',
        meaning: 'This shift reflects technological advancement and changing consumer preferences. Digital production allows for greater control, precision, and creative possibilities that pure acoustic recording cannot match.'
      },
      energy: {
        title: 'RISING ENERGY LEVELS',
        desc: 'Modern tracks are getting more intense and energetic',
        feature: 'energy',
        trend: 'Overall energy levels in popular music have increased significantly over the past 50 years. Louder mastering, faster drums, and more aggressive production have become the norm.',
        keyPeriod: 'The most dramatic increase happened between 1990s-2010s with EDM and dubstep influence.',
        meaning: 'Higher energy correlates with increased stimulation and intensity in music, reflecting faster pace of modern life and audience expectations for more engaging, dynamic content.'
      },
      dance: {
        title: 'THE DANCE REVOLUTION',
        desc: 'Danceability peaked in the 2010s with EDM and pop domination',
        feature: 'danceability',
        trend: 'Danceability metrics show a clear explosion in the 2000s-2010s as EDM, house, and dance-pop became globally dominant. Electronic beats and 4/4 time signatures became industry standard.',
        keyPeriod: 'The revolution accelerated between 2005-2015 as digital production and streaming enabled global distribution.',
        meaning: 'Increased danceability means music became more rhythmically predictable and beat-driven. This accessibility made it easier for mass audiences to connect with music on the dance floor and in playlists.'
      },
      valence: {
        title: 'MOOD SWINGS IN MUSIC',
        desc: 'The emotional tone of music has fluctuated dramatically',
        feature: 'valence',
        trend: 'Valence (musical positiveness/cheerfulness) shows cyclical patterns. The 1980s-90s saw upbeat pop, 2000s got darker with emo and alternative music, then recovered with upbeat electronic pop in 2010s.',
        keyPeriod: 'Major swing occurred around 2008-2010 when darker moods gave way to brighter electronic pop.',
        meaning: 'Mood fluctuations in commercial music reflect broader cultural and economic cycles. Happier music tends to emerge during prosperous times, while melancholy dominates during economic uncertainty.'
      }
    };
    
    const meta = storyMeta[storyType];
    const feature = meta.feature;
    
    // Aggregate by decade
    const decadeData = {};
    allData.tracks.forEach(t => {
      const decade = Math.floor(t.year / 10) * 10;
      const value = t[feature];
      
      if (decade > 0 && value !== undefined && !isNaN(value)) {
        if (!decadeData[decade]) decadeData[decade] = [];
        decadeData[decade].push(value);
      }
    });
    
    // Calculate averages and statistics
    const decades = Object.keys(decadeData).map(Number).sort((a, b) => a - b);
    const values = decades.map(d => {
      const avg = decadeData[d].reduce((a, b) => a + b, 0) / decadeData[d].length;
      return Math.round(avg * 1000) / 1000;
    });
    
    const trace = {
      x: decades.map(d => `${d}s`),
      y: values,
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#ffd700', width: 3 },
      marker: { size: 8, color: '#ffd700' },
      fill: 'tozeroy',
      fillcolor: 'rgba(255, 215, 0, 0.1)'
    };
    
    const layout = {
      title: { text: meta.title, font: { color: '#fff', size: 16 } },
      xaxis: { title: 'Decade', tickfont: { color: '#ccc' } },
      yaxis: { title: feature, tickfont: { color: '#ccc' }, gridcolor: '#2a2a2a' },
      plot_bgcolor: '#1a1a1a',
      paper_bgcolor: '#0a0a0a',
      margin: { l: 60, r: 40, t: 40, b: 50 }
    };
    
    // Update story header
    document.getElementById('storyTitle').textContent = meta.title;
    document.getElementById('storyDescription').textContent = meta.desc;
    
    // Update insight cards
    document.getElementById('trendText').textContent = meta.trend;
    document.getElementById('keyPeriod').textContent = meta.keyPeriod;
    document.getElementById('meaningText').textContent = meta.meaning;
    
    // Generate timeline content with decade-by-decade breakdown
    const timelineHTML = decades.map((decade, idx) => {
      const value = values[idx];
      const prevValue = idx > 0 ? values[idx - 1] : null;
      let changeIndicator = '';
      if (prevValue !== null) {
        const delta = value - prevValue;
        changeIndicator = delta > 0 ? ' ↑' : delta < 0 ? ' ↓' : ' →';
      }
      return `
        <div class="timeline-item">
          <div class="period">${decade}s</div>
          <div class="value">${value.toFixed(2)}${changeIndicator}</div>
          <div class="description">
            ${Math.round(decadeData[decade].length)} tracks analyzed
            ${idx > 0 ? `<br/>Change: ${((value - prevValue) * 100).toFixed(1)}%` : ''}
          </div>
        </div>
      `;
    }).join('');
    
    document.getElementById('timelineContent').innerHTML = timelineHTML;
    
    Plotly.newPlot('storyChart', [trace], layout, { responsive: true, displayModeBar: false });
    
    // Add click handler for storyChart
    document.getElementById('storyChart').on('plotly_click', (data) => {
      if (data.points.length > 0) {
        const point = data.points[0];
        const decade = point.x;
        const value = point.y.toFixed(2);
        const decadeNum = parseInt(decade);
        const trackCount = decadeData[decadeNum].length;
        const content = `
          <p><strong>Decade:</strong> ${decade}</p>
          <p><strong>${feature.charAt(0).toUpperCase() + feature.slice(1)} Score:</strong> ${value}</p>
          <p><strong>Tracks Analyzed:</strong> ${trackCount.toLocaleString()}</p>
          <p><strong>Meaning:</strong> ${meta.meaning}</p>
          <p>This decade's ${value} score contributes to the overall narrative of music evolution: ${meta.trend}</p>
        `;
        showTooltip(`${meta.title} - ${decade}`, content);
      }
    });
    
  } catch (e) {
    console.error('Story chart error:', e);
  }
}

// Event listeners
function setupListeners() {
  // Trends controls - year range sliders
  const yearStartEl = document.getElementById('yearStart');
  const yearEndEl = document.getElementById('yearEnd');
  const yearDisplayEl = document.getElementById('yearDisplay');
  
  if (yearStartEl && yearEndEl && yearDisplayEl) {
    yearStartEl.addEventListener('input', (e) => {
      let start = parseInt(e.target.value);
      let end = parseInt(yearEndEl.value);
      
      // Ensure start doesn't exceed end
      if (start > end) {
        start = end;
        yearStartEl.value = start;
      }
      
      yearDisplayEl.textContent = `${start} - ${end}`;
      console.log(`Year range changed: ${start} - ${end}`);
      loadTrendsChart();
    });
    
    yearEndEl.addEventListener('input', (e) => {
      let start = parseInt(yearStartEl.value);
      let end = parseInt(e.target.value);
      
      // Ensure end doesn't go below start
      if (end < start) {
        end = start;
        yearEndEl.value = end;
      }
      
      yearDisplayEl.textContent = `${start} - ${end}`;
      console.log(`Year range changed: ${start} - ${end}`);
      loadTrendsChart();
    });
  }
  
  const featureSelect = document.getElementById('featureSelect');
  if (featureSelect) {
    featureSelect.addEventListener('change', (e) => {
      console.log(`Feature changed: ${e.target.value}`);
      loadTrendsChart();
    });
  }
  
  // Genre pill listeners
  document.querySelectorAll('.genre-pills .pill').forEach(pill => {
    pill.addEventListener('click', function(e) {
      const genre = this.dataset.genre;
      
      // Toggle genre selection
      if (selectedGenres.has(genre)) {
        selectedGenres.delete(genre);
        this.classList.remove('active');
      } else {
        selectedGenres.add(genre);
        this.classList.add('active');
      }
      
      console.log(`Genre toggled: ${genre}, Selected:`, Array.from(selectedGenres));
      loadTrendsChart();
    });
  });
  
  // Anomaly controls
  const anomalyFeature = document.getElementById('anomalyFeature');
  const sensitivitySlider = document.getElementById('sensitivitySlider');
  const sensitivityDisplay = document.getElementById('sensitivityDisplay');
  
  if (anomalyFeature) {
    anomalyFeature.addEventListener('change', loadAnomaliesChart);
  }
  
  if (sensitivitySlider && sensitivityDisplay) {
    sensitivitySlider.addEventListener('input', (e) => {
      sensitivityDisplay.textContent = parseFloat(e.target.value).toFixed(1);
      loadAnomaliesChart();
    });
  }
  
  // Story mode
  document.querySelectorAll('.story-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.story-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      loadStoryChart();
    });
  });
  
  // Perfect Hit listeners
  const decadeSelect = document.getElementById('decadeSelect');
  if (decadeSelect) {
    decadeSelect.addEventListener('change', loadPerfectHitChart);
  }
  
  // Genre Dive listeners
  document.querySelectorAll('.genre-compare').forEach(cb => {
    cb.addEventListener('change', loadGenreDiveChart);
  });
  
  const genreDiveFeature = document.getElementById('genreDiveFeature');
  if (genreDiveFeature) {
    genreDiveFeature.addEventListener('change', loadGenreDiveChart);
  }
  
  // Hit Blueprint listeners
  const eraSelect = document.getElementById('eraSelect');
  if (eraSelect) {
    eraSelect.addEventListener('change', loadHitSongBlueprint);
  }
  
  // Feature Space Explorer listeners
  const xAxisSelect = document.getElementById('xAxisSelect');
  const yAxisSelect = document.getElementById('yAxisSelect');
  const colorBySelect = document.getElementById('colorBySelect');
  
  if (xAxisSelect) xAxisSelect.addEventListener('change', loadFeatureSpaceExplorer);
  if (yAxisSelect) yAxisSelect.addEventListener('change', loadFeatureSpaceExplorer);
  if (colorBySelect) colorBySelect.addEventListener('change', loadFeatureSpaceExplorer);
  
  console.log('✓ All event listeners attached');
}

// ===== 1. PERFECT HIT: Popularity Predictor by Decade =====
function loadPerfectHitChart() {
  const decadeSelect = document.getElementById('decadeSelect').value;
  
  // Filter data by decade
  let filteredData = allData.tracks;
  
  if (decadeSelect !== 'all') {
    const decadeNum = parseInt(decadeSelect);
    filteredData = allData.tracks.filter(t => {
      const year = t.year || 2000;
      return year >= decadeNum && year < decadeNum + 10;
    });
  }
  
  // Calculate correlation with popularity
  const features = ['energy', 'danceability', 'valence', 'acousticness', 'tempo', 'loudness'];
  const correlations = {};
  
  features.forEach(feature => {
    let sumXY = 0, sumX = 0, sumY = 0, sumX2 = 0, sumY2 = 0, n = 0;
    
    filteredData.forEach(track => {
      if (track[feature] !== undefined && track.popularity !== undefined) {
        const x = feature === 'tempo' ? track[feature] / 200 : track[feature];
        const y = track.popularity / 100;
        sumXY += x * y;
        sumX += x;
        sumY += y;
        sumX2 += x * x;
        sumY2 += y * y;
        n++;
      }
    });
    
    if (n > 0) {
      const numerator = n * sumXY - sumX * sumY;
      const denominator = Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));
      correlations[feature] = denominator !== 0 ? numerator / denominator : 0;
    }
  });
  
  // Create bar chart
  const features_sorted = Object.keys(correlations).sort((a, b) => Math.abs(correlations[b]) - Math.abs(correlations[a]));
  const values = features_sorted.map(f => correlations[f]);
  const colors = values.map(v => v > 0 ? '#00d9a3' : '#ff6b6b');
  
  const trace = {
    x: features_sorted,
    y: values,
    type: 'bar',
    marker: { color: colors },
  };
  
  const layout = {
    title: `Popularity Correlations - ${decadeSelect === 'all' ? 'All Time' : decadeSelect}`,
    xaxis: { title: 'Audio Feature' },
    yaxis: { title: 'Correlation with Popularity' },
    paper_bgcolor: '#0a0a0a',
    plot_bgcolor: '#1a1a1a',
    font: { color: '#fff' },
    margin: { l: 60, r: 40, t: 60, b: 60 },
    height: 400
  };
  
  Plotly.newPlot('perfectHitChart', [trace], layout, {responsive: true});
  
  // Add click handler for perfectHitChart
  document.getElementById('perfectHitChart').on('plotly_click', (data) => {
    if (data.points.length > 0) {
      const point = data.points[0];
      const feature = point.fullData.name;
      const correlation = point.y.toFixed(2);
      const decade = point.x;
      const content = `
        <p><strong>Feature:</strong> ${feature}</p>
        <p><strong>Decade:</strong> ${decade}</p>
        <p><strong>Correlation:</strong> ${correlation}</p>
        <p><strong>Meaning:</strong> In the ${decade}, ${feature} has a correlation of ${correlation} with popularity. ${correlation > 0.3 ? 'This strong positive correlation suggests ' + feature + ' is a key factor in hit songs.' : correlation > 0 ? 'This moderate positive correlation suggests ' + feature + ' contributes to song popularity.' : 'This weak or negative correlation suggests ' + feature + ' is not a primary driver of popularity.'}</p>
      `;
      showTooltip(`${feature.charAt(0).toUpperCase() + feature.slice(1)} Analysis`, content);
    }
  });
}


// ===== 3. GENRE DEEP DIVE =====
function loadGenreDiveChart() {
  const feature = document.getElementById('genreDiveFeature').value;
  const selectedGenres = Array.from(document.querySelectorAll('.genre-compare:checked')).map(cb => cb.value);
  
  if (selectedGenres.length === 0) {
    document.getElementById('genreDiveInsight').innerHTML = '<p>Please select at least one genre.</p>';
    return;
  }
  
  // Calculate average features by genre and year
  const genreYearData = {};
  selectedGenres.forEach(genre => {
    genreYearData[genre] = {};
  });
  
  allData.tracks.forEach(track => {
    const genre = classifyGenre(track);
    const year = track.year || 2000;
    
    if (selectedGenres.includes(genre)) {
      if (!genreYearData[genre][year]) {
        genreYearData[genre][year] = { values: [], count: 0 };
      }
      genreYearData[genre][year].values.push(track[feature] || 0);
      genreYearData[genre][year].count++;
    }
  });
  
  // Create traces for each genre
  const traces = selectedGenres.map(genre => {
    const years = Object.keys(genreYearData[genre]).sort((a, b) => a - b);
    const values = years.map(year => {
      const data = genreYearData[genre][year];
      return data.values.reduce((a, b) => a + b, 0) / data.values.length;
    });
    
    const genreColors = {
      pop: '#ffd700',
      rock: '#ff6b6b',
      'hip-hop': '#00b8ff',
      electronic: '#ff00ff',
      jazz: '#00d9a3'
    };
    
    return {
      x: years,
      y: values,
      name: genre.toUpperCase(),
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: genreColors[genre], width: 3 },
      marker: { size: 6 }
    };
  });
  
  const layout = {
    title: `${feature.charAt(0).toUpperCase() + feature.slice(1)} by Genre Over Time`,
    xaxis: { title: 'Year' },
    yaxis: { title: feature.charAt(0).toUpperCase() + feature.slice(1) },
    paper_bgcolor: '#0a0a0a',
    plot_bgcolor: '#1a1a1a',
    font: { color: '#fff' },
    hovermode: 'x unified',
    margin: { l: 60, r: 40, t: 60, b: 60 },
    height: 400,
    legend: { x: 0.02, y: 0.98, bgcolor: 'rgba(0,0,0,0.8)' }
  };
  
  Plotly.newPlot('genreDiveChart', traces, layout, {responsive: true});
  
  // Add click handler for genreDiveChart
  document.getElementById('genreDiveChart').on('plotly_click', (data) => {
    if (data.points.length > 0) {
      const point = data.points[0];
      const genre = point.fullData.name;
      const year = point.x;
      const value = point.y.toFixed(2);
      const content = `
        <p><strong>Genre:</strong> ${genre}</p>
        <p><strong>Year:</strong> ${year}</p>
        <p><strong>${feature.charAt(0).toUpperCase() + feature.slice(1)}:</strong> ${value}</p>
        <p><strong>Meaning:</strong> In ${year}, ${genre} music had a ${feature} level of ${value}. This indicates the ${feature === 'energy' ? 'intensity and activity level' : feature === 'danceability' ? 'how suitable for dancing' : feature === 'valence' ? 'musical positivity/mood' : feature === 'acousticness' ? 'use of acoustic instruments' : 'popularity'} of ${genre} songs during this period.</p>
      `;
      showTooltip(`${genre.toUpperCase()} - ${feature}`, content);
    }
  });
}

// ===== 4. HIT SONG BLUEPRINT BY ERA =====
function loadHitSongBlueprint() {
  const eraSelect = document.getElementById('eraSelect').value;
  const eraStart = parseInt(eraSelect);
  const eraEnd = eraStart + 10;
  
  // Filter to top 25% most popular tracks in era
  const eraData = allData.tracks.filter(t => {
    const year = t.year || 2000;
    return year >= eraStart && year < eraEnd;
  });
  
  const sorted = eraData.sort((a, b) => (b.popularity || 0) - (a.popularity || 0));
  const hits = sorted.slice(0, Math.ceil(sorted.length * 0.25));
  const nonHits = sorted.slice(Math.ceil(sorted.length * 0.25));
  
  // Calculate statistics
  const features = ['energy', 'danceability', 'valence', 'acousticness'];
  const stats = {};
  
  features.forEach(f => {
    const hitValues = hits.map(t => t[f] || 0);
    const nonHitValues = nonHits.map(t => t[f] || 0);
    
    const hitAvg = hitValues.reduce((a, b) => a + b, 0) / hitValues.length;
    const nonHitAvg = nonHitValues.reduce((a, b) => a + b, 0) / nonHitValues.length;
    
    stats[f] = { hit: hitAvg, nonHit: nonHitAvg, diff: hitAvg - nonHitAvg };
  });
  
  // Create comparison chart
  const traces = [
    {
      x: Object.keys(stats),
      y: Object.values(stats).map(s => s.hit),
      name: 'Hit Songs (Top 25%)',
      type: 'bar',
      marker: { color: '#00d9a3' }
    },
    {
      x: Object.keys(stats),
      y: Object.values(stats).map(s => s.nonHit),
      name: 'Other Songs',
      type: 'bar',
      marker: { color: '#666' }
    }
  ];
  
  const layout = {
    title: `Hit Song Blueprint - ${eraSelect}s`,
    xaxis: { title: 'Audio Feature' },
    yaxis: { title: 'Average Value' },
    paper_bgcolor: '#0a0a0a',
    plot_bgcolor: '#1a1a1a',
    font: { color: '#fff' },
    barmode: 'group',
    margin: { l: 60, r: 40, t: 60, b: 60 },
    height: 400,
    legend: { x: 0.02, y: 0.98, bgcolor: 'rgba(0,0,0,0.8)' }
  };
  
  Plotly.newPlot('blueprintChart', traces, layout, {responsive: true});
  
  // Add click handler for blueprintChart
  document.getElementById('blueprintChart').on('plotly_click', (data) => {
    if (data.points.length > 0) {
      const point = data.points[0];
      const feature = point.fullData.name;
      const value = point.y.toFixed(2);
      const year = point.x;
      const isHit = point.fullData.marker.color === '#00d9a3';
      const content = `
        <p><strong>Feature:</strong> ${feature}</p>
        <p><strong>Year:</strong> ${year}</p>
        <p><strong>Value:</strong> ${value}</p>
        <p><strong>Type:</strong> ${isHit ? 'Hit Songs' : 'Other Songs'}</p>
        <p><strong>Meaning:</strong> In the ${year}s, ${isHit ? 'hit' : 'non-hit'} songs had a ${feature} level of ${value}. ${isHit ? 'This is a characteristic of successful songs' : 'This is typical for songs that did not become hits'} during this era.</p>
      `;
      showTooltip(`${feature} - ${isHit ? 'Hits' : 'Others'}`, content);
    }
  });
  
  // Click handler for blueprintChart added below
  document.getElementById('blueprintChart').on('plotly_click', (data) => {
    if (data.points.length > 0) {
      const point = data.points[0];
      const feature = point.fullData.name;
      const value = point.y.toFixed(2);
      const year = point.x;
      const isHit = point.fullData.marker.color === '#00d9a3';
      const content = `
        <p><strong>Feature:</strong> ${feature}</p>
        <p><strong>Year:</strong> ${year}</p>
        <p><strong>Value:</strong> ${value}</p>
        <p><strong>Type:</strong> ${isHit ? 'Hit Songs' : 'Other Songs'}</p>
        <p><strong>Meaning:</strong> In the ${year}s, ${isHit ? 'hit' : 'non-hit'} songs had a ${feature} level of ${value}. ${isHit ? 'This is a characteristic of successful songs' : 'This is typical for songs that did not become hits'} during this era.</p>
      `;
      showTooltip(`${feature} - ${isHit ? 'Hits' : 'Others'}`, content);
    }
  });
}

// ===== 4. FEATURE SPACE EXPLORER =====
function loadFeatureSpaceExplorer() {
  const xFeature = document.getElementById('xAxisSelect').value;
  const yFeature = document.getElementById('yAxisSelect').value;
  const colorBy = document.getElementById('colorBySelect').value;
  
  // Sample data for performance (every 10th track if > 10K)
  const sampleData = allData.tracks.length > 10000 
    ? allData.tracks.filter((_, i) => i % Math.ceil(allData.tracks.length / 10000) === 0)
    : allData.tracks;
  
  // Prepare data
  const trace = {
    x: sampleData.map(t => t[xFeature] || 0),
    y: sampleData.map(t => t[yFeature] || 0),
    mode: 'markers',
    type: 'scatter',
    marker: {
      size: 5,
      opacity: 0.5,
      color: colorBy === 'year' 
        ? sampleData.map(t => t.year || 2000)
        : colorBy === 'popularity'
        ? sampleData.map(t => t.popularity || 0)
        : sampleData.map(t => {
            const genre = classifyGenre(t);
            const genreMap = { pop: 0, rock: 1, 'hip-hop': 2, electronic: 3, jazz: 4 };
            return genreMap[genre] || 0;
          }),
      colorscale: colorBy === 'year' ? 'Viridis' : colorBy === 'popularity' ? 'Blues' : 'Plasma',
      showscale: true,
      colorbar: {
        title: colorBy.charAt(0).toUpperCase() + colorBy.slice(1),
        thickness: 20,
        len: 0.7
      }
    },
    text: sampleData.map(t => `<b>${t.name || 'Track'}</b><br>Popularity: ${t.popularity}`),
    hovertemplate: '<b>%{text}</b><br>' + xFeature + ': %{x:.2f}<br>' + yFeature + ': %{y:.2f}<extra></extra>'
  };
  
  const layout = {
    title: `${xFeature.charAt(0).toUpperCase() + xFeature.slice(1)} vs ${yFeature.charAt(0).toUpperCase() + yFeature.slice(1)} (${sampleData.length.toLocaleString()} tracks)`,
    xaxis: { title: xFeature.charAt(0).toUpperCase() + xFeature.slice(1) },
    yaxis: { title: yFeature.charAt(0).toUpperCase() + yFeature.slice(1) },
    paper_bgcolor: '#0a0a0a',
    plot_bgcolor: '#1a1a1a',
    font: { color: '#fff' },
    hovermode: 'closest',
    margin: { l: 60, r: 80, t: 60, b: 60 },
    height: 500
  };
  
  Plotly.newPlot('explorerChart', [trace], layout, {responsive: true, displayModeBar: false});
  
  // Add click handler for explorerChart
  document.getElementById('explorerChart').on('plotly_click', (data) => {
    if (data.points.length > 0) {
      const point = data.points[0];
      const xVal = point.x.toFixed(2);
      const yVal = point.y.toFixed(2);
      const colorVal = point.text ? point.text : 'N/A';
      const content = `
        <p><strong>X Axis (${xFeature}):</strong> ${xVal}</p>
        <p><strong>Y Axis (${yFeature}):</strong> ${yVal}</p>
        <p><strong>Color (${colorBy}):</strong> ${colorVal}</p>
        <p><strong>Meaning:</strong> This track has ${xFeature} of ${xVal} and ${yFeature} of ${yVal}. This combination places it in a specific region of the audio feature space, indicating its musical characteristics relative to the overall dataset.</p>
      `;
      showTooltip(`Track Details`, content);
    }
  });
}

async function init() {
  console.log('Loading data...');
  await loadData();
  
  if (allData.tracks.length > 0) {
    console.log('Data ready, rendering...');
    updateHeroStats();
    
    setTimeout(() => {
      loadTrendsChart();
      loadAnomaliesChart();
      loadStoryChart();
      loadPerfectHitChart();
      loadGenreDiveChart();
      loadHitSongBlueprint();
      loadFeatureSpaceExplorer();
      setupListeners();
      console.log('✓ Dashboard ready!');
    }, 100);
  }
}

// Start when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
