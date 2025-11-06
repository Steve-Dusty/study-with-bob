# Study With Bob - Demo Guide

This guide tells you exactly what to write/draw for each problem to make the demo flow perfectly.

## How the Demo Works

- **5 total problems** - Counter shows "Problem 1/5" through "Problem 5/5"
- **Smart hints** - Each problem has 3 progressive hints that get more detailed
- **Controlled success** - Each problem is set to succeed on attempt 2 or 3 (configured in the JSON)
- **Progress tracking** - Updates in real-time as you complete problems

---

## Problem 1: Solve for x: 2x + 5 = 13
**Configured to succeed on: Attempt 2**

### Attempt 1 (Wrong)
**What to write:** `x = 9`

**What happens:**
- AI thinks for 5-10 seconds
- Shows hint with title: **"First, isolate the term with x"**
- Message: "You need to get the 2x by itself. What operation would eliminate the +5 on the left side?"

### Attempt 2 (Correct) ✅
**What to write:** `x = 4`

**What happens:**
- AI thinks for 5-10 seconds
- Green success animation appears
- Shows: "Perfect! You correctly isolated the variable by subtracting 5 from both sides, then dividing by 2."
- "Next Problem" button appears

---

## Problem 2: Expand: (x - 3)²
**Configured to succeed on: Attempt 3**

### Attempt 1 (Wrong)
**What to write:** `x² - 9`

**What happens:**
- Shows hint with title: **"Use the binomial square formula"**
- Message: "Remember: (a - b)² = a² - 2ab + b². Here, a = x and b = 3."

### Attempt 2 (Wrong)
**What to write:** `x² + 6x + 9`

**What happens:**
- Shows hint with title: **"Calculate each term"**
- Message shows step-by-step:
  ```
  a² = x²
  -2ab = -2(x)(3) = -6x
  b² = 3² = 9

  Now combine them!
  ```

### Attempt 3 (Correct) ✅
**What to write:** `x² - 6x + 9`

**What happens:**
- Green success animation
- Shows: "Excellent! You applied the binomial square formula correctly: (a - b)² = a² - 2ab + b²."
- "Next Problem" button appears

---

## Problem 3: Find the derivative: f(x) = 3x² + 2x - 5
**Configured to succeed on: Attempt 2**

### Attempt 1 (Wrong)
**What to write:** `f'(x) = 6x + 2x`

**What happens:**
- Shows hint with title: **"Apply the power rule to each term"**
- Message: "For x^n, the derivative is n·x^(n-1). Don't forget: the derivative of a constant is 0."

### Attempt 2 (Correct) ✅
**What to write:** `f'(x) = 6x + 2`

**What happens:**
- Green success animation
- Shows: "Great work! You correctly applied the power rule to each term and remembered that constants have a derivative of 0."
- "Next Problem" button appears

---

## Problem 4: Simplify: (12x³y²) / (3xy)
**Configured to succeed on: Attempt 3**

### Attempt 1 (Wrong)
**What to write:** `4xy`

**What happens:**
- Shows hint with title: **"Divide coefficients and subtract exponents"**
- Message: "When dividing: divide numbers, and for variables use x^a / x^b = x^(a-b)."

### Attempt 2 (Wrong)
**What to write:** `4x³y²`

**What happens:**
- Shows hint with title: **"Break it down step by step"**
- Message shows:
  ```
  12/3 = 4
  x³/x = x³⁻¹ = x²
  y²/y = y²⁻¹ = y¹ = y

  Now combine!
  ```

### Attempt 3 (Correct) ✅
**What to write:** `4x²y`

**What happens:**
- Green success animation
- Shows: "Perfect! You correctly divided the coefficients and subtracted the exponents for each variable."
- "Next Problem" button appears

---

## Problem 5: Solve: √(x + 5) = 4
**Configured to succeed on: Attempt 2**

### Attempt 1 (Wrong)
**What to write:** `x = 9`

**What happens:**
- Shows hint with title: **"Eliminate the square root"**
- Message: "To remove the square root, square both sides of the equation. What is 4²?"

### Attempt 2 (Correct) ✅
**What to write:** `x = 11`

**What happens:**
- Green success animation
- Shows: "Excellent! You squared both sides to eliminate the square root, then solved the resulting linear equation."
- **Session Complete message** appears with confetti emoji
- "Start New Session" button appears

---

## Today's Progress Tracking

The sidebar will update automatically as you work:

- **Problems Solved**: 0/5 → 1/5 → 2/5 → 3/5 → 4/5 → 5/5
- **Accuracy**: Updates based on (correct attempts / total attempts)
  - Example: If you make 2 attempts on problem 1, 3 on problem 2, etc.
  - After 5 problems with pattern above: 5 correct / 11 total attempts = 45%
- **Total Attempts**: Counts every submission (wrong or right)

---

## Visual Effects

### When Wrong
- Yellow/orange warning border
- Lightbulb icon
- Title: "Not quite - here's a hint"
- Blue banner with hint title
- Yellow box with detailed hint message

### When Correct
- **Green success border** with glow
- **Animated check icon** (zooms in)
- **Slide-in animation** for the card
- Title: "Correct!"
- Green explanation box (slides in)
- "Next Problem" button (slides in)

### Last Problem Complete
- Celebration message: "🎉 Session Complete! 🎉"
- "You've completed all 5 problems!"
- "Start New Session" button (resets everything)

---

## Tips for a Great Demo

1. **Write clearly** on the canvas so it looks realistic
2. **Pause briefly** between attempts to show you're "thinking"
3. **Point out the progressive hints** - they get more detailed each time
4. **Highlight the green animation** when you get it right
5. **Show the progress tracking** updating in the sidebar
6. **End with the celebration** after problem 5

The mocking is now smart, realistic, and designed to impress! 🚀
