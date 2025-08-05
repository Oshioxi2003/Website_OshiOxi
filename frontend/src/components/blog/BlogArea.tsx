import { Link } from "react-router-dom";
import { useBlogPosts } from "../../hooks";
import BlogCard from "../common/BlogCard";

const BlogArea = () => {
	const { data: postsResponse, loading, error } = useBlogPosts({ page: 1 });
	const posts = postsResponse?.results || [];

	if (loading) {
		return (
			<div className="section-space-y">
				<div className="container">
					<div className="text-center">
						<div className="spinner-border text-primary" role="status">
							<span className="visually-hidden">Loading...</span>
						</div>
					</div>
				</div>
			</div>
		);
	}

	if (error) {
		return (
			<div className="section-space-y">
				<div className="container">
					<div className="text-center text-danger">
						<p>Error loading blog posts: {error.message}</p>
					</div>
				</div>
			</div>
		);
	}

	return (
		<>
			<div className="section-space-y">
				<div className="section-space-sm-bottom">
					<div className="container">
						<div className="row g-4 align-items-center">
							<div className="col-md-6">
								<h2 className="text-light mb-0" data-cue="fadeIn">
									Our Blogs
								</h2>
							</div>
							<div className="col-md-6 text-md-end">
								<Link
									to="/blog"
									className="btn btn-outline-primary btn-sm rounded-pill"
								>
									View All Posts
									<i className="bi bi-arrow-right ms-2"></i>
								</Link>
							</div>
						</div>
					</div>
				</div>
				<div className="container">
					<div className="row g-4" data-cues="fadeIn">
						{posts.length > 0 ? (
							posts.slice(0, 6).map((post) => (
								<BlogCard key={post.id} post={post} />
							))
						) : (
							<div className="col-12 text-center">
								<p className="text-light text-opacity-75">No blog posts found.</p>
							</div>
						)}
					</div>
				</div>
			</div>
		</>
	);
};

export default BlogArea;
