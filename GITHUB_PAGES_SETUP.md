# 🚀 GitHub Pages Setup - Step by Step

## ⚠️ IMPORTANT: Manual Setup Required

GitHub Pages **must be enabled manually** in the repository settings. The workflows alone are not enough.

## 📋 Exact Steps to Enable GitHub Pages

### Step 1: Go to Repository
**Visit**: https://github.com/kamlesh9876/E-Commerce-Sales-Performance-Analysis

### Step 2: Navigate to Settings
1. Click the **"Settings"** tab (top navigation bar)
2. Scroll down to find **"Pages"** in the left sidebar menu

### Step 3: Configure GitHub Pages
In the Pages section, set these options:

#### Source Section:
- **Source**: Select "Deploy from a branch" 
- **Branch**: Select "master" from dropdown
- **Folder**: Select "/ (root)" from dropdown

#### Click **"Save"** button

### Step 4: Wait for Deployment
- GitHub will show a yellow dot: "Build in progress"
- Wait 2-5 minutes
- Status will change to green with your site URL

## 🌐 Your Live URLs (After Setup)

**Main Site**: https://kamlesh9876.github.io/E-Commerce-Sales-Performance-Analysis/
**Dashboard**: https://kamlesh9876.github.io/E-Commerce-Sales-Performance-Analysis/dashboard.html

## 🔍 What Should Happen

1. **After enabling Pages**, GitHub will automatically:
   - Build your site from the master branch
   - Deploy all files to GitHub Pages
   - Create a live URL

2. **Your index.html** will redirect to dashboard.html automatically

3. **All files will be available**:
   - dashboard.html (main dashboard)
   - data/ (processed data)
   - reports/ (analysis results)
   - sql/ (SQL scripts)
   - powerbi/ (Power BI guide)

## ⚡ Quick Verification

After enabling Pages, visit:
https://kamlesh9876.github.io/E-Commerce-Sales-Performance-Analysis/

You should see:
- A redirect page with "📊 E-Commerce Sales Analysis"
- Automatic redirect to dashboard.html after 2 seconds

## 🛠️ Troubleshooting

### Still Getting 404?
1. **Wait 5-10 minutes** - GitHub Pages takes time to initialize
2. **Check Actions tab** - See if workflow is running
3. **Verify branch selection** - Make sure "master" branch is selected
4. **Clear browser cache** - Try a different browser or incognito mode

### Build Failed?
1. Go to **Actions** tab in your repository
2. Click on the failed workflow
3. Check the error message
4. The workflow should show any file issues

## 🎯 Alternative: Use gh-pages Branch

If the above doesn't work, try this:

1. **Go to Pages settings**
2. **Source**: Deploy from a branch
3. **Branch**: gh-pages
4. **Folder**: / (root)
5. **Save**

## 📊 What's Already Prepared

✅ **GitHub Actions Workflow**: `.github/workflows/pages.yml`
✅ **Index Page**: `index.html` (redirects to dashboard)
✅ **Dashboard**: `dashboard.html` (fully functional)
✅ **All Data Files**: Ready for deployment

## 🚀 Final Result

Once GitHub Pages is enabled, you'll have:
- **Professional Portfolio Site**
- **Interactive E-Commerce Dashboard**
- **Live Business Analysis**
- **Shareable URL for Resume/Portfolio**

---

**The key is manually enabling GitHub Pages in the repository settings - this step cannot be automated!**
