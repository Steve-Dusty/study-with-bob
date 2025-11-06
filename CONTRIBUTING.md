# Contributing to Study With Bob

Thank you for your interest in contributing! 🎉

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to learn and build something awesome.

## How to Contribute

### Reporting Bugs

1. Check if the bug is already reported in [Issues](https://github.com/yourname/study-with-bob/issues)
2. If not, create a new issue with:
   - Clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Environment (OS, browser, versions)

### Suggesting Features

1. Check [Discussions](https://github.com/yourname/study-with-bob/discussions) first
2. Create a new discussion with:
   - Clear description
   - Use case / motivation
   - Proposed implementation (optional)

### Pull Requests

1. **Fork** the repository
2. **Create a branch:** `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit:** `git commit -m 'Add some feature'`
6. **Push:** `git push origin feature/your-feature-name`
7. **Open a Pull Request**

#### PR Guidelines

- Write clear commit messages
- Update documentation if needed
- Add tests for new features
- Ensure all tests pass
- Follow existing code style
- Keep PRs focused (one feature per PR)

## Development Setup

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.

Quick start:
```bash
# Frontend
npm install
npm run dev

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Project Structure

```
SVIL/
├── app/                    # Next.js frontend
│   ├── page.tsx           # Homepage
│   ├── student/           # Student dashboard
│   └── teacher/           # Teacher dashboard
├── components/            # React components
│   ├── canvas/           # Handwriting canvas
│   └── ui/               # Shadcn UI components
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── agents/      # Multi-agent system
│   │   ├── api/         # API routes
│   │   ├── database/    # Supabase integration
│   │   ├── services/    # LLM & math services
│   │   └── realtime/    # SSE handlers
│   └── main.py          # FastAPI app
└── README.md
```

## Coding Standards

### Frontend (TypeScript/React)

- Use TypeScript with strict mode
- Functional components with hooks
- Follow React best practices
- Use Tailwind for styling
- Component names: PascalCase

Example:
```typescript
interface Props {
  studentId: string;
  onSubmit: (data: Data) => void;
}

export function StudentCard({ studentId, onSubmit }: Props) {
  // ...
}
```

### Backend (Python)

- Follow PEP 8 style guide
- Type hints everywhere
- Async/await for I/O operations
- Docstrings for functions
- Class names: PascalCase
- Function names: snake_case

Example:
```python
async def process_submission(
    problem: Dict[str, Any],
    answer: str
) -> Dict[str, Any]:
    """
    Process student submission.
    
    Args:
        problem: Problem data
        answer: Student's answer
        
    Returns:
        Feedback response
    """
    # ...
```

## Testing

### Frontend Tests
```bash
npm test
```

### Backend Tests
```bash
cd backend
pytest
```

### Manual Testing

See [SETUP_GUIDE.md](SETUP_GUIDE.md#testing) for testing checklist.

## Areas for Contribution

### High Priority

- [ ] Mobile responsive improvements
- [ ] More problem types (calculus, geometry)
- [ ] Better error handling
- [ ] Performance optimization
- [ ] Accessibility improvements (ARIA labels, keyboard nav)

### Medium Priority

- [ ] Video lesson integration
- [ ] Gamification features
- [ ] Parent dashboard
- [ ] Export progress reports

### Nice to Have

- [ ] Multi-language support
- [ ] Voice input
- [ ] Collaborative problem solving
- [ ] Mobile apps (React Native)

## Questions?

- 💬 Join our Discord: [discord.gg/studywithbob](#)
- 📧 Email: dev@studywithbob.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourname/study-with-bob/issues)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making Study With Bob better! 🙏**

