# GitHub Setup Instructions

## Option 1: Using GitHub Web Interface (Recommended)

### Step 1: Create Repository on GitHub

1. Go to [github.com/new](https://github.com/new)
2. Fill in the repository details:
   - **Repository name**: `tana-paste-skill`
   - **Description**: "Multi-purpose Claude Code skill for converting content to valid Tana Paste format"
   - **Visibility**: Public (or Private if preferred)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Step 2: Push to GitHub

After creating the repository, run these commands:

```bash
cd "C:\Dev\ddv\tana-paste-skill"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tana-paste-skill.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify

Visit `https://github.com/YOUR_USERNAME/tana-paste-skill` to see your repository.

---

## Option 2: Using GitHub CLI (if installed)

### Install GitHub CLI

**Windows (using winget):**
```bash
winget install --id GitHub.cli
```

**Or download from**: https://cli.github.com/

### Create and Push Repository

```bash
cd "C:\Dev\ddv\tana-paste-skill"

# Login to GitHub
gh auth login

# Create repository
gh repo create tana-paste-skill --public --source=. --remote=origin --description="Multi-purpose Claude Code skill for converting content to valid Tana Paste format"

# Push to GitHub
git push -u origin main
```

---

## Repository Settings (After Creation)

### Add Topics

Go to repository settings and add these topics:
- `claude-code`
- `tana`
- `tana-paste`
- `knowledge-management`
- `pkm`
- `bim`
- `skill`

### Add Description

Ensure the description is:
```
Multi-purpose Claude Code skill for converting content (tasks, meetings, projects, notes, BIM data) to valid Tana Paste format
```

### Enable Issues

Go to Settings > Features > Enable Issues

### Create Release

After pushing:

1. Go to Releases > Create a new release
2. Tag version: `v1.0.0`
3. Release title: `v1.0.0 - Initial Release`
4. Description: Copy from CHANGELOG.md
5. Attach the built `.skill` file (generate with `python scripts/build_skill.py`)
6. Publish release

---

## Current Repository Status

✅ Git initialized
✅ Initial commit created
✅ All files staged and committed
⏳ Waiting for remote repository creation
⏳ Waiting for push to GitHub

**Commit hash**: `95a1089`
**Branch**: `main`
**Files committed**: 13 files, 2230 lines

---

## Next Steps After Push

1. **Update README links** - Replace relative paths with GitHub URLs
2. **Add badges** - Build status, version, license badges
3. **Create Wiki** - Add detailed usage guides
4. **Enable Discussions** - For community support
5. **Set up GitHub Actions** (optional) - Auto-build on release

---

## Troubleshooting

### Permission Denied

If you get permission errors, ensure you have:
1. GitHub account credentials configured
2. SSH key added to GitHub (if using SSH)
3. Personal access token (if using HTTPS)

### Remote Already Exists

If you see "remote origin already exists":
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/tana-paste-skill.git
```

---

## Contact

For issues or questions:
- GitHub: Create an issue
- Email: davdelven@gmail.com
