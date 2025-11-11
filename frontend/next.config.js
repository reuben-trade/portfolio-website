/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['loom.com', 'www.loom.com', 'youtube.com', 'www.youtube.com'],
  },
}

module.exports = nextConfig