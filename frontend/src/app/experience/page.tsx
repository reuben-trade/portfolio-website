import { getPortfolioContent } from '@/lib/api';

export default async function ExperiencePage() {
  const data = await getPortfolioContent();
  const { experience } = data;

  return (
    <div className="max-w-4xl mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-4">Work Experience</h1>
      <p className="text-gray-600 mb-12">
        Professional experience building AI systems, backend infrastructure, and full-stack applications.
      </p>

      <div className="space-y-12">
        {experience.map((exp) => (
          <div key={exp.id} className="border-l-2 border-primary-600 pl-6">
            {/* Header */}
            <div className="mb-4">
              <h2 className="text-2xl font-bold">{exp.role}</h2>
              <div className="flex items-center gap-2 text-gray-600 mt-1">
                <span className="font-semibold">{exp.company}</span>
                <span>•</span>
                <span>{exp.duration}</span>
                <span>•</span>
                <span>{exp.location}</span>
              </div>
            </div>

            {/* Description */}
            <p className="text-gray-700 mb-4">{exp.description}</p>

            {/* Achievements */}
            <div className="mb-4">
              <h3 className="font-semibold mb-2">Key Achievements:</h3>
              <ul className="space-y-1">
                {exp.achievements.map((achievement, index) => (
                  <li key={index} className="flex items-start">
                    <span className="text-primary-600 mr-2">•</span>
                    <span className="text-gray-700">{achievement}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Tech Stack */}
            <div>
              <h3 className="font-semibold mb-2">Technologies:</h3>
              <div className="flex flex-wrap gap-2">
                {exp.tech_stack.map((tech) => (
                  <span
                    key={tech}
                    className="px-3 py-1 bg-gray-100 rounded-full text-sm"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}