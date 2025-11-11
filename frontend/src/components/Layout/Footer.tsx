const Footer = () => {
  return (
    <footer className="bg-gray-50 border-t border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center text-sm text-gray-600">
          <p>© {new Date().getFullYear()} AI Portfolio. All rights reserved.</p>
          <p className="mt-2">Built with FastAPI, React, and AI</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
