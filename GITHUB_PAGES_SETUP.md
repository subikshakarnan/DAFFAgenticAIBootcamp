# GitHub Pages Setup Instructions

Follow these steps to enable GitHub Pages for your Watsonx Agentic AI Course:

## 🚀 Quick Setup (5 minutes)

### Step 1: Enable GitHub Pages

1. **Go to your repository** on GitHub
2. **Click "Settings"** (in the repository, not your account)
3. **Scroll down to "Pages"** in the left sidebar
4. **Under "Source"**, select:
   - Source: **GitHub Actions**
5. **Save the changes**

### Step 2: Verify Workflow

1. **Go to the "Actions" tab** in your repository
2. **Check that the "Deploy Jekyll site to Pages" workflow** is present
3. **If there are no workflows**, push the files created in this setup to trigger the first deployment

### Step 3: Access Your Course

After the first successful deployment (usually 2-3 minutes):

- **Your course will be available at**: `https://[your-username].github.io/6-08-2025-DTA/`
- **Replace `[your-username]`** with your actual GitHub username

## 📋 What Was Created

This setup created the following structure for your course:

```
6-08-2025-DTA/
├── docs/                           # Course website files
│   ├── _config.yml                 # Jekyll configuration
│   ├── _layouts/
│   │   └── default.html            # Custom layout with navigation
│   ├── index.md                    # Course homepage
│   ├── orchestrate.md              # Chapter 1: Orchestrate
│   ├── langflow.md                 # Chapter 2: Langflow
│   ├── langgraph.md                # Chapter 3: Langgraph
│   ├── governance.md               # Chapter 4: Governance
│   ├── Gemfile                     # Ruby dependencies
│   └── README.md                   # Documentation
├── .github/
│   └── workflows/
│       └── deploy.yml              # Automated deployment
└── GITHUB_PAGES_SETUP.md          # This file
```

## 🎯 Course Features

Your course website includes:

### ✅ Professional Course Structure
- **Landing page** with course overview
- **4 progressive chapters**: Orchestrate → Langflow → Langgraph → Governance
- **Clear learning objectives** for each section
- **Video placeholders** ready for your content

### ✅ Navigation System
- **Course navigation bar** on all pages
- **Previous/Next links** between chapters
- **Home button** to return to overview
- **Mobile-responsive** design

### ✅ Ready for Video Content
- **Styled video placeholders** in each chapter
- **Easy embedding** for YouTube, Vimeo, or custom videos
- **Responsive video containers**

### ✅ Automatic Deployment
- **GitHub Actions workflow** for automated publishing
- **Builds on every push** to main branch
- **No manual deployment** required

## 🎬 Adding Your Videos

When you're ready to add videos to each chapter:

### For YouTube Videos:
```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
        title="YouTube video player" frameborder="0" allowfullscreen></iframe>
```

### For Vimeo Videos:
```html
<iframe src="https://player.vimeo.com/video/YOUR_VIDEO_ID" width="560" height="315" 
        frameborder="0" allowfullscreen></iframe>
```

Replace the video placeholder sections in each chapter file with the appropriate embed code.

## 🔧 Customization Options

### Update Course Title or Description
Edit `docs/_config.yml`:
```yaml
title: "Your Custom Course Title"
description: "Your course description"
```

### Modify Course Sections
Edit the `course.sections` in `docs/_config.yml` to:
- Change section titles
- Add new sections
- Reorder content

### Custom Styling
- Edit `docs/_layouts/default.html` for layout changes
- Add CSS to individual page `<style>` sections
- Create `docs/_sass/` directory for global styles

## 🐛 Troubleshooting

### Site Not Loading?
1. **Check Actions tab** for build errors
2. **Verify Pages settings** are correct
3. **Wait 2-3 minutes** after first push
4. **Check that main branch** has the docs folder

### Build Failing?
1. **Check the Actions tab** for error details
2. **Verify all Markdown** syntax is correct
3. **Ensure Jekyll front matter** is properly formatted
4. **Test locally** with `bundle exec jekyll serve`

### Navigation Issues?
1. **Check file names** match navigation links
2. **Verify front matter titles** match config
3. **Ensure all pages** have proper front matter

## 📱 Mobile Optimization

Your course is automatically mobile-optimized with:
- **Responsive navigation** that collapses on small screens
- **Flexible grid layout** for course sections
- **Touch-friendly buttons** and links
- **Readable typography** on all devices

## 🔄 Updating Content

To update your course:

1. **Edit the appropriate `.md` files** in the `docs/` directory
2. **Commit and push** to the main branch
3. **GitHub Actions automatically rebuilds** the site
4. **Changes appear** within 1-2 minutes

## 📊 Analytics (Optional)

To add Google Analytics:

1. **Add your GA tracking ID** to `docs/_config.yml`:
   ```yaml
   google_analytics: "YOUR_GA_TRACKING_ID"
   ```

2. **The theme will automatically** include the tracking code

## 🎓 Course Completion

Your Watsonx Agentic AI Course is now:
- ✅ **Professionally structured** with 4 progressive chapters
- ✅ **Automatically deployed** to GitHub Pages
- ✅ **Mobile-responsive** and accessible
- ✅ **Ready for video content** with styled placeholders
- ✅ **Easy to maintain** with simple Markdown editing

## 🚀 Next Steps

1. **Add your video content** to each chapter
2. **Customize the styling** to match your brand
3. **Share the course URL** with your students
4. **Collect feedback** and iterate on the content

Your course URL: `https://[your-username].github.io/6-08-2025-DTA/`

**Happy teaching! 🎉** 