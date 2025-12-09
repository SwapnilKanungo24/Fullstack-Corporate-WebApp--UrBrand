# GitHub Setup Guide for Beginners

## Step 1: Create a GitHub Account (if you don't have one)
1. Go to https://github.com
2. Click "Sign up"
3. Follow the instructions to create your account

## Step 2: Create a New Repository on GitHub

1. **Login to GitHub**
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Fill in the details:**
   - Repository name: `fullstack-project` (or any name you like)
   - Description: "Full-stack web application with Flask and MongoDB"
   - Choose: **Public** or **Private** (your choice)
   - **DO NOT** check "Initialize with README" (we already have files)
5. **Click "Create repository"**

## Step 3: Install Git (if not installed)

**Check if Git is installed:**
```bash
git --version
```

**If not installed, download from:** https://git-scm.com/downloads

## Step 4: Initialize Git in Your Project

Open terminal/command prompt in your project folder:

```bash
# Navigate to your project folder
cd "D:\FullStack Project\fullstack project"

# Initialize git repository
git init

# Add all files (respects .gitignore)
git add .

# Create your first commit
git commit -m "Initial commit: Full-stack application with Flask and MongoDB"
```

## Step 5: Connect to GitHub

After creating the repository on GitHub, you'll see a page with instructions. Use these commands:

```bash
# Add GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/fullstack-project.git

# Rename main branch (if needed)
git branch -M main

# Push your code to GitHub
git push -u origin main
```

**Note:** GitHub will ask for your username and password. Use a **Personal Access Token** instead of password:
- Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
- Generate new token with "repo" permissions
- Use this token as your password

## Step 6: Verify Upload

1. Go to your GitHub repository page
2. You should see all your files there
3. Check that `.gitignore` is working (you shouldn't see `__pycache__`, `venv/`, etc.)

## Common Commands You'll Need

```bash
# Check status of files
git status

# Add specific file
git add filename.txt

# Add all changes
git add .

# Commit changes
git commit -m "Description of what you changed"

# Push to GitHub
git push

# Pull latest changes from GitHub
git pull

# See what files are being tracked
git ls-files
```

## What's Included in .gitignore

✅ **Excluded (won't be uploaded):**
- Python cache files (`__pycache__/`)
- Virtual environment (`venv/`, `env/`)
- Uploaded images (`backend/uploads/`)
- IDE settings (`.vscode/`, `.idea/`)
- Documentation files (QUICK_START.md, SETUP_GUIDE.md, TROUBLESHOOTING.md)
- Environment variables (`.env`)
- Log files (`.log`)

✅ **Included (will be uploaded):**
- All source code (`.py`, `.html`, `.css`, `.js`)
- Configuration files (`requirements.txt`, `config.py`)
- README.md
- Project structure

## Troubleshooting

**Problem: "fatal: not a git repository"**
- Solution: Make sure you're in the project folder and run `git init`

**Problem: "remote origin already exists"**
- Solution: Remove it first: `git remote remove origin`, then add again

**Problem: "Authentication failed"**
- Solution: Use Personal Access Token instead of password

**Problem: "Permission denied"**
- Solution: Check your GitHub username and repository name are correct

## Next Steps After Upload

1. **Add a description** to your GitHub repository
2. **Add topics/tags** (flask, mongodb, fullstack, python)
3. **Update README.md** with project description
4. **Create a license** if you want (MIT, Apache, etc.)

## Your Repository Structure on GitHub

```
fullstack-project/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── utils.py
│   ├── routes/
│   └── README.md
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── admin/
├── requirements.txt
├── README.md
└── .gitignore
```

**Files NOT on GitHub:**
- `QUICK_START.md` ❌
- `SETUP_GUIDE.md` ❌
- `TROUBLESHOOTING.md` ❌
- `backend/uploads/` ❌ (user-generated content)
- `__pycache__/` ❌
- `venv/` ❌

---

**Need Help?** Check GitHub documentation: https://docs.github.com

