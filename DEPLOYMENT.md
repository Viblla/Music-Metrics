# Music Metrics - Deployment Guide

## Choose Your Deployment Platform

We'll walk through 4 free deployment options. Pick the one that suits you best!

---

## Option 1: GitHub Pages (Recommended for Beginners)

### Why GitHub Pages?
✅ Free forever  
✅ No backend needed (perfect for static sites)  
✅ Custom domain support  
✅ SSL/HTTPS included  
✅ Easy to update  

### Steps

#### 1. Create GitHub Account
- Go to [github.com](https://github.com)
- Sign up if you don't have an account
- Verify email

#### 2. Create Repository
- Click "+" → New repository
- Name: `music-metrics` (or your choice)
- Description: "Interactive music evolution analytics dashboard"
- Set to **Public** (required for free Pages)
- Check "Add README file"
- Click "Create repository"

#### 3. Add Your Files
```bash
# Clone the repo you just created
git clone https://github.com/YOUR_USERNAME/music-metrics.git
cd music-metrics

# Copy dashboard files
# Copy dashboard.html, dashboard-script-cwm.js, dashboard-styles-cwm.css
# Copy tracks.csv and artists.csv

# Create index.html that redirects to dashboard
# OR rename dashboard.html to index.html
```

#### 4. Create index.html
Create a file `index.html` in the root:
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=dashboard.html" />
</head>
<body>
    <p><a href="dashboard.html">Click here to open the dashboard</a></p>
</body>
</html>
```

#### 5. Push to GitHub
```bash
git add .
git commit -m "Initial commit: Music Metrics dashboard"
git push origin main
```

#### 6. Enable GitHub Pages
- Go to repository settings
- Scroll to "Pages" section
- Under "Source", select "main" branch
- Click "Save"
- Wait 1-2 minutes for deployment

#### 7. Access Your Site
Your site will be at:
```
https://YOUR_USERNAME.github.io/music-metrics/
```

### Updating Content
Just push new commits!
```bash
git add .
git commit -m "Update description"
git push origin main
```

---

## Option 2: Netlify (Easiest for Continuous Deployment)

### Why Netlify?
✅ Free tier very generous  
✅ Auto-deploy on push  
✅ Custom domain  
✅ SSL included  
✅ Better performance  

### Steps

#### 1. Prepare Repository
- Push your code to GitHub (from Option 1, steps 1-5)

#### 2. Sign Up on Netlify
- Go to [netlify.com](https://netlify.com)
- Click "Sign up" (use GitHub)
- Authorize Netlify to access GitHub
- Click "Authorize netlify"

#### 3. Create New Site
- Click "New site from Git"
- Choose GitHub
- Search for your `music-metrics` repo
- Click on it

#### 4. Configure Build
- Branch: `main`
- Build command: (leave empty - static site)
- Publish directory: `.` (root folder)
- Click "Deploy site"

#### 5. Wait for Deployment
- Status shows "Building"
- Changes to "Published" when ready (1-2 min)

#### 6. Access Your Site
```
https://[random-name].netlify.app/dashboard.html
```

#### 7. Custom Domain (Optional)
- Click "Domain settings"
- Add custom domain
- Update DNS records with your provider

### Auto-Deploy
Every time you push to GitHub, Netlify auto-deploys!

---

## Option 3: Vercel (Best Performance)

### Why Vercel?
✅ Lightning-fast CDN  
✅ Free tier excellent  
✅ Made by Next.js creators  
✅ Auto-deploy from GitHub  
✅ Global edge network  

### Steps

#### 1. Go to Vercel
- Visit [vercel.com](https://vercel.com)
- Click "Start Deploying"
- Sign up with GitHub

#### 2. Import Project
- Click "Import Project"
- Select "Import Git Repository"
- Paste GitHub repo URL
- Click "Continue"

#### 3. Configure Project
- Framework: "Other" (static site)
- Build Command: (leave empty)
- Output Directory: `.` 
- Click "Deploy"

#### 4. Wait for Deploy
- Deployment starts automatically
- Watch progress in dashboard
- Get URL when complete

#### 5. Access Your Site
```
https://music-metrics-[random].vercel.app/dashboard.html
```

### Custom Domain
- Project settings → Domains
- Add your domain
- Update DNS records

---

## Option 4: Firebase Hosting (For Advanced Users)

### Why Firebase?
✅ Managed by Google  
✅ Great performance  
✅ Built-in analytics  
✅ Custom domain  

### Steps

#### 1. Install Firebase CLI
```bash
npm install -g firebase-tools
```

#### 2. Sign In
```bash
firebase login
```
- Opens browser for Google login
- Authorize Firebase

#### 3. Initialize Firebase
```bash
firebase init hosting
? What do you want to use as your public directory? .
? Configure as single-page app? No
```

#### 4. Deploy
```bash
firebase deploy
```

#### 5. Get Your URL
Shows `hosting URL: https://music-metrics-[id].web.app`

---

## Quick Comparison

| Feature | GitHub Pages | Netlify | Vercel | Firebase |
|---------|-------------|---------|--------|----------|
| **Cost** | Free | Free | Free | Free |
| **Setup Time** | 15 min | 10 min | 10 min | 15 min |
| **Performance** | Good | Excellent | Excellent | Good |
| **Auto-Deploy** | Manual | Yes | Yes | Manual |
| **Custom Domain** | Yes | Yes | Yes | Yes |
| **Analytics** | No | Basic | Basic | Yes |
| **Difficulty** | Easy | Easy | Easy | Medium |

**Recommended**: Netlify or Vercel (easiest + auto-deploy)

---

## Post-Deployment Steps

### 1. Test Everything
- [ ] Dashboard loads at your URL
- [ ] All charts render
- [ ] Click tooltips work
- [ ] Genre filtering works
- [ ] Year sliders work
- [ ] Anomaly detector works
- [ ] Story mode works
- [ ] Mobile responsive
- [ ] Try on different browser

### 2. Share Your Site
```
🎵 Check out my Music Metrics dashboard!
https://your-domain.com/dashboard.html

Explore 121 years of music evolution with interactive charts, 
anomaly detection, and narrative stories. Built with HTML/CSS/JS + Plotly.
```

### 3. Add to Portfolio
- Add link to GitHub profile
- Add to resume/CV
- Share in class
- Post on social media

### 4. Monitor Performance
- Check deployment status regularly
- Ensure site stays live
- Monitor any errors (console)
- Update content if needed

---

## Updating After Deployment

### For GitHub Pages / Netlify / Vercel:
```bash
# Make changes locally
# Edit files as needed

# Push to GitHub
git add .
git commit -m "Update: your change description"
git push origin main

# Site auto-deploys! (Netlify/Vercel)
# Or manually trigger (GitHub Pages)
```

### For Firebase:
```bash
firebase deploy
```

---

## Custom Domain Setup

### DNS Configuration Example (using Namecheap)

1. Go to domain registrar
2. Find DNS settings
3. Add DNS records:
   - For Netlify: CNAME to netlify.app
   - For Vercel: Add Vercel nameservers
   - For Firebase: Add Google-provided records

4. Wait 24-48 hours for propagation
5. Verify in your platform's settings

---

## Troubleshooting

### Site shows 404
- Check file paths (case-sensitive)
- Ensure CSV files are uploaded
- Verify index.html exists in root

### Charts not loading
- CSV files in correct location
- JavaScript paths correct
- No console errors (F12)

### Slow performance
- Check file sizes
- Verify CDN working
- Look for network errors
- Test on different connection

### Domain not working
- DNS still propagating (wait 48h)
- Check DNS records correct
- Verify in platform settings
- Try different browser/DNS cache clear

---

## Security Notes

✅ CSV files are fine to share (public data)  
✅ No sensitive data in code  
✅ HTML/CSS/JS are publicly visible  
✅ HTTPS included automatically  
✅ No backend = no vulnerabilities  

---

## Performance Tips

1. **Compress images** (if you add any)
2. **Minify CSS/JS** for production
3. **Use CDN** (handled by platforms)
4. **Monitor load times** (Vercel/Firebase have tools)
5. **Test on slow connections** (DevTools → Throttle)

---

## Next Steps

1. Choose a platform (Netlify recommended)
2. Push code to GitHub
3. Connect to deployment platform
4. Wait for deployment
5. Test all features
6. Share your link!

---

## Support

If deployment fails:
1. Check platform documentation
2. Verify GitHub access
3. Clear browser cache
4. Try different browser
5. Contact platform support

---

**Deployment Guide Version**: 1.0  
**Recommended Platform**: Netlify or Vercel  
**Setup Time**: 10-15 minutes  
**Status**: Ready to deploy! ✅

Choose a platform and get your dashboard live! 🚀
