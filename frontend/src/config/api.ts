// API Configuration
export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api/v1',
  BACKEND_URL: import.meta.env.VITE_BACKEND_URL || 'http://127.0.0.1:8000',
  TIMEOUT: 10000,
};

// API Endpoints
export const API_ENDPOINTS = {
  // Blog endpoints
  BLOG: {
    POSTS: '/blog/posts/',
    POST_DETAIL: (slug: string) => `/blog/posts/${slug}/`,
    FEATURED_POSTS: '/blog/posts/featured/',
    POPULAR_POSTS: '/blog/posts/popular/',
    RECENT_POSTS: '/blog/posts/recent/',
    CATEGORIES: '/blog/categories/',
    TAGS: '/blog/tags/',
    COMMENTS: '/blog/comments/',
    STATS: '/blog/stats/',
  },
  
  // Services endpoints
  SERVICES: {
    LIST: '/services/',
    DETAIL: (slug: string) => `/services/${slug}/`,
    FEATURED: '/services/featured/',
    CATEGORIES: '/services/categories/',
    INQUIRIES: '/services/inquiries/',
    STATS: '/services/stats/',
  },
  
  // Contact endpoints
  CONTACT: {
    MESSAGES: '/contact/messages/',
    NEWSLETTER: '/contact/newsletter/',
    FAQ: '/contact/faq/',
    FAQ_CATEGORIES: '/contact/faq/categories/',
    STATS: '/contact/stats/',
  },
  
  // Pages endpoints
  PAGES: {
    LIST: '/pages/',
    DETAIL: (slug: string) => `/pages/${slug}/`,
    MENU: '/pages/menu/',
    TESTIMONIALS: '/pages/testimonials/',
    FEATURED_TESTIMONIALS: '/pages/testimonials/featured/',
    TEAM: '/pages/team/',
    PRICING: '/pages/pricing/',
    STATS: '/pages/stats/',
  },
};