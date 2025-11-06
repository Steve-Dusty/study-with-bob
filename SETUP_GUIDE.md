# 📖 Complete Setup Guide for Study With Bob

This guide will walk you through setting up Study With Bob from scratch.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [API Keys Setup](#api-keys-setup)
3. [Supabase Setup](#supabase-setup)
4. [Local Development](#local-development)
5. [Production Deployment](#production-deployment)
6. [Testing](#testing)

---

## Prerequisites

### Required Software

1. **Node.js 18+**
   ```bash
   node --version  # Should be v18.0.0 or higher
   ```
   Download from: https://nodejs.org/

2. **Python 3.10+**
   ```bash
   python --version  # Should be 3.10.0 or higher
   ```
   Download from: https://python.org/

3. **Git**
   ```bash
   git --version
   ```

### Recommended Tools

- **VS Code** or **Cursor** for development
- **Postman** or **Insomnia** for API testing
- **PostgreSQL Client** (optional, for database inspection)

---

## API Keys Setup

You need **at least one** LLM provider. We recommend starting with Gemini (free tier available).

### 1. Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key

**Free Tier:** 60 requests/minute, perfect for development!

### 2. OpenAI API Key (Optional)

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create new secret key
4. Copy and save it (you won't see it again!)

**Pricing:** Pay-as-you-go, ~$0.01-0.03 per request

### 3. Anthropic Claude API Key (Optional)

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up for API access
3. Create API key
4. Copy the key

**Pricing:** Pay-as-you-go, competitive rates

---

## Supabase Setup

### 1. Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign up with GitHub (recommended)
4. Click "New Project"
5. Fill in:
   - **Name:** study-with-bob
   - **Database Password:** (choose strong password)
   - **Region:** (closest to you)
6. Wait 2-3 minutes for setup

### 2. Get API Credentials

1. In your project dashboard, click ⚙️ **Settings**
2. Go to **API** section
3. Copy these values:
   - **Project URL** → `SUPABASE_URL`
   - **anon public** → `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - **service_role** → `SUPABASE_KEY` (backend only!)

### 3. Set Up Database Schema

1. In Supabase, click **SQL Editor** (left sidebar)
2. Click "New Query"
3. Copy entire contents of `backend/app/database/schema.sql`
4. Paste and click "Run"
5. Should see "Success. No rows returned"

### 4. Enable pgvector Extension

1. Go to **Database** → **Extensions** (left sidebar)
2. Search for "vector"
3. Click toggle to enable
4. Confirm

### 5. Configure Auth (Optional)

For email/password auth:
1. Go to **Authentication** → **Providers**
2. Enable "Email" provider
3. Configure email templates if desired

---

## Local Development

### Step 1: Clone Repository

```bash
git clone <your-repo-url>
cd SVIL
```

### Step 2: Frontend Setup

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Edit .env.local with your values
nano .env.local  # or use any text editor
```

**.env.local:**
```env
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Step 3: Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env with your values
nano .env
```

**backend/.env:**
```env
# LLM API Keys (need at least one)
GEMINI_API_KEY=AIzaSyD...your_key_here
OPENAI_API_KEY=sk-proj-...your_key_here  # optional
ANTHROPIC_API_KEY=sk-ant-...your_key_here  # optional

# Supabase
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...service_role_key

# Server
PORT=8000
HOST=0.0.0.0
```

### Step 4: Start Development Servers

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # if not already activated
python main.py
```

You should see:
```
🚀 Starting Study With Bob Backend...
✅ Gemini client initialized
✅ Supabase client initialized
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Frontend:**
```bash
npm run dev
```

You should see:
```
  ▲ Next.js 14.2.5
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

### Step 5: Test the Application

1. Open browser to http://localhost:3000
2. You should see the homepage
3. Click "Start Learning" → Should go to `/student`
4. Try drawing on canvas and submitting

---

## Production Deployment

### Frontend (Vercel - Recommended)

1. Push code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Import Project"
4. Select your repo
5. Add environment variables:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `NEXT_PUBLIC_API_URL` (your backend URL)
6. Click "Deploy"

### Backend (Railway, Render, or DigitalOcean)

#### Option A: Railway

1. Go to [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Select repo, set root directory to `backend`
4. Add environment variables (all from `.env`)
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy

#### Option B: Render

1. Go to [render.com](https://render.com)
2. "New +" → "Web Service"
3. Connect GitHub repo
4. Settings:
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables
6. Create Service

#### Option C: Docker (Any Platform)

```dockerfile
# Dockerfile for backend
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Deploy to:
- AWS ECS
- Google Cloud Run
- DigitalOcean App Platform
- Your own VPS

---

## Testing

### Manual Testing Checklist

**Student Features:**
- [ ] Homepage loads
- [ ] Can navigate to student dashboard
- [ ] Canvas drawing works
- [ ] Can submit answer
- [ ] Receives feedback/hint
- [ ] Progress displays correctly

**Teacher Features:**
- [ ] Teacher dashboard loads
- [ ] Can view student list
- [ ] Can view analytics
- [ ] Assignment creation works

**Backend:**
- [ ] API docs accessible at `/docs`
- [ ] Health check at `/health` returns OK
- [ ] Answer checking endpoint works
- [ ] Real-time SSE stream works

### Testing Answer Checking

**Test Problem:** Expand (x-1)²

**Correct Answer:** x^2 - 2x + 1

Try these on canvas:
- ✅ `x^2 - 2x + 1`
- ✅ `x**2 - 2*x + 1`
- ❌ `x^2 - x + 1` (should get hint)
- ❌ `x^2 + 2x + 1` (should get hint)

### API Testing with cURL

```bash
# Health check
curl http://localhost:8000/health

# Test answer checking (you'll need actual image data)
curl -X POST http://localhost:8000/api/student/check-answer \
  -H "Content-Type: application/json" \
  -d '{
    "problemId": 1,
    "imageData": "data:image/png;base64,iVBOR...",
    "strokes": []
  }'
```

---

## Common Issues & Solutions

### Issue: "Module not found" in backend

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

### Issue: Canvas not drawing

**Solutions:**
1. Check browser (Chrome/Safari work best)
2. Try incognito mode
3. Check console for errors (F12)

### Issue: LLM timeout

**Solutions:**
1. Check API key is correct
2. Verify internet connection
3. Try different provider
4. Check API quota limits

### Issue: Database connection fails

**Solutions:**
1. Verify Supabase URL and key
2. Check Supabase project is running
3. Confirm schema was set up
4. Test connection in Supabase dashboard

### Issue: Frontend can't reach backend

**Solutions:**
1. Verify backend is running (check terminal)
2. Check `NEXT_PUBLIC_API_URL` in `.env.local`
3. Try http://localhost:8000/health in browser
4. Check CORS settings in `main.py`

---

## Next Steps

Once everything is working:

1. **Customize Problems:** Add your own problems to database
2. **Adjust Styling:** Modify colors in `globals.css`
3. **Add Features:** Extend agents with new capabilities
4. **Deploy:** Follow production deployment guide above
5. **Monitor:** Set up error tracking (Sentry recommended)

---

## Getting Help

If you're stuck:

1. Check this guide again carefully
2. Review error messages in terminal
3. Check GitHub Issues
4. Join our Discord community
5. Email: support@studywithbob.com

---

**You're all set! Happy coding! 🚀**

