import axios from 'axios';
import type { Project, Experience, Achievement, ChatMessage, ChatResponse, VoiceTranscription } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Projects
export const getProjects = async (): Promise<Project[]> => {
  const response = await api.get('/api/content/projects');
  return response.data;
};

export const getProject = async (id: number): Promise<Project> => {
  const response = await api.get(`/api/content/projects/${id}`);
  return response.data;
};

// Experiences
export const getExperiences = async (): Promise<Experience[]> => {
  const response = await api.get('/api/content/experiences');
  return response.data;
};

// Achievements
export const getAchievements = async (): Promise<Achievement[]> => {
  const response = await api.get('/api/content/achievements');
  return response.data;
};

// Chat
export const sendChatMessage = async (message: ChatMessage): Promise<ChatResponse> => {
  const response = await api.post('/api/chat/', message);
  return response.data;
};

// Voice
export const transcribeAudio = async (audioBlob: Blob): Promise<VoiceTranscription> => {
  const formData = new FormData();
  formData.append('audio', audioBlob, 'audio.webm');

  const response = await api.post('/api/voice/transcribe', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  return response.data;
};

export default api;
