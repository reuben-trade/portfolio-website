import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { AIChat } from '@/components/AIChat';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Reuben Stanley | Backend Developer & AI Engineer',
  description: 'Portfolio of Reuben Stanley - Honours Computer Science student (AI) at UWA with experience in production-grade AI systems, embeddings, and backend development.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav className="border-b">
          <div className="max-w-6xl mx-auto px-4 py-4">
            <div className="flex justify-between items-center">
              <a href="/" className="text-xl font-bold">
                Reuben Stanley
              </a>
              <div className="flex gap-6">
                <a href="/" className="hover:text-primary-600">Home</a>
                <a href="/projects" className="hover:text-primary-600">Projects</a>
                <a href="/experience" className="hover:text-primary-600">Experience</a>
              </div>
            </div>
          </div>
        </nav>

        <main className="min-h-screen">
          {children}
        </main>

        <footer className="border-t mt-20">
          <div className="max-w-6xl mx-auto px-4 py-8 text-center text-gray-600">
            <p>© 2025 Reuben Stanley. Built with Next.js & FastAPI.</p>
          </div>
        </footer>

        {/* AI Chat Widget - available on all pages */}
        <AIChat />
      </body>
    </html>
  );
}