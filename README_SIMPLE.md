# 🎓 Study With Bob - Quick Start (No API Keys!)

**An AI-powered learning platform that works out-of-the-box with mock data!**

No Gemini, OpenAI, Claude, or Supabase needed! 🎉

---

## ⚡ Super Quick Start

### 1. Install Dependencies

```bash
# Frontend
npm install

# Backend
cd backend
pip install -r requirements.txt
```

### 2. Run Both Servers

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```

**Terminal 2 - Frontend:**
```bash
npm run dev
```

### 3. Open & Use

Go to http://localhost:3000

**That's it!** No API keys, no database setup, no configuration! 🚀

---

## 🎮 What You Can Do

### Try as a Student
1. Go to http://localhost:3000/student
2. Draw on the canvas (use mouse or touchscreen)
3. Submit your answer
4. Get instant AI feedback (mock data)
5. See your progress update

### Try as a Teacher
1. Go to http://localhost:3000/teacher
2. View student analytics
3. See class performance
4. Check misconceptions
5. Browse assignments

---

## 🤖 How It Works (Without APIs)

✅ **Mock LLM Service** - Realistic AI responses without API calls
✅ **In-Memory Database** - No Supabase needed, uses RAM
✅ **Demo Problems** - 3 pre-loaded math problems
✅ **Randomized Feedback** - Different hints each time
✅ **Canvas Drawing** - Fully functional handwriting input

---

## 📁 Project Structure

```
SVIL/
├── app/              # Next.js pages (student, teacher, login)
├── components/       # React components (canvas, UI)
├── backend/
│   └── app/
│       ├── agents/   # AI agents (mock responses)
│       ├── services/ # Math + Mock LLM
│       └── database/ # In-memory storage
└── README_SIMPLE.md  # This file!
```

---

## ❓ FAQ

**Q: Do I need API keys?**
A: Nope! Everything uses mock data.

**Q: Does it save data?**
A: Data is stored in memory and resets when you restart the server.

**Q: Can I add real API keys later?**
A: Yes! The original implementation is still in git history if needed.

**Q: Does the canvas work?**
A: Yes! Drawing is fully functional. The "handwriting recognition" returns mock answers.

**Q: What math problems are included?**
A: 
- Expand: (x - 1)²
- Solve: 2x + 5 = 13
- Derivative: f(x) = 3x² + 2x - 5

---

## 🔧 Customization

### Add Your Own Problems

Edit `backend/app/database/supabase_client.py`:

```python
def _seed_demo_data(self):
    self.problems = {
        4: {  # Add new problem
            "id": 4,
            "question": "Your question here",
            "expected_answer": "answer",
            "topic": "Algebra",
            "difficulty": "easy",
            "hints": ["hint 1", "hint 2"]
        }
    }
```

### Change Mock Responses

Edit `backend/app/services/llm_service.py`:

```python
async def generate_text(self, prompt: str, ...):
    # Add your own mock responses here
    if "your_keyword" in prompt_lower:
        return "Your custom response"
```

---

## 🎨 GitHub-Style UI

The interface is designed to look like GitHub:
- Clean card layouts
- Subtle borders
- Blue accent colors
- Professional typography
- Responsive design

---

## 🚀 What's Included

✅ Full-stack application (Next.js + FastAPI)
✅ Handwriting canvas with drawing
✅ Multi-agent AI system (with mocks)
✅ SymPy math validation
✅ Student & teacher dashboards
✅ Progress tracking
✅ Real-time SSE support
✅ Spaced repetition system
✅ Professional UI

---

## 📝 Notes

- This is a **demo/development version**
- All data is lost when servers restart
- Mock responses are randomized for variety
- Perfect for testing, demos, or learning
- Can be upgraded to use real APIs later

---

## 🎯 Next Steps

Want to add real API integrations?

1. Get API keys (Gemini is free!)
2. Check git history for original implementation
3. Uncomment real LLM service code
4. Add Supabase credentials
5. Deploy to production

---

## 💡 Tips

- Press F12 in browser to see API calls
- Check console for backend logs
- Try drawing different answers
- Refresh page to reset state
- Test both student and teacher views

---

**Enjoy exploring Study With Bob! No setup needed! 🎉**

Questions? Check the backend logs or frontend console for details.

