import { Project } from '@/lib/api';

interface ProjectCardProps {
  project: Project;
}

export function ProjectCard({ project }: ProjectCardProps) {
  return (
    <a
      href={`/projects/${project.id}`}
      className="block p-6 border rounded-lg hover:border-primary-600 hover:shadow-lg transition"
    >
      <h3 className="text-xl font-bold mb-2">{project.title}</h3>
      <p className="text-gray-600 mb-4">{project.description}</p>

      <div className="flex flex-wrap gap-2 mb-4">
        {project.tech_stack.slice(0, 3).map((tech) => (
          <span
            key={tech}
            className="px-2 py-1 bg-gray-100 rounded text-sm"
          >
            {tech}
          </span>
        ))}
        {project.tech_stack.length > 3 && (
          <span className="px-2 py-1 text-gray-500 text-sm">
            +{project.tech_stack.length - 3} more
          </span>
        )}
      </div>

      <div className="flex gap-2">
        {project.github_url && (
          <span className="text-sm text-primary-600">GitHub →</span>
        )}
        {project.demo_url && (
          <span className="text-sm text-primary-600">Demo →</span>
        )}
      </div>
    </a>
  );
}