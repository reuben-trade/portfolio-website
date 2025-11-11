interface VideoEmbedProps {
  url: string;
  title?: string;
}

const VideoEmbed = ({ url, title = 'Video' }: VideoEmbedProps) => {
  const getEmbedUrl = (url: string): string | null => {
    // YouTube
    if (url.includes('youtube.com') || url.includes('youtu.be')) {
      const videoId = url.includes('youtu.be')
        ? url.split('youtu.be/')[1]?.split('?')[0]
        : new URLSearchParams(new URL(url).search).get('v');
      return videoId ? `https://www.youtube.com/embed/${videoId}` : null;
    }

    // Loom
    if (url.includes('loom.com')) {
      const videoId = url.split('/share/')[1]?.split('?')[0];
      return videoId ? `https://www.loom.com/embed/${videoId}` : null;
    }

    // Vimeo
    if (url.includes('vimeo.com')) {
      const videoId = url.split('vimeo.com/')[1]?.split('?')[0];
      return videoId ? `https://player.vimeo.com/video/${videoId}` : null;
    }

    return null;
  };

  const embedUrl = getEmbedUrl(url);

  if (!embedUrl) {
    return (
      <div className="bg-gray-100 rounded-lg p-8 text-center">
        <p className="text-gray-600">Video format not supported</p>
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-primary-600 hover:text-primary-700 mt-2 inline-block"
        >
          Watch on external site ↗
        </a>
      </div>
    );
  }

  return (
    <div className="relative w-full pb-[56.25%] rounded-lg overflow-hidden shadow-lg">
      <iframe
        src={embedUrl}
        title={title}
        className="absolute top-0 left-0 w-full h-full"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    </div>
  );
};

export default VideoEmbed;
