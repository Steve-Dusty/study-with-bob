"use client";

import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { 
  BarChart3, 
  Users, 
  FileText, 
  TrendingUp, 
  AlertCircle,
  Home,
  Plus,
  Download,
  CheckCircle
} from "lucide-react";
import Link from "next/link";

// Mock data
const STUDENTS = [
  { id: 1, name: "Alice Johnson", score: 92, problems: 45, accuracy: 89, lastActive: "2h ago" },
  { id: 2, name: "Bob Smith", score: 78, problems: 38, accuracy: 76, lastActive: "5h ago" },
  { id: 3, name: "Charlie Brown", score: 85, problems: 42, accuracy: 82, lastActive: "1h ago" },
  { id: 4, name: "Diana Prince", score: 95, problems: 50, accuracy: 94, lastActive: "30m ago" },
  { id: 5, name: "Ethan Hunt", score: 71, problems: 35, accuracy: 68, lastActive: "1d ago" },
];

const ASSIGNMENTS = [
  { id: 1, title: "Algebra Quiz 1", dueDate: "2025-11-10", submitted: 24, total: 30, avgScore: 82 },
  { id: 2, title: "Calculus Problem Set", dueDate: "2025-11-12", submitted: 18, total: 30, avgScore: 75 },
  { id: 3, title: "Geometry Practice", dueDate: "2025-11-15", submitted: 12, total: 30, avgScore: 88 },
];

const MISCONCEPTIONS = [
  { topic: "Quadratic Formula", students: 8, description: "Sign errors when calculating discriminant" },
  { topic: "Chain Rule", students: 6, description: "Forgetting to multiply by inner derivative" },
  { topic: "Factoring", students: 5, description: "Difficulty identifying common factors" },
];

