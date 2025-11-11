import { getPortfolioContent } from '@/lib/api';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  const data = await getPortfolioContent();
  return data.projects.map((project) => ({
    id: project.id,
  }));
}

export default async function ProjectPage({
  params,
}: {
  params: { id: string };
}) {
  const data = await getPortfolioContent();
  const project = data.projects.find((p) => p.id === params.id);

  if (!project) {
    notFound();
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-12">
      {/* Back button */}
      <a href="/projects" className="text-primary-600 hover:underline mb-6 inline-block">
        ← Back to Projects
      </a>

      {/* Project Header */}
      <h1 className="text-4xl font-bold mb-4">{project.title}</h1>
      <p className="text-xl text-gray-600 mb-8">{project.description}</p>

      {/* Links */}
      <div className="flex gap-4 mb-8">
        {project.github_url && (
          <a
            href={project.github_url}
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 border border-gray-300 rounded-lg hover:border-primary-600 transition"
          >
            GitHub →
          </a>
        )}
        {project.demo_url && (
          <a
            href={project.demo_url}
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
          >
            Live Demo →
          </a>
        )}
      </div>

      {/* Video Embed */}
      {project.video_url && (
        <div className="mb-8 rounded-lg overflow-hidden bg-gray-100 aspect-video">
          <iframe
            src={project.video_url}
            className="w-full h-full"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      )}

      {/* Description */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-4">About</h2>
        <p className="text-gray-700 leading-relaxed whitespace-pre-line">
          {project.long_description}
        </p>
      </section>

      {/* Highlights */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Key Achievements</h2>
        <ul className="space-y-2">
          {project.highlights.map((highlight, index) => (
            <li key={index} className="flex items-start">
              <span className="text-primary-600 mr-2">✓</span>
              <span>{highlight}</span>
            </li>
          ))}
        </ul>
      </section>

      {/* Tech Stack */}
      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Technologies Used</h2>
        <div className="flex flex-wrap gap-2">
          {project.tech_stack.map((tech) => (
            <span
              key={tech}
              className="px-3 py-1 bg-gray-100 rounded-full text-sm"
            >
              {tech}
            </span>
          ))}
        </div>
      </section>
    </div>
  );
}