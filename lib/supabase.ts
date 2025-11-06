// Mock Supabase client - No API needed!

export const supabase = {
  auth: {
    signUp: null,
    signInWithPassword: null,
    signOut: null,
    getUser: null,
    onAuthStateChange: null
  }
}

// Helper functions for auth - MOCK VERSION (No Supabase needed!)
export const auth = {
  signUp: async (email: string, password: string, metadata?: any) => {
    // Mock signup - always succeeds
    await new Promise(resolve => setTimeout(resolve, 500))
    return { 
      data: { 
        user: { 
          id: 'demo_user', 
          email, 
          user_metadata: metadata 
        },
        session: { access_token: 'mock_token' }
      }, 
      error: null 
    }
  },

  signIn: async (email: string, password: string) => {
    // Mock signin - always succeeds
    await new Promise(resolve => setTimeout(resolve, 500))
    return { 
      data: { 
        user: { 
          id: 'demo_user', 
          email,
          user_metadata: { role: 'student' }
        },
        session: { access_token: 'mock_token' }
      }, 
      error: null 
    }
  },

  signOut: async () => {
    // Mock signout
    await new Promise(resolve => setTimeout(resolve, 200))
    return { error: null }
  },

  getCurrentUser: async () => {
    // Mock get current user
    return {
      id: 'demo_user',
      email: 'demo@example.com',
      user_metadata: { role: 'student' }
    }
  },

  onAuthStateChange: (callback: (event: string, session: any) => void) => {
    // Mock auth state change
    return {
      data: { subscription: { unsubscribe: () => {} } }
    }
  }
}

