export interface Project {
  id: number;
  title: string;
  description: string;
  long_description?: string;
  technologies?: string[];
  video_url?: string;
  demo_url?: string;
  github_url?: string;
  image_url?: string;
  start_date?: string;
  end_date?: string;
  featured: boolean;
  created_at: string;
  updated_at: string;
}

export interface Experience {
  id: number;
  company: string;
  position: string;
  description?: string;
  location?: string;
  start_date: string;
  end_date?: string;
  current: boolean;
  technologies?: string[];
  achievements?: string[];
  created_at: string;
  updated_at: string;
}

export interface Achievement {
  id: number;
  title: string;
  description?: string;
  category?: string;
  date?: string;
  created_at: string;
}

export interface ChatMessage {
  message: string;
  conversation_id?: string;
}

export interface ChatResponse {
  response: string;
  conversation_id: string;
  sources?: any[];
}

export interface VoiceTranscription {
  text: string;
  confidence?: number;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}
