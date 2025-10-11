# Overview

This is a personal portfolio website for KR Sai Varun, built with Streamlit. The portfolio showcases professional skills, projects, blog posts, and testimonials. It features interactive data visualizations using Plotly, analytics tracking, contact form functionality, and a comprehensive content management system for skills, projects, blog posts, and testimonials.

The application serves as both a professional showcase and a demonstration of the developer's capabilities in data visualization, web development, and full-stack development.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Framework Choice: Streamlit**
- **Rationale**: Streamlit provides rapid development for data-focused web applications with built-in Python integration
- **Pros**: Simple deployment, native Python support, built-in state management, easy data visualization integration
- **Cons**: Limited customization compared to traditional frontend frameworks, less control over UI/UX details

**Visualization Library: Plotly**
- **Purpose**: Interactive charts and graphs for skills proficiency, analytics dashboards, and project metrics
- **Chosen for**: Interactive capabilities, professional appearance, seamless Plotly Express and Graph Objects integration

**Custom Styling**
- Dark theme implemented through custom CSS injected via st.markdown()
- Gradient headers and styled components for visual appeal
- Responsive card-based layouts for skills, projects, and testimonials

## Data Layer Architecture

**File-based Data Storage**
- **Structure**: Python modules in `/data` directory containing functions that return structured dictionaries/lists
- **Rationale**: Lightweight solution suitable for static portfolio content without database overhead
- **Files**:
  - `skills_data.py`: Skills categorized by type with proficiency percentages
  - `projects_data.py`: Project portfolio with descriptions, technologies, and links
  - `blog_data.py`: Blog posts with markdown content, metadata, and categorization
  - `testimonials_data.py`: Client testimonials with ratings and filtering capabilities

**JSON-based Analytics Storage**
- `analytics.json`: Stores page view metrics, engagement data, and activity logs
- Sample data generation for demonstration purposes
- Time-series data for trend visualization

**Contact Messages Storage**
- `contact_messages.json`: Fallback storage for contact form submissions
- Structured with timestamp, sender info, and message content

## Backend Services

**Email Handler (`utils/email_handler.py`)**
- SMTP integration for contact form submissions
- Fallback to local JSON storage if email configuration unavailable
- Gmail SMTP server configuration ready

**Analytics System (`utils/analytics.py`)**
- Page view tracking across different sections
- Engagement metrics calculation
- Trend analysis with date-based aggregation
- Sample data generation for demonstration

## Content Management

**Blog System**
- Full blog post management with markdown content support
- Category and tag-based filtering
- Recent posts and featured content capabilities
- Individual post retrieval by ID or slug

**Skills Presentation**
- Category-based skill grouping (Data Tools, Programming, Web Development, AI/ML)
- Percentage-based proficiency visualization
- Support for skill filtering and display customization

**Project Portfolio**
- Technology stack tagging
- Category classification
- GitHub and live demo link integration
- Detailed project descriptions

**Testimonials**
- Star rating system (1-5 scale)
- Featured testimonials selection
- Average rating calculation
- Company and role attribution

## Application Entry Point

**Main Application (`app.py`)**
- Streamlit page configuration with custom theme
- Section-based navigation (Home, About, Skills, Projects, Blog, Testimonials, Contact)
- Modular data loading from separate data modules
- Integration of all utility functions for email and analytics

# External Dependencies

## Python Libraries

**Core Framework**
- `streamlit`: Main web application framework for UI and deployment

**Data Visualization**
- `plotly.express`: High-level plotting interface
- `plotly.graph_objects`: Custom interactive visualizations
- `pandas`: Data manipulation and analysis

**Image Processing**
- `PIL (Pillow)`: Image handling and processing

**Standard Library**
- `base64`: Encoding for embedded assets
- `os`: File system operations
- `json`: Data storage and retrieval
- `datetime`: Timestamp management
- `smtplib`: Email sending functionality
- `email.mime`: Email message formatting

## External Services

**Email Service**
- SMTP Server: Gmail (smtp.gmail.com)
- Configuration: Requires environment variables or hardcoded credentials
- Fallback: Local JSON storage for messages

**Potential Integrations** (referenced in HTML/JS assets)
- EmailJS SDK: Client-side email service (alternative implementation)
- Box Icons: Icon library for UI elements
- Google Fonts: Poppins font family

## Static Assets

**Frontend Assets** (in `attached_assets/`)
- Custom CSS with dark theme variables
- JavaScript for navigation and scroll effects
- HTML template structure
- Theme customization with CSS variables (hue-based color scheme)

## Development Environment

**File Structure Requirements**
- `/data` directory for JSON storage and Python data modules
- `/utils` directory for utility functions
- `/attached_assets` for static frontend files
- Root level `app.py` as main entry point