import { getPortfolioContent } from '@/lib/api';
import { ProjectCard } from '@/components/ProjectCard';

export default async function Home() {
  const data = await getPortfolioContent();
  const { personal, projects } = data;
  const featuredProjects = projects.filter(p => p.featured).slice(0, 3);

  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      {/* Hero Section */}
      <section className="py-20 text-center">
        <h1 className="text-5xl font-bold mb-4">{personal.name}</h1>
        <p className="text-2xl text-gray-600 mb-6">{personal.title}</p>
        <p className="text-lg text-gray-700 max-w-3xl mx-auto mb-8">
          {personal.bio}
        </p>
        <div className="flex gap-4 justify-center">
          <a
            href={personal.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
          >
            LinkedIn
          </a>
          <a
            href={personal.github}
            target="_blank"
            rel="noopener noreferrer"
            className="px-6 py-3 border border-gray-300 rounded-lg hover:border-primary-600 transition"
          >
            GitHub
          </a>
          <a
            href={`mailto:${personal.email}`}
            className="px-6 py-3 border border-gray-300 rounded-lg hover:border-primary-600 transition"
          >
            Contact
          </a>
        </div>
      </section>

      {/* Featured Projects */}
      <section className="py-12">
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-3xl font-bold">Featured Projects</h2>
          <a href="/projects" className="text-primary-600 hover:underline">
            View All →
          </a>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {featuredProjects.map((project) => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>
      </section>

      {/* Try AI Assistant */}
      <section className="py-12 bg-gray-50 rounded-lg px-8 mt-12">
        <h2 className="text-2xl font-bold mb-4 text-center">Try the AI Assistant</h2>
        <p className="text-gray-600 text-center mb-6">
          Click the chat icon in the bottom right to ask about my work!
        </p>
        <div className="flex flex-wrap gap-2 justify-center">
          <span className="px-4 py-2 bg-white rounded-full text-sm border">
            "Tell me about your ML projects"
          </span>
          <span className="px-4 py-2 bg-white rounded-full text-sm border">
            "What hackathons have you won?"
          </span>
          <span className="px-4 py-2 bg-white rounded-full text-sm border">
            "Show me the semantic search project"
          </span>
        </div>
      </section>
    </div>
  );
}