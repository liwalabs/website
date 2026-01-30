# Liwa Labs - Technology Solutions

## Overview

This repository contains a complete, fully responsive multi-page website for Liwa Labs, a technology solutions company specializing in decentralized computing, HPC data centers, cloud solutions, and Web3 development. The project is built as a modern HTML website using Tailwind CSS for styling and follows a professional, clean design approach with custom branding and interactive features.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Static HTML Website**: Single-page application built with vanilla HTML
- **CSS Framework**: Tailwind CSS via CDN for rapid styling and responsive design
- **Typography**: Google Fonts (Inter) for consistent, modern typography
- **Styling Approach**: Utility-first CSS with Tailwind, supplemented by custom CSS variables for brand consistency

### Design System
- **Color Scheme**: Minimalist approach with white background (#FFFFFF) and dark navy text (#0D253F)
- **Typography**: Inter font family with multiple weights (300-700) for hierarchy
- **Responsive Design**: Built-in responsive capabilities through Tailwind CSS utilities

## Strategic Service Pillars

The website now showcases six comprehensive service areas:

1. **HPC Data Centers**: Building and managing high-performance computing (HPC) data centers optimized for large-scale crypto and Bitcoin mining operations
2. **Web3 & Blockchain Development**: Complete development stack including smart contract development, dApp creation, and blockchain integration services
3. **Web3 & Strategic Consulting**: Expert guidance for navigating the decentralized ecosystem with Web3 consultation and advanced technology training
4. **Financial Technology (FinTech)**: Advanced financial technology solutions integrating with Web3 development to create DeFi platforms and blockchain-based financial products
5. **Cloud & Data Infrastructure**: Scalable cloud computing and big data analytics providing essential off-chain and data processing support for high-performance applications
6. **Digital Asset Management**: Management of state-of-the-art Bitcoin mining infrastructure, positioning at the core of digital computation and asset creation

## Key Components

### Website Sections
1. **Sticky Navigation Bar**: Logo on left, navigation links on right, mobile hamburger menu
2. **Hero Section**: Company tagline, value proposition, and prominent CTA button
3. **Services Section**: Six strategic service pillars in responsive grid layout
4. **About Us/Team**: Four co-founder profiles with real biographies, achievements, and professional photos
5. **Contact Section**: Professional contact form and company information
6. **Footer**: Copyright, social media links (Instagram, Twitter/X)
7. **Dedicated Contact Page**: Comprehensive contact page with enhanced form, business hours, and detailed company information
8. **Dedicated Services Page**: Comprehensive services page with detailed descriptions, feature lists, and service-specific information for all six core service areas
9. **Dedicated About Page**: Complete about page featuring mission & vision, team leadership profiles, company values, and call-to-action sections
10. **Dedicated Projects Page**: Portfolio showcase featuring featured projects, project categories, statistics, and comprehensive project details with modern visual design

### HTML Structure
- Fully semantic HTML5 document structure
- Accessibility-focused design with proper ARIA labels
- Meta tags for proper viewport and character encoding
- Optimized for SEO and social sharing

### Styling System
- **Tailwind CSS CDN**: External stylesheet for utility classes
- **Custom CSS Variables**: Brand-specific colors defined in CSS custom properties
- **Google Fonts Integration**: Inter typeface with multiple weights (300-700)
- **Tailwind Configuration**: Extended configuration for custom accent blue color
- **Responsive Design**: Comprehensive mobile-first approach with sm:, md:, lg: breakpoints

### Interactive Features
- **Smooth Scrolling**: Enhanced JavaScript for navigation with sticky header offset
- **Mobile Menu**: Collapsible hamburger menu for mobile devices
- **Hover Effects**: Card animations, button interactions, and visual feedback
- **Form Functionality**: Professional contact form with validation-ready inputs

### Brand Identity
- **Primary Background**: White (#FFFFFF)
- **Primary Text**: Dark navy (#0D253F)
- **Accent Color**: Bright blue (#007BFF)
- **Typography**: Inter font family for modern, professional appearance

## Data Flow

This is a static website with no dynamic data flow:
1. HTML document loads in browser
2. External resources (Tailwind CSS, Google Fonts) are fetched via CDN
3. Custom styles are applied through embedded CSS
4. Page renders with complete styling and typography

## External Dependencies

### CDN Dependencies
- **Tailwind CSS**: `https://cdn.tailwindcss.com` - CSS framework for styling
- **Google Fonts**: Inter font family from Google Fonts API
- **Font Preconnections**: DNS prefetch for improved font loading performance

### No Backend Dependencies
- No server-side processing required
- No database connections
- No API integrations
- No authentication systems

## Deployment Strategy

### Static Hosting Compatible
This project is designed for static hosting deployment:
- **Hosting Options**: Any static hosting service (Netlify, Vercel, GitHub Pages, etc.)
- **Build Process**: No build step required - direct HTML deployment
- **CDN Requirements**: Relies on external CDNs for CSS framework and fonts
- **Performance**: Optimized for fast loading with font preconnections and CDN usage

### Deployment Fixes Applied (July 30, 2025)
Fixed deployment configuration issues by creating multiple deployment-compatible files:
- **main.py**: Python HTTP server with environment PORT variable support
- **start.py**: Alternative Python HTTP server entry point
- **Procfile**: Heroku-style deployment configuration (`web: python main.py`)
- **runtime.txt**: Python version specification (python-3.11)
- **Dockerfile**: Container deployment configuration
- **run.sh**: Shell script for simple deployment
- **server.js**: Node.js alternative server implementation

### Recent Updates (August 11, 2025)
- **Contact Information Integration**: Added phone number +92 326 2263160 to both home page and contact page with professional styling
- **Google Maps Integration**: Embedded interactive Google Maps showing exact Liwa Labs location at Tai Roshan Trade Center
- **AI & Mobile Solutions Projects**: Updated with correct projects (AITELLS, CALLWALA, EVE, SWIFT ME) with accurate descriptions
- **Location Features**: Clickable address links, Google Maps embed with "Get Directions" button, and location detail cards
- **Contact Page Reconstruction**: Recreated complete contact.html with comprehensive contact form and business information

### Deployment Considerations
- Ensure external CDN access for Tailwind CSS and Google Fonts
- Multiple server options available (Python HTTP server, Node.js)
- Environment PORT variable support for cloud deployments
- Mobile-responsive design ready for all device types
- Cross-browser compatible with modern browsers
- Google Maps embed requires stable internet connection for proper display

### Development Workflow
- Direct HTML editing for content changes
- Live preview capability in any web browser
- No compilation or build process needed
- Version control friendly (single HTML file)
- Current development server: Python HTTP server on port 5000
- Contact information and location data fully integrated across all pages