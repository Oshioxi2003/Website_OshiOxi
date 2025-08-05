import apiClient from './api';
import { API_ENDPOINTS } from '../config/api';
import { Page, Testimonial, TeamMember, PricingPlan, SiteStats, ApiResponse } from '../types/api';

export const pagesService = {
  // Get all pages
  getPages: async (): Promise<Page[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.LIST);
    return response.data;
  },

  // Get single page by slug
  getPage: async (slug: string): Promise<Page> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.DETAIL(slug));
    return response.data;
  },

  // Get menu pages
  getMenuPages: async (): Promise<Page[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.MENU);
    return response.data;
  },

  // Get all testimonials
  getTestimonials: async (): Promise<Testimonial[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.TESTIMONIALS);
    return response.data;
  },

  // Get featured testimonials
  getFeaturedTestimonials: async (): Promise<Testimonial[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.FEATURED_TESTIMONIALS);
    return response.data;
  },

  // Get team members
  getTeamMembers: async (): Promise<TeamMember[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.TEAM);
    return response.data;
  },

  // Get pricing plans
  getPricingPlans: async (): Promise<PricingPlan[]> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.PRICING);
    return response.data;
  },

  // Get site stats
  getStats: async (): Promise<SiteStats> => {
    const response = await apiClient.get(API_ENDPOINTS.PAGES.STATS);
    return response.data;
  },
};