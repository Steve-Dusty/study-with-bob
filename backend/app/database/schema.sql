-- Study With Bob Database Schema for Supabase/PostgreSQL

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";  -- For pgvector (embeddings)

-- ==================== Users & Auth ====================
-- Note: Supabase provides auth.users table by default
-- We extend it with our custom tables

-- Students table
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    grade_level INTEGER,
    class_id UUID,
    total_score INTEGER DEFAULT 0,
    problems_solved INTEGER DEFAULT 0,
    accuracy FLOAT DEFAULT 0.0,
    streak_days INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Teachers table
CREATE TABLE teachers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Classes
CREATE TABLE classes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    teacher_id UUID REFERENCES teachers(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ==================== Problems & Content ====================

-- Problems
CREATE TABLE problems (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    expected_answer TEXT NOT NULL,
    topic TEXT NOT NULL,
    difficulty TEXT CHECK (difficulty IN ('easy', 'medium', 'hard')),
    hints JSONB,  -- Array of hints
    explanation TEXT,
    created_by UUID REFERENCES teachers(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ==================== Submissions & Progress ====================

-- Student submissions
CREATE TABLE submissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id) ON DELETE CASCADE,
    answer TEXT NOT NULL,
    correct BOOLEAN NOT NULL,
    attempts INTEGER DEFAULT 1,
    image_data TEXT,  -- Base64 encoded image
    confidence FLOAT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Student progress by topic (for spaced repetition)
CREATE TABLE student_topics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    topic TEXT NOT NULL,
    strength FLOAT DEFAULT 0.0,  -- 0-1 mastery level
    level INTEGER DEFAULT 0,  -- Spaced repetition level
    last_reviewed TIMESTAMP WITH TIME ZONE,
    next_review TIMESTAMP WITH TIME ZONE,
    total_correct INTEGER DEFAULT 0,
    total_attempts INTEGER DEFAULT 0,
    UNIQUE(student_id, topic)
);

-- ==================== Assignments ====================

-- Assignments
CREATE TABLE assignments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    teacher_id UUID REFERENCES teachers(id) ON DELETE CASCADE,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    due_date TIMESTAMP WITH TIME ZONE,
    problem_ids INTEGER[],
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'closed', 'draft')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Assignment submissions
CREATE TABLE assignment_submissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assignment_id UUID REFERENCES assignments(id) ON DELETE CASCADE,
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id),
    answer TEXT,
    score INTEGER,
    feedback TEXT,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    graded_at TIMESTAMP WITH TIME ZONE,
    UNIQUE(assignment_id, student_id, problem_id)
);

-- ==================== Vector Embeddings (for personalization) ====================

-- Student struggle embeddings
CREATE TABLE struggle_embeddings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    problem_id INTEGER REFERENCES problems(id),
    topic TEXT,
    error_description TEXT,
    embedding vector(1536),  -- For OpenAI embeddings
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for vector similarity search
CREATE INDEX ON struggle_embeddings USING ivfflat (embedding vector_cosine_ops);

-- ==================== Indexes for Performance ====================

CREATE INDEX idx_students_user_id ON students(user_id);
CREATE INDEX idx_students_class_id ON students(class_id);
CREATE INDEX idx_submissions_student_id ON submissions(student_id);
CREATE INDEX idx_submissions_problem_id ON submissions(problem_id);
CREATE INDEX idx_submissions_created_at ON submissions(created_at DESC);
CREATE INDEX idx_problems_topic ON problems(topic);
CREATE INDEX idx_student_topics_student_id ON student_topics(student_id);
CREATE INDEX idx_student_topics_next_review ON student_topics(next_review);
CREATE INDEX idx_assignments_class_id ON assignments(class_id);
CREATE INDEX idx_assignment_submissions_assignment_id ON assignment_submissions(assignment_id);
CREATE INDEX idx_assignment_submissions_student_id ON assignment_submissions(student_id);

-- ==================== Row Level Security (RLS) ====================

-- Enable RLS on all tables
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
ALTER TABLE teachers ENABLE ROW LEVEL SECURITY;
ALTER TABLE classes ENABLE ROW LEVEL SECURITY;
ALTER TABLE problems ENABLE ROW LEVEL SECURITY;
ALTER TABLE submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE student_topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE assignments ENABLE ROW LEVEL SECURITY;
ALTER TABLE assignment_submissions ENABLE ROW LEVEL SECURITY;

-- Students can only see their own data
CREATE POLICY "Students can view own data" ON students
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Students can update own data" ON students
    FOR UPDATE USING (auth.uid() = user_id);

-- Students can view their own submissions
CREATE POLICY "Students can view own submissions" ON submissions
    FOR SELECT USING (
        student_id IN (SELECT id FROM students WHERE user_id = auth.uid())
    );

-- Teachers can view all data for their classes
CREATE POLICY "Teachers can view class data" ON students
    FOR SELECT USING (
        class_id IN (SELECT id FROM classes WHERE teacher_id IN (
            SELECT id FROM teachers WHERE user_id = auth.uid()
        ))
    );

-- ==================== Functions ====================

-- Update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for updated_at
CREATE TRIGGER update_students_updated_at BEFORE UPDATE ON students
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_teachers_updated_at BEFORE UPDATE ON teachers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

