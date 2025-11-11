import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import Timeline from '../components/Experience/Timeline';
import { getExperiences } from '../services/api';
import type { Experience as ExperienceType } from '../types';

const Experience = () => {
  const [experiences, setExperiences] = useState<ExperienceType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const fetchExperiences = async () => {
      try {
        const data = await getExperiences();
        setExperiences(data);
      } catch (err) {
        setError('Failed to load experiences');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchExperiences();
  }, []);

  return (
    <div className="min-h-screen pt-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center mb-12"
        >
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Experience</h1>
          <p className="text-lg text-gray-600">
            My professional journey and key achievements
          </p>
        </motion.div>

        {loading && (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
            <p className="mt-4 text-gray-600">Loading experiences...</p>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}

        {!loading && !error && experiences.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-600">No experiences found.</p>
          </div>
        )}

        {!loading && !error && experiences.length > 0 && (
          <div className="py-8">
            <Timeline experiences={experiences} />
          </div>
        )}
      </div>
    </div>
  );
};

export default Experience;
