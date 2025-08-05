import { Link } from "react-router-dom";
import { BlogPost } from "../../types/api";
import { API_CONFIG } from "../../config/api";

interface BlogCardProps {
  post: BlogPost;
  className?: string;
}

const BlogCard = ({ post, className = "" }: BlogCardProps) => {
  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  const getImageUrl = (imageUrl: string | null) => {
    if (!imageUrl) return "assets/img/placeholder-img.png";
    if (imageUrl.startsWith('http')) return imageUrl;
    return `${API_CONFIG.BACKEND_URL}${imageUrl}`;
  };

  return (
    <div className={`col-md-6 col-xl-4 ${className}`}>
      <Link to={`/blog/${post.slug}`} className="link d-block mb-6">
        <img
          src={getImageUrl(post.featured_image)}
          alt={post.title}
          className="img-fluid"
          style={{ height: '200px', objectFit: 'cover', width: '100%' }}
        />
      </Link>
      <div className="d-flex align-items-center flex-wrap gap-4 mb-2">
        {post.category && (
          <Link
            to={`/blog?category=${post.category.slug}`}
            className="link d-inline-block text-light hover:text-primary fs-14"
          >
            {post.category.name}
          </Link>
        )}
        <span className="d-inline-block fs-14 d-inline-block text-light text-opacity-50">
          {formatDate(post.created_at)}
        </span>
        <span className="d-inline-block fs-14 d-inline-block text-light text-opacity-50">
          {post.reading_time} min read
        </span>
      </div>
      <h5>
        <Link
          to={`/blog/${post.slug}`}
          className="link d-inline-block text-light hover:text-primary"
        >
          {post.title}
        </Link>
      </h5>
      <p className="fs-14 mb-6">
        {post.excerpt}
      </p>
      <div className="d-flex align-items-center justify-content-between mb-4">
        <div className="d-flex align-items-center gap-2">
          {post.tags.slice(0, 2).map((tag) => (
            <Link
              key={tag.id}
              to={`/blog?tag=${tag.slug}`}
              className="badge bg-secondary text-decoration-none"
            >
              {tag.name}
            </Link>
          ))}
        </div>
        <div className="text-light text-opacity-50 fs-14">
          <i className="bi bi-eye me-1"></i>
          {post.views_count} views
        </div>
      </div>
      <Link
        to={`/blog/${post.slug}`}
        className="btn btn-sm btn-outline-danger fs-14 rounded-pill"
      >
        <span className="d-inline-block">Read More</span>
        <span className="d-inline-block">
          <i className="bi bi-arrow-right"></i>
        </span>
      </Link>
    </div>
  );
};

export default BlogCard;