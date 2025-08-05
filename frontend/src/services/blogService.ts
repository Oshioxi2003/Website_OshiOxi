import apiClient from './api';
import { API_ENDPOINTS } from '../config/api';
import { BlogPost, Category, Tag, Comment, BlogStats, ApiResponse } from '../types/api';

export const blogService = {
  // Get all blog posts with optional filters
  getPosts: async (params?: {
    page?: number;
    category?: string;
    tag?: string;
    search?: string;
    is_featured?: boolean;
    ordering?: string;
  }): Promise<ApiResponse<BlogPost>> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.POSTS, { params });
    return response.data;
  },

  // Get single blog post by slug
  getPost: async (slug: string): Promise<BlogPost> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.POST_DETAIL(slug));
    return response.data;
  },

  // Get featured posts
  getFeaturedPosts: async (): Promise<BlogPost[]> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.FEATURED_POSTS);
    return response.data;
  },

  // Get popular posts
  getPopularPosts: async (): Promise<BlogPost[]> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.POPULAR_POSTS);
    return response.data;
  },

  // Get recent posts
  getRecentPosts: async (): Promise<BlogPost[]> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.RECENT_POSTS);
    return response.data;
  },

  // Get all categories
  getCategories: async (): Promise<Category[]> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.CATEGORIES);
    return response.data;
  },

  // Get all tags
  getTags: async (): Promise<Tag[]> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.TAGS);
    return response.data;
  },

  // Create comment
  createComment: async (commentData: {
    post: number;
    name: string;
    email: string;
    website?: string;
    content: string;
    parent?: number;
  }): Promise<{ message: string; comment_id: number }> => {
    const response = await apiClient.post(API_ENDPOINTS.BLOG.COMMENTS, commentData);
    return response.data;
  },

  // Get blog stats
  getStats: async (): Promise<BlogStats> => {
    const response = await apiClient.get(API_ENDPOINTS.BLOG.STATS);
    return response.data;
  },
};