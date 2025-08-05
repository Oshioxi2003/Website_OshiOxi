import { useApi, useAsyncOperation } from './useApi';
import { blogService } from '../services';
import { BlogPost, Category, Tag, BlogStats } from '../types/api';

// Hook to get blog posts
export function useBlogPosts(params?: {
  page?: number;
  category?: string;
  tag?: string;
  search?: string;
  is_featured?: boolean;
  ordering?: string;
}) {
  return useApi(() => blogService.getPosts(params), [JSON.stringify(params)]);
}

// Hook to get single blog post
export function useBlogPost(slug: string) {
  return useApi(() => blogService.getPost(slug), [slug]);
}

// Hook to get featured posts
export function useFeaturedPosts() {
  return useApi(() => blogService.getFeaturedPosts(), []);
}

// Hook to get popular posts
export function usePopularPosts() {
  return useApi(() => blogService.getPopularPosts(), []);
}

// Hook to get recent posts
export function useRecentPosts() {
  return useApi(() => blogService.getRecentPosts(), []);
}

// Hook to get blog categories
export function useBlogCategories() {
  return useApi(() => blogService.getCategories(), []);
}

// Hook to get blog tags
export function useBlogTags() {
  return useApi(() => blogService.getTags(), []);
}

// Hook to get blog stats
export function useBlogStats() {
  return useApi(() => blogService.getStats(), []);
}

// Hook for comment submission
export function useCommentSubmission() {
  return useAsyncOperation<
    { message: string; comment_id: number },
    [{
      post: number;
      name: string;
      email: string;
      website?: string;
      content: string;
      parent?: number;
    }]
  >();
}