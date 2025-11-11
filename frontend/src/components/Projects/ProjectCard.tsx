import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import type { Project } from '../../types';

interface ProjectCardProps {
  project: Project;
}

const ProjectCard = ({ project }: ProjectCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      whileHover={{ y: -5 }}
      className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow"
    >
      {project.image_url && (
        <div className="h-48 bg-gray-200 overflow-hidden">
          <img
            src={project.image_url}
            alt={project.title}
            className="w-full h-full object-cover"
          />
        </div>
      )}

      <div className="p-6">
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-xl font-semibold text-gray-900">{project.title}</h3>
          {project.featured && (
            <span className="px-2 py-1 text-xs bg-primary-100 text-primary-800 rounded-full">
              Featured
            </span>
          )}
        </div>

        <p className="text-gray-600 text-sm mb-4 line-clamp-3">{project.description}</p>

        {project.technologies && project.technologies.length > 0 && (
          <div className="flex flex-wrap gap-2 mb-4">
            {project.technologies.slice(0, 4).map((tech, index) => (
              <span
                key={index}
                className="px-2 py-1 text-xs bg-gray-100 text-gray-700 rounded"
              >
                {tech}
              </span>
            ))}
            {project.technologies.length > 4 && (
              <span className="px-2 py-1 text-xs bg-gray-100 text-gray-700 rounded">
                +{project.technologies.length - 4} more
              </span>
            )}
          </div>
        )}

        <div className="flex space-x-3">
          <Link
            to={`/projects/${project.id}`}
            className="text-primary-600 hover:text-primary-700 text-sm font-medium"
          >
            View Details →
          </Link>
          {project.github_url && (
            <a
              href={project.github_url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-600 hover:text-gray-700 text-sm font-medium"
            >
              GitHub ↗
            </a>
          )}
          {project.demo_url && (
            <a
              href={project.demo_url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-600 hover:text-gray-700 text-sm font-medium"
            >
              Demo ↗
            </a>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default ProjectCard;
