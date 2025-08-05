import { useApi } from './useApi';
import { pagesService } from '../services';
import { Page, Testimonial, TeamMember, PricingPlan, SiteStats } from '../types/api';

// Hook to get pages
export function usePages() {
  return useApi(() => pagesService.getPages(), []);
}

// Hook to get single page
export function usePage(slug: string) {
  return useApi(() => pagesService.getPage(slug), [slug]);
}

// Hook to get menu pages
export function useMenuPages() {
  return useApi(() => pagesService.getMenuPages(), []);
}

// Hook to get testimonials
export function useTestimonials() {
  return useApi(() => pagesService.getTestimonials(), []);
}

// Hook to get featured testimonials
export function useFeaturedTestimonials() {
  return useApi(() => pagesService.getFeaturedTestimonials(), []);
}

// Hook to get team members
export function useTeamMembers() {
  return useApi(() => pagesService.getTeamMembers(), []);
}

// Hook to get pricing plans
export function usePricingPlans() {
  return useApi(() => pagesService.getPricingPlans(), []);
}

// Hook to get site stats
export function useSiteStats() {
  return useApi(() => pagesService.getStats(), []);
}