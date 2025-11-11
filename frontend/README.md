# Portfolio Frontend

React + TypeScript + Vite frontend for an AI-powered portfolio website.

## Features

- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS** for styling
- **Framer Motion** for animations
- **React Router** for navigation
- **AI Chat Widget** with text and voice input
- **Responsive Design** for all screen sizes

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Update environment variables if needed (default points to localhost:8000)

## Development

Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Building

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## Project Structure

```
src/
├── components/
│   ├── AIChat/        # AI chat widget components
│   ├── Projects/      # Project-related components
│   ├── Experience/    # Experience timeline components
│   └── Layout/        # Layout components (nav, footer)
├── pages/             # Page components
├── services/          # API and WebSocket services
├── hooks/             # Custom React hooks
├── types/             # TypeScript type definitions
├── App.tsx            # Main app component
└── main.tsx           # Entry point
```

## Features to Implement

- [ ] Integrate WebSocket for streaming chat responses
- [ ] Add error boundaries
- [ ] Implement loading states
- [ ] Add accessibility features
- [ ] Optimize performance
- [ ] Add analytics
