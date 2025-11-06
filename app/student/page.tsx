"use client";

import { useState } from "react";
import { HandwritingCanvas } from "@/components/canvas/HandwritingCanvas";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  BookOpen,
  TrendingUp,
  Clock,
  CheckCircle2,
  XCircle,
  Lightbulb,
  Home,
  Award,
  Loader2
} from "lucide-react";
import Link from "next/link";
import problemsData from "@/data/problems.json";

interface FeedbackResponse {
  correct: boolean;
  hint?: string;
  title?: string;
  explanation?: string;
  nextSteps?: string;
}

interface Problem {
  id: number;
  text: string;
  topic: string;
  difficulty: string;
  correctAnswer: string;
  commonMistakes: Array<{
    pattern: string;
    feedback: string;
  }>;
  hints: Array<{
    attempt: number;
    title: string;
    message: string;
  }>;
  successMessage: string;
  successOnAttempt: number;
}

const PROBLEMS: Problem[] = problemsData.problems;

export default function StudentDashboard() {
  const [currentProblemIndex, setCurrentProblemIndex] = useState(0);
  const [feedback, setFeedback] = useState<FeedbackResponse | null>(null);
  const [attempts, setAttempts] = useState(0);
  const [sessionStats, setSessionStats] = useState({ completed: 0, correct: 0, totalAttempts: 0 });
  const [isThinking, setIsThinking] = useState(false);
  const [showSuccessAnimation, setShowSuccessAnimation] = useState(false);

  const currentProblem = PROBLEMS[currentProblemIndex];
  const totalProblems = PROBLEMS.length;

  const handleSubmit = async (imageData: string, strokes: any[]) => {
    const currentAttempt = attempts + 1;
    setAttempts(currentAttempt);
    setFeedback(null);
    setIsThinking(true);
    setSessionStats(prev => ({ ...prev, totalAttempts: prev.totalAttempts + 1 }));

    // Simulate AI "thinking" with random delay between 5-10 seconds
    const thinkingTime = Math.floor(Math.random() * 5000) + 5000; // 5000-10000ms
    await new Promise(resolve => setTimeout(resolve, thinkingTime));

    // Smart mocked response - succeeds on the predetermined attempt
    const isCorrect = currentAttempt >= currentProblem.successOnAttempt;

    if (isCorrect) {
      setShowSuccessAnimation(true);
      setFeedback({
        correct: true,
        explanation: currentProblem.successMessage,
        nextSteps: "Ready for the next challenge?"
      });
      setSessionStats(prev => ({
        ...prev,
        correct: prev.correct + 1,
        completed: prev.completed + 1
      }));
    } else {
      // Get the hint for the current attempt
      const hintIndex = Math.min(currentAttempt - 1, currentProblem.hints.length - 1);
      const currentHint = currentProblem.hints[hintIndex];

      setFeedback({
        correct: false,
        title: currentHint.title,
        hint: currentHint.message
      });
    }

    setIsThinking(false);
  };

  const loadNextProblem = () => {
    setShowSuccessAnimation(false);
    setCurrentProblemIndex(prev => prev + 1);
    setFeedback(null);
    setAttempts(0);
  };

  // Calculate session progress
  const accuracy = sessionStats.totalAttempts > 0
    ? Math.round((sessionStats.correct / sessionStats.totalAttempts) * 100)
    : 0;

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="backdrop-blur-md bg-card/50 border-b border-border sticky top-0 z-50">
        <div className="container mx-auto px-6 py-5">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Link href="/">
                <Button variant="ghost" size="sm" className="text-muted-foreground hover:text-primary hover:bg-primary/10">
                  <Home className="h-4 w-4 mr-2" />
                  Home
                </Button>
              </Link>
              <div className="h-6 w-px bg-border" />
              <h1 className="text-2xl font-black text-foreground">Study Dashboard</h1>
            </div>
            
            <div className="flex items-center gap-4">
              <div className="bg-gradient-to-r from-primary to-accent px-5 py-2.5 rounded-xl font-black shadow-lg shadow-primary/30 text-white">
                Problem {currentProblemIndex + 1}/{totalProblems}
              </div>
              <Button size="sm" className="bg-primary hover:bg-primary/90 font-bold shadow-lg shadow-primary/30">
                <Award className="h-4 w-4 mr-2" />
                Profile
              </Button>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-6">
        <div className="grid lg:grid-cols-3 gap-6">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Current Problem */}
            <Card>
              <CardHeader>
                <div className="flex items-center justify-between">
                  <div>
                    <CardTitle>Current Problem</CardTitle>
                    <CardDescription>
                      {currentProblem.topic} • {currentProblem.difficulty}
                    </CardDescription>
                  </div>
                  <div className="flex items-center gap-2 text-sm text-muted-foreground">
                    <Clock className="h-4 w-4" />
                    Attempt {attempts + 1}
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <HandwritingCanvas
                  problemText={currentProblem.text}
                  onSubmit={handleSubmit}
                />
              </CardContent>
            </Card>

            {/* AI Thinking Indicator */}
            {isThinking && (
              <Card className="border-2 border-primary shadow-2xl shadow-primary/20 animate-pulse">
                <CardHeader className="bg-gradient-to-r from-primary to-accent">
                  <div className="flex items-center gap-3">
                    <Loader2 className="h-10 w-10 text-white animate-spin" />
                    <CardTitle className="text-3xl font-black text-white">AI is analyzing your work...</CardTitle>
                  </div>
                </CardHeader>
                <CardContent className="p-8">
                  <div className="space-y-4">
                    <div className="flex items-center gap-3 text-muted-foreground">
                      <div className="h-2 w-2 bg-primary rounded-full animate-bounce" />
                      <p className="font-medium">Reading handwriting...</p>
                    </div>
                    <div className="flex items-center gap-3 text-muted-foreground">
                      <div className="h-2 w-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                      <p className="font-medium">Checking mathematical correctness...</p>
                    </div>
                    <div className="flex items-center gap-3 text-muted-foreground">
                      <div className="h-2 w-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.4s' }} />
                      <p className="font-medium">Generating personalized feedback...</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Feedback */}
            {feedback && !isThinking && (
              <Card className={`${
                feedback.correct
                  ? "border-2 border-success shadow-2xl shadow-success/20"
                  : "border-2 border-warning shadow-2xl shadow-warning/20"
              } ${showSuccessAnimation ? "animate-in slide-in-from-bottom-4 duration-500" : ""}`}>
                <CardHeader className={`${
                  feedback.correct
                    ? "bg-gradient-to-r from-success to-success/80"
                    : "bg-gradient-to-r from-warning to-warning/80"
                } ${showSuccessAnimation ? "animate-in fade-in duration-700" : ""}`}>
                  <div className="flex items-center gap-3">
                    {feedback.correct ? (
                      <>
                        <CheckCircle2 className={`h-10 w-10 text-white ${showSuccessAnimation ? "animate-in zoom-in duration-500" : ""}`} />
                        <CardTitle className="text-3xl font-black text-white">Correct!</CardTitle>
                      </>
                    ) : (
                      <>
                        <Lightbulb className="h-10 w-10 text-white" />
                        <CardTitle className="text-3xl font-black text-white">Not quite - here's a hint</CardTitle>
                      </>
                    )}
                  </div>
                </CardHeader>
                <CardContent className="space-y-5 p-8">
                  {feedback.title && !feedback.correct && (
                    <div className="p-4 bg-primary/10 border-l-4 border-primary rounded-lg">
                      <p className="font-black text-base text-primary">{feedback.title}</p>
                    </div>
                  )}

                  {feedback.hint && (
                    <div className="p-6 bg-warning/10 border-2 border-warning rounded-xl">
                      <p className="font-bold text-lg text-foreground whitespace-pre-line">{feedback.hint}</p>
                    </div>
                  )}

                  {feedback.explanation && (
                    <div className={`p-6 bg-success/10 border-2 border-success rounded-xl ${showSuccessAnimation ? "animate-in slide-in-from-bottom-2 duration-500 delay-300" : ""}`}>
                      <p className="font-bold text-lg text-foreground">{feedback.explanation}</p>
                    </div>
                  )}

                  {feedback.correct && currentProblemIndex < totalProblems - 1 && (
                    <Button
                      onClick={loadNextProblem}
                      className={`w-full bg-primary hover:bg-primary/90 text-lg py-7 font-black shadow-lg shadow-primary/30 hover:scale-105 transition-all ${showSuccessAnimation ? "animate-in slide-in-from-bottom-2 duration-500 delay-500" : ""}`}
                    >
                      Next Problem
                    </Button>
                  )}

                  {feedback.correct && currentProblemIndex === totalProblems - 1 && (
                    <div className={`text-center space-y-4 ${showSuccessAnimation ? "animate-in slide-in-from-bottom-2 duration-500 delay-500" : ""}`}>
                      <p className="text-2xl font-black text-success">🎉 Session Complete! 🎉</p>
                      <p className="text-muted-foreground">You've completed all {totalProblems} problems!</p>
                      <Button
                        onClick={() => {
                          setCurrentProblemIndex(0);
                          setSessionStats({ completed: 0, correct: 0, totalAttempts: 0 });
                          setFeedback(null);
                          setAttempts(0);
                          setShowSuccessAnimation(false);
                        }}
                        className="w-full bg-primary hover:bg-primary/90 text-lg py-7 font-black shadow-lg shadow-primary/30 hover:scale-105 transition-all"
                      >
                        Start New Session
                      </Button>
                    </div>
                  )}
                </CardContent>
              </Card>
            )}
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Progress Overview */}
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Today's Progress</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div>
                  <div className="flex items-center justify-between text-sm mb-2">
                    <span className="text-muted-foreground">Problems Solved</span>
                    <span className="font-medium">{sessionStats.completed}/{totalProblems}</span>
                  </div>
                  <Progress value={(sessionStats.completed / totalProblems) * 100} />
                </div>

                <div>
                  <div className="flex items-center justify-between text-sm mb-2">
                    <span className="text-muted-foreground">Accuracy</span>
                    <span className="font-medium">{accuracy}%</span>
                  </div>
                  <Progress value={accuracy} />
                </div>

                <div>
                  <div className="flex items-center justify-between text-sm mb-2">
                    <span className="text-muted-foreground">Total Attempts</span>
                    <span className="font-medium">{sessionStats.totalAttempts}</span>
                  </div>
                </div>

                <div className="pt-2 border-t">
                  <div className="flex items-center gap-2 text-sm text-muted-foreground mb-2">
                    <TrendingUp className="h-4 w-4" />
                    <span>Streak: 5 days 🔥</span>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Topics to Review */}
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Review Queue</CardTitle>
                <CardDescription>Spaced repetition reminders</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  <div className="flex items-center justify-between p-2 rounded-md bg-muted">
                    <div>
                      <p className="text-sm font-medium">Quadratic Formula</p>
                      <p className="text-xs text-muted-foreground">Due today</p>
                    </div>
                    <Button size="sm" variant="ghost">Review</Button>
                  </div>
                  
                  <div className="flex items-center justify-between p-2 rounded-md bg-muted">
                    <div>
                      <p className="text-sm font-medium">Trigonometry</p>
                      <p className="text-xs text-muted-foreground">Due in 2 days</p>
                    </div>
                    <Button size="sm" variant="ghost">Review</Button>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Quick Actions */}
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Quick Actions</CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                <Button variant="outline" className="w-full justify-start" size="sm">
                  <BookOpen className="h-4 w-4 mr-2" />
                  Browse Lessons
                </Button>
                <Button variant="outline" className="w-full justify-start" size="sm">
                  <Award className="h-4 w-4 mr-2" />
                  View Achievements
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}

