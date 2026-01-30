#!/usr/bin/env python3

import os
import re

# Define the standardized header HTML
STANDARD_HEADER = '''    <!-- Sticky Navigation Bar -->
    <header class="w-full sticky top-0 bg-white/95 backdrop-blur-sm border-b border-gray-100 z-50">
        <nav class="container mx-auto px-4 py-3">
            <div class="flex items-center justify-between">
                <!-- Logo -->
                <div class="flex items-center">
                    <a href="index.html" class="flex items-center">
                        <img src="./attached_assets/Logo-transparent_1754605962039.png" alt="Liwa Labs Logo" class="logo w-auto">
                    </a>
                </div>
                
                <!-- Navigation Links -->
                <div class="hidden md:flex items-center space-x-8">
                    <a href="index.html" class="nav-link text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium">Home</a>
                    <a href="services.html" class="nav-link text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium">Services</a>
                    <a href="projects.html" class="nav-link text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium">Projects</a>
                    <a href="about.html" class="nav-link text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium">About</a>
                    <a href="contact.html" class="nav-link text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium">Contact</a>
                </div>
                
                <!-- Mobile Menu Button -->
                <div class="md:hidden">
                    <button id="mobile-menu-button" class="text-primary-text hover:text-accent-blue focus:outline-none" aria-label="Toggle navigation menu">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
            
            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden md:hidden mt-4 pb-4">
                <div class="flex flex-col space-y-4">
                    <a href="index.html" class="nav-link-mobile text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium py-2">Home</a>
                    <a href="services.html" class="nav-link-mobile text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium py-2">Services</a>
                    <a href="projects.html" class="nav-link-mobile text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium py-2">Projects</a>
                    <a href="about.html" class="nav-link-mobile text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium py-2">About</a>
                    <a href="contact.html" class="nav-link-mobile text-primary-text hover:text-accent-blue transition-colors duration-200 font-medium py-2">Contact</a>
                </div>
            </div>
        </nav>
    </header>'''

# Define the standardized footer HTML
STANDARD_FOOTER = '''    <!-- Footer -->
    <footer class="bg-primary-text text-white py-12 lg:py-16">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <div class="mb-6">
                    <img src="./attached_assets/Logo-transparent_1754605962039.png" alt="Liwa Labs" class="logo mx-auto filter invert">
                </div>
                <p class="text-gray-300 mb-8 max-w-2xl mx-auto text-base sm:text-lg leading-relaxed">
                    Pioneering the future of technology through innovative solutions in Web3, blockchain, HPC data centers, and cutting-edge digital infrastructure.
                </p>
                
                <div class="flex justify-center space-x-4 sm:space-x-6">
                    <!-- Instagram Icon -->
                    <a href="https://www.instagram.com/liwalabs" target="_blank" rel="noopener noreferrer" 
                       class="w-8 h-8 sm:w-10 sm:h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-white/20 transition-colors duration-200">
                        <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                        </svg>
                    </a>
                    
                    <!-- Twitter/X Icon -->
                    <a href="https://twitter.com/liwalabs" target="_blank" rel="noopener noreferrer" 
                       class="w-8 h-8 sm:w-10 sm:h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-white/20 transition-colors duration-200">
                        <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.80l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                        </svg>
                    </a>
                </div>
            </div>
            
            <div class="border-t border-gray-700 mt-8 pt-8 text-center">
                <p class="text-gray-400 text-sm">
                    © 2025 Liwa Labs. All rights reserved.
                </p>
            </div>
        </div>
    </footer>'''

# Define the standardized JavaScript
STANDARD_JS = '''    <!-- Navigation JavaScript -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            
            if (mobileMenuButton && mobileMenu) {
                mobileMenuButton.addEventListener('click', function() {
                    mobileMenu.classList.toggle('hidden');
                });
                
                // Close mobile menu when clicking on a link
                const mobileMenuLinks = mobileMenu.querySelectorAll('a');
                mobileMenuLinks.forEach(link => {
                    link.addEventListener('click', function() {
                        mobileMenu.classList.add('hidden');
                    });
                });
            }
            
            // Set active navigation link
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            const navLinks = document.querySelectorAll('.nav-link, .nav-link-mobile');
            
            navLinks.forEach(link => {
                const href = link.getAttribute('href');
                if (href === currentPage || 
                    (currentPage === '' && href === 'index.html') ||
                    (currentPage === 'index.html' && href === 'index.html')) {
                    link.classList.remove('text-primary-text');
                    link.classList.add('text-accent-blue', 'font-semibold');
                }
            });
            
            // Smooth scrolling for anchor links with offset for sticky header
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        const headerHeight = 80; // Account for sticky header
                        const targetPosition = target.offsetTop - headerHeight;
                        
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // Add smooth scrolling class to HTML for better browser support
            document.documentElement.style.scrollBehavior = 'smooth';
        });
    </script>'''

def update_html_file(filename):
    """Update a single HTML file with standardized header and footer"""
    
    if not os.path.exists(filename):
        print(f"Skipping {filename} - file does not exist")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header - find from <header to </header>
    header_pattern = r'(\s*<!-- Sticky Navigation Bar -->\s*<header.*?</header>)'
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(header_pattern, STANDARD_HEADER, content, flags=re.DOTALL)
        print(f"Updated header in {filename}")
    else:
        print(f"Header pattern not found in {filename}")
    
    # Replace footer - find from <!-- Footer --> to </footer>
    footer_pattern = r'(\s*<!-- Footer -->\s*<footer.*?</footer>)'
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, STANDARD_FOOTER, content, flags=re.DOTALL)
        print(f"Updated footer in {filename}")
    else:
        print(f"Footer pattern not found in {filename}")
        
    # Replace JavaScript - find the script section
    js_pattern = r'(\s*<!-- .*?JavaScript -->\s*<script>.*?</script>)'
    if re.search(js_pattern, content, re.DOTALL):
        content = re.sub(js_pattern, STANDARD_JS, content, flags=re.DOTALL)
        print(f"Updated JavaScript in {filename}")
    else:
        # If no existing script section, add it before </body>
        content = content.replace('</body>', f'{STANDARD_JS}\n</body>')
        print(f"Added JavaScript to {filename}")
    
    # Write the updated content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated {filename}")

# List of HTML files to update
html_files = [
    'services.html',
    'about.html', 
    'contact.html',
    'projects.html'
]

print("Starting to update HTML files with standardized header and footer...")

for filename in html_files:
    print(f"\nProcessing {filename}...")
    update_html_file(filename)

print("\nAll files have been updated with standardized header and footer!")
print("Now any changes to header/footer can be made by running this script again.")
