import Link from "next/link";
import { Button } from "@/components/ui/button";
import { BookOpen, GraduationCap, BarChart3, Sparkles, Zap, Brain } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="backdrop-blur-md bg-card/50 border-b border-border sticky top-0 z-50">
        <div className="container mx-auto px-6 py-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-br from-primary to-accent p-2.5 rounded-xl shadow-lg">
              <Sparkles className="h-6 w-6 text-white" />
            </div>
            <span className="text-2xl font-black text-foreground tracking-tight">Study With Bob</span>
          </div>
          <nav className="flex gap-2">
            <Link href="/student">
              <Button variant="ghost" className="text-foreground hover:text-primary hover:bg-primary/10 font-medium">For Students</Button>
            </Link>
            <Link href="/teacher">
              <Button variant="ghost" className="text-foreground hover:text-primary hover:bg-primary/10 font-medium">For Teachers</Button>
            </Link>
            <Link href="/login">
              <Button className="bg-primary hover:bg-primary/90 text-white font-bold shadow-lg shadow-primary/30">Sign In</Button>
            </Link>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <main className="relative">
        {/* Gradient background */}
        <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-background to-accent/10 pointer-events-none" />
        
        <div className="container mx-auto px-6 py-24 relative">
          <div className="text-center max-w-5xl mx-auto">
            <div className="inline-block mb-6 animate-pulse">
              <span className="bg-gradient-to-r from-primary to-accent text-white px-6 py-2.5 rounded-full text-sm font-black tracking-wide shadow-lg shadow-primary/30">
                NO API KEYS NEEDED
              </span>
            </div>
            <h1 className="text-7xl md:text-8xl font-black mb-8 text-foreground tracking-tight leading-none">
              Supercharge
              <br />
              <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
                Canvas Search
              </span>
            </h1>
            <p className="text-2xl mb-12 text-muted-foreground leading-relaxed max-w-3xl mx-auto">
              Get instant answers to any course question with our AI-powered Canvas assistant. 
              Find exactly what you need, when you need it.
            </p>
            <div className="flex gap-5 justify-center flex-wrap">
              <Link href="/student">
                <Button size="lg" className="gap-3 bg-primary hover:bg-primary/90 text-white text-lg px-12 py-7 font-black shadow-2xl shadow-primary/40 hover:shadow-primary/60 hover:scale-105 transition-all">
                  <GraduationCap className="h-7 w-7" />
                  Start Learning
                </Button>
              </Link>
              <Link href="/teacher">
                <Button size="lg" variant="outline" className="gap-3 border-2 border-primary text-primary hover:bg-primary hover:text-white text-lg px-12 py-7 font-black shadow-xl hover:scale-105 transition-all">
                  <BarChart3 className="h-7 w-7" />
                  I'm a Teacher
                </Button>
              </Link>
            </div>
          </div>

          {/* Features Grid */}
          <div className="grid md:grid-cols-3 gap-6 mt-28">
            <div className="group relative bg-card border border-border rounded-2xl p-8 shadow-xl hover:shadow-2xl hover:shadow-primary/20 hover:-translate-y-2 transition-all duration-300">
              <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity" />
              <div className="relative">
                <div className="h-16 w-16 bg-gradient-to-br from-primary to-accent rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-primary/30">
                  <Zap className="h-9 w-9 text-white" />
                </div>
                <h3 className="text-2xl font-black mb-4 text-foreground">Instant Search</h3>
                <p className="text-muted-foreground leading-relaxed text-lg">
                  Find content across all your courses instantly. No more digging through multiple pages.
                </p>
              </div>
            </div>

            <div className="group relative bg-card border border-border rounded-2xl p-8 shadow-xl hover:shadow-2xl hover:shadow-accent/20 hover:-translate-y-2 transition-all duration-300">
              <div className="absolute inset-0 bg-gradient-to-br from-accent/5 to-transparent rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity" />
              <div className="relative">
                <div className="h-16 w-16 bg-gradient-to-br from-accent to-primary rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-accent/30">
                  <Brain className="h-9 w-9 text-white" />
                </div>
                <h3 className="text-2xl font-black mb-4 text-foreground">AI-Powered</h3>
                <p className="text-muted-foreground leading-relaxed text-lg">
                  Get accurate answers based on your course content. Smart hints without giving away solutions.
                </p>
              </div>
            </div>

            <div className="group relative bg-card border border-border rounded-2xl p-8 shadow-xl hover:shadow-2xl hover:shadow-primary/20 hover:-translate-y-2 transition-all duration-300">
              <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity" />
              <div className="relative">
                <div className="h-16 w-16 bg-gradient-to-br from-primary to-accent rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-primary/30">
                  <BookOpen className="h-9 w-9 text-white" />
                </div>
                <h3 className="text-2xl font-black mb-4 text-foreground">Chat Interface</h3>
                <p className="text-muted-foreground leading-relaxed text-lg">
                  Ask questions about assignments, deadlines, or materials through a simple chat.
                </p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

