# 🎓 Study With Bob

**An AI-powered learning platform for students and teachers** featuring handwriting recognition, intelligent tutoring, auto-grading, and spaced repetition.

![Study With Bob](https://img.shields.io/badge/Status-Ready-green) ![Next.js](https://img.shields.io/badge/Next.js-14-black) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.109-teal)

---

## ✨ Features

### 👨‍🎓 For Students

- **✍️ Handwriting Recognition** - Write naturally with Apple Pencil or mouse on canvas
- **🤖 AI Tutor (Bob)** - Get contextual hints without spoiling the answer
- **✅ Instant Feedback** - Real-time correctness checking with explanations
- **🆘 Stuck Helper** - Proactive nudges when you need them
- **📚 Spaced Repetition** - Automatic review scheduling for long-term retention
- **📊 Progress Tracking** - Visual dashboards showing your growth

### 👩‍🏫 For Teachers

- **📝 Auto-Grading** - AI-powered grading with rubric-based feedback
- **📊 Analytics Dashboard** - Track class and individual performance
- **🔍 Misconception Detection** - AI identifies common student errors
- **📈 Topic Performance** - See which topics need more focus
- **✍️ Assignment Management** - Create and manage assignments easily

---

## 🏗️ Architecture

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Shadcn UI** - Beautiful GitHub-inspired components
- **Canvas API** - Handwriting input
- **SSE** - Real-time server updates

### Backend
- **FastAPI** - Modern Python web framework
- **Multi-Agent System:**
  - 🎓 **Tutor Agent** - Generates hints and guidance
  - ✅ **Assessment Agent** - Evaluates correctness
  - 💬 **Feedback Agent** - Creates personalized feedback
  - 🧠 **Memory Agent** - Manages spaced repetition

### AI/ML Stack
- **Gemini 2.0 Flash** - Primary LLM for grading & hints
- **GPT-4o / Claude 3.5** - Fallback LLMs for robust reasoning
- **SymPy** - Symbolic mathematics for exact correctness
- **Vision APIs** - Handwriting recognition

### Database
- **Supabase** - PostgreSQL with Auth
- **pgvector** - Vector embeddings for personalization
- **Row Level Security** - Secure data access

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.10+

### 1. Clone & Install

```bash
# Clone the repository
git clone <your-repo-url>
cd SVIL

# Install frontend dependencies
npm install

# Install backend dependencies
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Application

**Terminal 1 - Frontend:**
```bash
npm run dev
```

**Terminal 2 - Backend:**
```bash
cd backend
python main.py
```

**Access the app:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 📖 Usage Guide

### For Students

1. **Sign Up** - Create an account from the homepage
2. **Start Learning** - Navigate to `/student` to see your dashboard
3. **Solve Problems:**
   - Read the problem
   - Write your solution on the canvas
   - Submit your answer
   - Get instant feedback or hints
4. **Review Topics** - Check your review queue for spaced repetition

### For Teachers

1. **Sign Up** - Create a teacher account
2. **Dashboard** - Navigate to `/teacher`
3. **View Students** - See all student performance metrics
4. **Create Assignments** - Click "Create Assignment"
5. **Auto-Grade** - Use AI to grade submissions automatically
6. **Analyze** - View analytics to identify class-wide issues

---

## 🧪 API Documentation

### Student Endpoints

**Check Answer**
```bash
POST /api/student/check-answer
```
```json
{
  "problemId": 1,
  "imageData": "data:image/png;base64,...",
  "strokes": [...]
}
```

**Get Problem**
```bash
GET /api/student/problems/{problem_id}
```

**Review Queue**
```bash
GET /api/student/review-queue/{student_id}
```

### Teacher Endpoints

**Create Assignment**
```bash
POST /api/teacher/assignments
```

**Get Class Analytics**
```bash
GET /api/teacher/analytics/{class_id}
```

**Auto-Grade**
```bash
POST /api/teacher/grade/{assignment_id}
```

### Real-Time

**SSE Stream**
```bash
GET /api/realtime/stream/{user_id}
```

Example client-side:
```javascript
const eventSource = new EventSource('/api/realtime/stream/user_123');
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle hints, nudges, feedback
};
```

---

## 🧠 How It Works

### Answer Checking Flow

1. **Student submits** handwritten answer (canvas → image + stroke data)
2. **Vision LLM** extracts mathematical expression
3. **SymPy** checks symbolic equivalence
4. **Assessment Agent** evaluates correctness
5. **Decision:**
   - ✅ Correct → Feedback Agent generates congratulations + explanation
   - ❌ Incorrect → Tutor Agent generates progressive hint
6. **Memory Agent** records for spaced repetition

### Multi-Agent System

```
Student Submission
       ↓
   Orchestrator
       ↓
   ┌───┴────────────────┐
   ↓                    ↓
Assessment Agent    Tutor Agent
   ↓                    ↓
Feedback Agent      Memory Agent
```

### Spaced Repetition

Uses the **SM-2 algorithm** with intervals: 1, 3, 7, 14, 30, 60 days

- Topics reviewed based on strength (0-1)
- Automatic scheduling
- Personalized review queue

---

## 🎨 UI/UX Design

Inspired by **GitHub's clean, professional interface:**

- ⚪ Minimal color palette (blues, grays)
- 📦 Card-based layouts
- 🔘 Subtle hover effects
- 📱 Fully responsive
- 🌓 Dark mode support

---

## 🔐 Security

- **Row Level Security (RLS)** - Students see only their data
- **Auth tokens** - Supabase handles JWT authentication
- **Input validation** - Pydantic models on backend
- **Rate limiting** - Prevent API abuse (TODO: implement)

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📋 Roadmap

- [ ] Mobile app (React Native)
- [ ] Video lesson integration
- [ ] Real-time collaboration (students work together)
- [ ] Voice input for verbal explanations
- [ ] Gamification (badges, leaderboards)
- [ ] Parent dashboard
- [ ] Multi-language support
- [ ] Offline mode

---

## 🐛 Troubleshooting

### Frontend won't start
- Check Node.js version: `node --version` (need 18+)
- Delete `node_modules` and `.next`, then `npm install`

### Backend errors
- Activate virtual environment
- Check Python version: `python --version` (need 3.10+)
- Try: `pip install -r requirements.txt` again

### Canvas not drawing
- Check browser compatibility (Chrome, Safari, Firefox recommended)
- Try clearing cache
- Ensure JavaScript is enabled

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- **Gemini 2.0 Flash** for fast, accurate AI tutoring
- **Supabase** for amazing backend infrastructure
- **Shadcn UI** for beautiful components
- **SymPy** for symbolic mathematics

---

## 📞 Support

- 🐛 Issues: [GitHub Issues](https://github.com/yourname/study-with-bob/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourname/study-with-bob/discussions)
- 📧 Email: support@studywithbob.com

---

Built with ❤️ by the Study With Bob team

**Ready to revolutionize learning? Let's go! 🚀**

