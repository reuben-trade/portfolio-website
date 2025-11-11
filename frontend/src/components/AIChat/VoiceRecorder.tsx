import { useState } from 'react';
import { motion } from 'framer-motion';
import { useVoiceRecorder } from '../../hooks/useVoiceRecorder';

interface VoiceRecorderProps {
  onTranscription: (text: string) => void;
}

const VoiceRecorder = ({ onTranscription }: VoiceRecorderProps) => {
  const { isRecording, isProcessing, startRecording, stopRecording } = useVoiceRecorder();
  const [error, setError] = useState<string>('');

  const handleClick = async () => {
    try {
      setError('');
      if (isRecording) {
        const text = await stopRecording();
        onTranscription(text);
      } else {
        await startRecording();
      }
    } catch (err) {
      setError('Failed to record audio');
      console.error(err);
    }
  };

  return (
    <div className="relative">
      <motion.button
        onClick={handleClick}
        disabled={isProcessing}
        className={`p-2 rounded-lg transition-colors ${
          isRecording
            ? 'bg-red-600 text-white'
            : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
        } disabled:opacity-50 disabled:cursor-not-allowed`}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        {isProcessing ? '⏳' : isRecording ? '⏹️' : '🎤'}
      </motion.button>

      {isRecording && (
        <motion.div
          className="absolute -top-1 -right-1 w-3 h-3 bg-red-600 rounded-full"
          animate={{ scale: [1, 1.2, 1] }}
          transition={{ repeat: Infinity, duration: 1 }}
        />
      )}

      {error && (
        <div className="absolute bottom-full mb-2 right-0 bg-red-100 text-red-700 text-xs px-2 py-1 rounded whitespace-nowrap">
          {error}
        </div>
      )}
    </div>
  );
};

export default VoiceRecorder;