export default function TeacherDashboard() {
  const [selectedStudent, setSelectedStudent] = useState<typeof STUDENTS[0] | null>(null);

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
              <h1 className="text-2xl font-black text-foreground">Teacher Dashboard</h1>
            </div>
            
            <Button className="bg-primary hover:bg-primary/90 font-black shadow-lg shadow-primary/30">
              <Plus className="h-4 w-4 mr-2" />
              Create Assignment
            </Button>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-6">
        {/* Stats Overview */}
        <div className="grid md:grid-cols-4 gap-4 mb-6">
          <Card className="border-2 border-border hover:border-primary/50 transition-colors">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-bold">Total Students</CardTitle>
              <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center">
                <Users className="h-5 w-5 text-white" />
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-black text-foreground">30</div>
              <p className="text-xs text-muted-foreground mt-1">
                <span className="text-success font-bold">+2</span> from last week
              </p>
            </CardContent>
          </Card>

          <Card className="border-2 border-border hover:border-primary/50 transition-colors">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-bold">Avg Class Score</CardTitle>
              <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center">
                <TrendingUp className="h-5 w-5 text-white" />
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-black text-foreground">82%</div>
              <p className="text-xs text-muted-foreground mt-1">
                <span className="text-success font-bold">+5%</span> from last month
              </p>
            </CardContent>
          </Card>

          <Card className="border-2 border-border hover:border-primary/50 transition-colors">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-bold">Active Assignments</CardTitle>
              <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center">
                <FileText className="h-5 w-5 text-white" />
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-black text-foreground">3</div>
              <p className="text-xs text-muted-foreground mt-1">
                62 submissions pending
              </p>
            </CardContent>
          </Card>

          <Card className="border-2 border-border hover:border-primary/50 transition-colors">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-bold">Completion Rate</CardTitle>
              <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center">
                <CheckCircle className="h-5 w-5 text-white" />
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-black text-foreground">87%</div>
              <p className="text-xs text-muted-foreground mt-1">
                <span className="text-success font-bold">+3%</span> from last week
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Main Content */}
        <Tabs defaultValue="students" className="space-y-4">
          <TabsList>
            <TabsTrigger value="students">Students</TabsTrigger>
            <TabsTrigger value="assignments">Assignments</TabsTrigger>
            <TabsTrigger value="analytics">Analytics</TabsTrigger>
          </TabsList>

          {/* Students Tab */}
          <TabsContent value="students" className="space-y-4">
            <Card>
              <CardHeader>
                <CardTitle>Student Performance</CardTitle>
                <CardDescription>Overview of all students in your class</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {STUDENTS.map((student) => (
                    <div
                      key={student.id}
                      className="flex items-center justify-between p-4 rounded-lg border hover:bg-muted cursor-pointer transition-colors"
                      onClick={() => setSelectedStudent(student)}
                    >
                      <div className="flex items-center gap-4">
                        <div className="h-12 w-12 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center shadow-md">
                          <span className="font-black text-white text-sm">
                            {student.name.split(' ').map(n => n[0]).join('')}
                          </span>
                        </div>
                        <div>
                          <p className="font-medium">{student.name}</p>
                          <p className="text-sm text-muted-foreground">
                            {student.problems} problems • Last active {student.lastActive}
                          </p>
                        </div>
                      </div>
                      <div className="flex items-center gap-6 text-sm">
                        <div className="text-right">
                          <p className="text-muted-foreground">Score</p>
                          <p className="font-medium">{student.score}%</p>
                        </div>
                        <div className="text-right">
                          <p className="text-muted-foreground">Accuracy</p>
                          <p className="font-medium">{student.accuracy}%</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Assignments Tab */}
          <TabsContent value="assignments" className="space-y-4">
            <Card>
              <CardHeader>
                <CardTitle>Active Assignments</CardTitle>
                <CardDescription>Manage and grade student submissions</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {ASSIGNMENTS.map((assignment) => (
                    <div
                      key={assignment.id}
                      className="flex items-center justify-between p-4 rounded-lg border"
                    >
                      <div>
                        <h4 className="font-medium">{assignment.title}</h4>
                        <p className="text-sm text-muted-foreground">
                          Due: {assignment.dueDate} • {assignment.submitted}/{assignment.total} submitted
                        </p>
                      </div>
                      <div className="flex items-center gap-4">
                        <div className="text-right">
                          <p className="text-sm text-muted-foreground">Avg Score</p>
                          <p className="font-medium text-lg">{assignment.avgScore}%</p>
                        </div>
                        <Button variant="outline" size="sm">
                          Grade
                        </Button>
                        <Button variant="outline" size="sm">
                          <Download className="h-4 w-4" />
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Analytics Tab */}
          <TabsContent value="analytics" className="space-y-4">
            <div className="grid lg:grid-cols-2 gap-4">
              {/* Class Misconceptions */}
              <Card>
                <CardHeader>
                  <div className="flex items-center gap-2">
                    <AlertCircle className="h-5 w-5 text-yellow-500" />
                    <CardTitle>Common Misconceptions</CardTitle>
                  </div>
                  <CardDescription>
                    AI-detected patterns across student work
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {MISCONCEPTIONS.map((item, idx) => (
                      <div key={idx} className="p-5 rounded-xl border-2 border-warning bg-warning/10 shadow-lg hover:shadow-xl transition-all">
                        <div className="flex items-center justify-between mb-3">
                          <h4 className="font-black text-lg text-foreground">{item.topic}</h4>
                          <span className="text-sm font-black bg-gradient-to-r from-warning to-warning/80 text-white px-4 py-1.5 rounded-full shadow-md">
                            {item.students} students
                          </span>
                        </div>
                        <p className="text-sm font-medium mb-4 text-muted-foreground">{item.description}</p>
                        <Button size="sm" className="bg-primary hover:bg-primary/90 font-bold shadow-md shadow-primary/30">
                          Create targeted lesson →
                        </Button>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Performance Trends */}
              <Card>
                <CardHeader>
                  <CardTitle>Performance by Topic</CardTitle>
                  <CardDescription>Class average scores</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {[
                      { topic: "Algebra", score: 85, color: "bg-green-600" },
                      { topic: "Calculus", score: 72, color: "bg-yellow-500" },
                      { topic: "Geometry", score: 90, color: "bg-green-600" },
                      { topic: "Trigonometry", score: 68, color: "bg-red-500" },
                    ].map((item, idx) => (
                      <div key={idx}>
                        <div className="flex items-center justify-between mb-2">
                          <span className="text-sm font-medium">{item.topic}</span>
                          <span className="text-sm font-bold">{item.score}%</span>
                        </div>
                        <div className="h-3 bg-gray-200 rounded-full overflow-hidden border border-border">
                          <div 
                            className={`h-full ${item.color}`}
                            style={{ width: `${item.score}%` }}
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Engagement Metrics */}
            <Card>
              <CardHeader>
                <CardTitle>Student Engagement</CardTitle>
                <CardDescription>Activity patterns over the past week</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-7 gap-2">
                  {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map((day, idx) => (
                    <div key={day} className="text-center">
                      <p className="text-xs text-muted-foreground mb-2">{day}</p>
                      <div className="space-y-1">
                        {[...Array(5)].map((_, i) => (
                          <div
                            key={i}
                            className={`h-3 rounded ${
                              Math.random() > 0.3 ? 'bg-primary' : 'bg-muted'
                            }`}
                          />
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}

