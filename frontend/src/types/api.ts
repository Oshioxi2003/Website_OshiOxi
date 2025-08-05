// Common API types
export interface ApiResponse<T> {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results?: T[];
}

export interface ApiError {
  message: string;
  status?: number;
  data?: any;
}

// Blog types
export interface User {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  description: string;
  posts_count: number;
}

export interface Tag {
  id: number;
  name: string;
  slug: string;
  posts_count: number;
}

export interface Comment {
  id: number;
  name: string;
  email?: string;
  website?: string;
  content: string;
  created_at: string;
  replies: Comment[];
}

export interface BlogPost {
  id: number;
  title: string;
  slug: string;
  author: User;
  category: Category | null;
  tags: Tag[];
  excerpt: string;
  content?: string;
  featured_image: string | null;
  is_featured: boolean;
  views_count: number;
  comments?: Comment[];
  comments_count: number;
  reading_time: number;
  related_posts?: BlogPost[];
  meta_title?: string;
  meta_description?: string;
  created_at: string;
  updated_at?: string;
  published_at?: string;
}

// Services types
export interface ServiceCategory {
  id: number;
  name: string;
  slug: string;
  description: string;
  icon: string;
  services_count: number;
}

export interface Service {
  id: number;
  name: string;
  slug: string;
  category: ServiceCategory | null;
  short_description: string;
  description?: string;
  featured_image: string | null;
  icon: string;
  features?: string[];
  starting_price: number | null;
  price_description: string;
  is_featured: boolean;
  order: number;
  related_services?: Service[];
  meta_title?: string;
  meta_description?: string;
}

export interface ServiceInquiry {
  service: number;
  name: string;
  email: string;
  phone?: string;
  company?: string;
  message: string;
  budget_range?: string;
  timeline?: string;
}

// Contact types
export interface ContactMessage {
  name: string;
  email: string;
  phone?: string;
  company?: string;
  subject: 'general' | 'support' | 'business' | 'quote' | 'feedback' | 'other';
  message: string;
}

export interface Newsletter {
  email: string;
  name?: string;
}

export interface FAQ {
  id: number;
  question: string;
  answer: string;
  category: string;
  order: number;
}

// Pages types
export interface Page {
  id: number;
  title: string;
  slug: string;
  content: string;
  excerpt: string;
  template: string;
  featured_image: string | null;
  meta_title?: string;
  meta_description?: string;
  created_at: string;
  updated_at?: string;
}

export interface Testimonial {
  id: number;
  name: string;
  position: string;
  company: string;
  content: string;
  avatar: string | null;
  rating: number;
  is_featured: boolean;
}

export interface TeamMember {
  id: number;
  name: string;
  position: string;
  bio: string;
  photo: string | null;
  email?: string;
  linkedin?: string;
  twitter?: string;
  github?: string;
}

export interface PricingPlan {
  id: number;
  name: string;
  description: string;
  price: number;
  price_period: string;
  features: string[];
  highlighted_features: string[];
  is_popular: boolean;
  button_text: string;
  button_link?: string;
}

// Stats types
export interface BlogStats {
  total_posts: number;
  total_categories: number;
  total_tags: number;
  total_views: number;
}

export interface ServiceStats {
  total_services: number;
  total_categories: number;
  total_inquiries: number;
  featured_services: number;
}

export interface ContactStats {
  total_messages: number;
  new_messages: number;
  newsletter_subscribers: number;
  total_faqs: number;
}

export interface SiteStats {
  total_pages: number;
  total_testimonials: number;
  team_members: number;
  pricing_plans: number;
}