# 🕊️ NeverForgotten - Digital Memorial Platform

## 📋 Table of Contents
1. [🌟 Project Overview](#project-overview)
2. [💼 Business Model](#business-model)
3. [🎨 UX Design](#ux-design)
4. [✨ Features](#features)
5. [🛠️ Technologies Used](#technologies-used)
6. [🗄️ Database Schema](#database-schema)
7. [🧪 Testing](#testing)
8. [🚀 Deployment](#deployment)
9. [🔍 SEO Implementation](#seo-implementation)
10. [📢 Marketing Strategy](#marketing-strategy)
11. [🙏 Credits](#credits)

---

## 🌟 Project Overview

NeverForgotten is a full-stack Django e-commerce application that serves as a digital sanctuary for preserving and honoring memories of loved ones. Born from personal experience with loss, this platform transforms traditional memorialization into a dynamic, interactive digital experience that helps users create lasting legacies.

### 💎 Value Proposition
- **For Users**: A beautiful, permanent digital space to celebrate lives and share memories
- **For Families**: Collaborative platform for multiple contributors to build memorials together  
- **For the Future**: Ensures stories and memories are preserved for generations to come

### 👥 Target Audience
- Individuals coping with loss and seeking meaningful ways to memorialize loved ones
- Families wanting to create shared memorial spaces accessible to relatives worldwide
- People planning their digital legacy as part of end-of-life preparations
- Those seeking affordable alternatives to traditional memorial services

---

## 💼 Business Model

NeverForgotten operates on a tiered subscription model with both recurring and one-time payment options, designed to make digital memorialization accessible while ensuring sustainable platform maintenance.

### 💰 Subscription Tiers

#### 🆓 **Free Tier** - $0/month
- Basic memorial page with essential features
- Gallery images
- QR code generation
- Biography section
- Portrait photo
- Tributes from friends and family
- Story sharing

#### 📅 **Monthly Plan** - $4.99/month
- Includes all Free Plan features
- 9 additional gallery images
- Memorial music player
- Custom banner customization
- Priority support

#### 📆 **Yearly Plan** - $49.99/year (Better Value)
- Includes all Monthly Plan features
- Annual billing with 17% savings compared to monthly
- Better value for long-term memorial preservation

#### ⭐ **Lifetime Plan** - $150.00 one-time (Most Popular)
- Includes all Yearly Plan features
- Permanent memorial preservation
- One-time payment for lifetime access
- Most popular choice for permanent legacies

---

## 🎨 UX Design

### 🎭 Design Philosophy

NeverForgotten was designed with empathy and sensitivity at its core, creating a comforting digital space for users during difficult times. The interface prioritizes simplicity, intuitive navigation, and emotional support.

### 🖥️ User Experience Approach

**Key Design Principles:**
- **Simplicity**: Clean, uncluttered interfaces that reduce cognitive load
- **Comfort**: Soothing color palettes and gentle interactions
- **Accessibility**: WCAG 2.1 compliant with high contrast and keyboard navigation
- **Responsiveness**: Mobile-first design that works seamlessly across all devices

![Responsive Design](docs/responsive.JPG)

### 📝 User Stories & Agile Development

![GitHub Issues Overview](docs/user_story.JPG)

The development followed Agile methodology with user stories organized into key epics:
- Memorial creation and management
- User authentication and profiles
- Subscription and payment processing
- Community features and sharing

### ✏️ Design Process

**Hand-Drawn Wireframes**
![Hand-Drawn Wireframes](docs/mockups.jpg)

I prefer the tactile nature of pencil and paper for initial design concepts, allowing for quick iteration and organic creativity before moving to digital tools. This approach helped capture the emotional flow and user journey in a more intuitive way.

### 🔬 Testing & Refinement

User feedback and continuous testing informed design improvements:
- Streamlined memorial creation process
- Enhanced mobile navigation
- Improved privacy controls
- Added contextual guidance for emotional tasks

The result is a platform that balances emotional sensitivity with robust functionality, providing users with a supportive environment for preserving precious memories.

---

## ✨ Features

### 🌐 Core Website Features

#### 🔍 **Browse Memorials**
- Public memorial gallery for discovering tributes
- Search functionality to find specific memorials
- Responsive grid layout for all devices

![Browse Memorials](docs/browse_memorials.JPG)

#### 🔐 **User Authentication**
- Secure registration and login system
- Profile management dashboard
- Password reset functionality

![Login Page](docs/login.JPG)

### 📖 Memorial Management

#### ➕ **Create Memorial**
- Step-by-step memorial creation wizard
- Photo upload and management
- Biography and story sections
- Privacy settings configuration

![Create Memorial](docs/create_memorial.JPG)


#### ✏️ **Edit Memorial**
- Real-time editing of memorial content
- Photo gallery management
- Memorial theme customization

![Edit Memorial](docs/edit_memorial.JPG)


### 💳 Subscription Plans

#### 🆓 **Free Plan** - $0/month
- Basic memorial page
- Gallery images
- QR code generation
- Biography section
- Tributes and stories

#### 📅 **Monthly Plan** - $4.99/month
- All Free features plus:
- 9 additional gallery images
- Memorial music player
- Custom banner changes
- Priority support

![Subscription Plans](docs/plans.JPG)


#### 📆 **Yearly Plan** - $49.99/year
- All Monthly features
- Better value (save 17%)
- Annual billing

#### ⭐ **Lifetime Plan** - $150.00 one-time
- All Yearly features
- Permanent memorial access
- One-time payment

### 🎁 Additional Features

#### 📱 **QR Code Integration**
- Unique QR codes for each memorial
- Printable versions
- Direct mobile access

![QR Code Example](docs/qr_code.JPG)

#### 📧 **Contact & Support**
- Direct communication with support team
- Categorized inquiry forms

![Contact Page](docs/contact_us.JPG)
---

## 🛠️ Technologies Used

### ⚙️ Backend Technologies
- **Django**: High-level Python web framework for rapid development
- **Python**: Primary programming language for backend logic
- **PostgreSQL**: Relational database for secure data storage

### 🎨 Frontend Technologies
- **HTML5**: Semantic markup structure
- **CSS3**: Custom styling and responsive design
- **JavaScript**: Interactive functionality and dynamic content
- **Bootstrap 5**: Responsive framework and UI components

### 🚀 Development & Deployment
- **Git & GitHub**: Version control and collaboration
- **Heroku**: Cloud platform for deployment
- **Stripe**: Payment processing integration
- **Cloudinary**: Image and media management service

### 🔧 Additional Tools
- **Font Awesome**: Icon library
- **Google Fonts**: Typography styling
- **Django Allauth**: Authentication system

---

## 🗄️ Database Schema

### 📊 Entity Relationship Diagram
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    User     │    │  Memorial   │    │    Plan     │
├─────────────┤    ├─────────────┤    ├─────────────┤
│ id (PK)     │    │ id (PK)     │    │ id (PK)     │
│ username    │    │ user_id (FK)│    │ name        │
│ email       │┼──┼│ plan_id (FK)│┼──┼│ price       │
│ date_joined │    │ first_name  │    │billing_cycle│
└─────────────┘    │ last_name   │    │feature_flags│
                   │ dates       │    └─────────────┘
                   │ biography   │
                   └─────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
┌────────┴───────┐ ┌─────┴────────┐ ┌────┴─────────┐
│   Tribute      │ │ GalleryImage │ │    Story     │
├────────────────┤ ├──────────────┤ ├──────────────┤
│ id (PK)        │ │ id (PK)      │ │ id (PK)      │
│ memorial_id(FK)│ │ memorial_id  │ │ memorial_id  │
│ author_name    │ │ image        │ │ title        │
│ message        │ │ caption      │ │ content      │
│ created_at     │ │ order        │ │ author_name  │
└────────────────┘ └──────────────┘ │ created_at   │
                                    └──────────────┘

┌─────────────┐
│ Subscriber  │
├─────────────┤
│ id (PK)     │
│ email       │
│ first_name  │
│ subscribed  │
│ created_at  │
└─────────────┘
```

### 📦 Models Overview

| Model         | Purpose                           | Key Fields                                      |
|---------------|-----------------------------------|-------------------------------------------------|
| Memorial      | Core memorial profiles            | first_name, last_name, biography, dates         |
| Plan          | Subscription tiers                | name, price, billing_cycle, feature_flags       |
| Tribute       | User condolences                  | author_name, message, created_at                |
| GalleryImage  | Photo gallery                     | image, caption, order                           |
| Story         | Detailed narratives               | title, content, author_name                     |
| Subscriber    | Newsletter management             | email, first_name, subscribed                   |

### 🔗 Key Relationships
- **One User** → **Many Memorials**
- **One Memorial** → **One Plan** (subscription)
- **One Memorial** → **Many Tributes**
- **One Memorial** → **Many GalleryImages**
- **One Memorial** → **Many Stories**

---

## 🧪 Testing

### 🎯 Comprehensive Testing Strategy

NeverForgotten underwent rigorous testing to ensure a robust, user-friendly experience across all features and platforms.

### 🖱️ Manual Testing

#### ⚙️ Core Functionality Testing
- **User Authentication**: Registration, login, logout, and password reset flows
- **Memorial Creation**: Complete memorial setup process with all field types
- **Subscription System**: Plan selection, Stripe payments, and feature access
- **Content Management**: Adding tributes, stories, and gallery images
- **Responsive Design**: Mobile, tablet, and desktop viewport testing

#### 🌐 Browser Compatibility
- **Chrome** (v115+): All features functional ✅
- **Firefox** (v115+): All features functional ✅  
- **Safari** (v15+): All features functional ✅

### 🤖 Automated Testing

#### 🐍 Django Unit Tests
- Memorial model creation and validation tests
- Subscription feature access control tests
- QR code generation and storage tests
- User authentication and authorization tests

### 🐛 Bug Resolution

#### ⚠️ Deployment Issue: Database Migration to Heroku
**Problem**: Initial deployment failed due to PostgreSQL migration conflicts between development and production environments.

**Solution**: 
- Implemented Django migration conflict detection
- Used Heroku migration planning to preview steps
- Created safe data migration files for schema changes
- Established consistent deployment workflow: local → staging → production

#### 💳 Payment Issue: Stripe Webhook Handling
**Problem**: Webhook events were not consistently processing subscription updates, causing sync issues between Stripe and the application database.

**Solution**:
- Added comprehensive debugging throughout webhook views
- Implemented webhook signature verification for security
- Created duplicate event handling prevention
- Added retry logic for failed webhook deliveries

![Webhook Debugging](docs/stripe_webhooks.JPG)


### ✔️ Validation Results

#### 📝 HTML Validation
- **W3C Validator**: All pages pass with no errors ✅
- **Semantic HTML**: Proper heading hierarchy and landmark elements ✅
- **Accessibility**: ARIA labels and alt text implemented throughout ✅

#### 🎨 CSS Validation
- **W3C Jigsaw**: All custom CSS passes validation ✅
- **Bootstrap Integration**: No conflicts with framework styles ✅

#### 💻 JavaScript Validation
- **ESLint**: Code follows consistent style guidelines ✅
- **Functionality**: All interactive features work as intended ✅

#### 🐍 Python Code Quality
- **PEP 8 Compliance**: Code follows Python style guide ✅
- **Django Best Practices**: Proper project structure and app organization ✅

#### 🔒 Security Testing
- **Authentication**: Secure session management and password hashing
- **Data Protection**: Environment variables for all sensitive information
- **Payment Security**: PCI compliant through Stripe integration

### 👤 User Acceptance Testing

#### ✨ Test Scenarios Completed
- Memorial creation and editing workflow
- Subscription upgrade and downgrade processes
- Content sharing and privacy settings
- Mobile responsiveness across devices
- Error handling and user feedback

All critical user journeys have been validated to ensure a seamless experience for users during emotionally sensitive interactions with the platform.

---

## 🚀 Deployment

### 💻 Local Development Setup

#### 📦 What You Need
- Python 3.8 or higher
- PostgreSQL installed
- A code editor (VS Code recommended)

### ⚡ Quick Start (5 Steps)

#### 1️⃣ **Step 1: Get the Code**
```bash
git clone https://github.com/yourusername/neverforgotten.git
cd neverforgotten
```

#### 2️⃣ **Step 2: Setup Python Environment**
```bash
python -m venv venv
source venv/bin/activate
```
**Windows users:** Use `venv\Scripts\activate` instead

#### 3️⃣ **Step 3: Install Everything**
```bash
pip install -r requirements.txt
```

#### 4️⃣ **Step 4: Create Environment File**
Create a file named `.env` in your project folder and copy this (update the values):
```text
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://username:password@localhost/neverforgotten
STRIPE_PUBLIC_KEY=pk_test_your_key
STRIPE_SECRET_KEY=sk_test_your_key
STRIPE_WH_SECRET=whsec_your_webhook_secret
CLOUDINARY_URL=cloudinary://your_cloudinary_url
DEBUG=True
```

**🔑 Where to find these:**
- **SECRET_KEY**: Generate at [Djecrety.ir](https://djecrety.ir/)
- **Stripe Keys**: [Stripe Dashboard](https://dashboard.stripe.com/test/apikeys)
- **Cloudinary URL**: [Cloudinary Console](https://cloudinary.com/console)

#### 5️⃣ **Step 5: Setup Database & Run**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**✅ Done!** Open http://localhost:8000 in your browser 🎉

---

### ☁️ Heroku Production Deployment

#### 🚀 Quick Setup (3 Steps)

##### 1️⃣ **Step 1: Create Heroku App**
1. Go to [Heroku Dashboard](https://dashboard.heroku.com)
2. Click "New" → "Create new app"
3. Enter app name (e.g., `neverforgotten-app`)
4. Choose your region
5. Click "Create app"

##### 2️⃣ **Step 2: Connect GitHub & Add Database**
1. In your app dashboard, go to "Deploy" tab
2. Select "GitHub" as deployment method
3. Connect your GitHub account and select your repository
4. Go to "Resources" tab
5. Search for "Heroku Postgres" and add the "Hobby Dev" plan (free)

##### 3️⃣ **Step 3: Configure Environment Variables**
1. Go to "Settings" tab → "Config Vars" → "Reveal Config Vars"
2. Add each variable (click "Add" after each):

| Key                   | Value                        |
|-----------------------|------------------------------|
| `SECRET_KEY`          | Your Django secret key       |
| `STRIPE_PUBLIC_KEY`   | From Stripe Dashboard        |
| `STRIPE_SECRET_KEY`   | From Stripe Dashboard        |
| `STRIPE_WH_SECRET`    | From Stripe Webhook settings |
| `CLOUDINARY_URL`      | From Cloudinary Dashboard    |
| `DEBUG`               | `False`                      |
| `DISABLE_COLLECTSTATIC`|`0`                        |

**📝 Note:** `DATABASE_URL` is automatically created when you add Postgres.

##### 4️⃣ **Step 4: Deploy & Setup Database**
1. Go back to "Deploy" tab
2. Scroll to "Manual deploy" section
3. Click "Deploy Branch"
4. Once deployed, click "More" → "Run console"
5. Run these commands one at a time:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Click "Open app" to view your live site!

### 📁 Required Files

#### Procfile
```text
web: gunicorn neverforgotten.wsgi:application
```

#### requirements.txt
```text
Django>=4.2.0
gunicorn
whitenoise
psycopg2-binary
dj-database-url
django-allauth
stripe
django-cloudinary-storage
cloudinary
```

---

### ✅ Post-Deployment Verification

#### 1️⃣ **Live Site Testing**
- Memorial creation workflow
- Stripe payment processing
- User authentication flows
- Responsive design checks

#### 2️⃣ **Environment Checks**
```bash
heroku run python manage.py check --deploy
```

#### 3️⃣ **Security Verification**
- DEBUG mode set to False
- All secret keys properly hidden
- HTTPS enforcement active
- CSRF protection enabled

---

### 🔧 Troubleshooting Common Issues

#### 🗄️ Database Connection Issues
- Verify DATABASE_URL format
- Check PostgreSQL add-on status
- Run `heroku pg:info` to verify database

#### 🎨 Static Files Not Loading
- Ensure DISABLE_COLLECTSTATIC=0
- Verify WhiteNoise middleware in settings
- Check Cloudinary configuration

#### 💳 Stripe Webhook Failures
- Verify webhook endpoint in Stripe Dashboard
- Check STRIPE_WH_SECRET matches webhook secret
- Monitor Heroku logs for webhook events

---

**🌐 The application is successfully deployed and fully functional at: [Your Live Heroku URL]**

---

## 🔍 SEO Implementation

NeverForgotten implements comprehensive SEO strategies to ensure the platform is easily discoverable by those seeking memorialization services.

### 🔧 Technical SEO

**📌 Meta Tags & Structured Data**
```html
<!-- Primary Meta Tags -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NeverForgotten - Create a Memorial Page for Loved Ones</title>
<meta name="description" content="NeverForgotten helps you honor loved ones by creating beautiful online memorial pages. Share memories, photos, music, and tributes in one place.">
<meta name="keywords" content="online memorial, tribute, obituary, remember loved ones, create memorial page, digital legacy">
<meta name="author" content="NeverForgotten Team">
<meta name="robots" content="index, follow">

<!-- Canonical URL -->
<link rel="canonical" href="{{ request.build_absolute_uri }}">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:title" content="NeverForgotten - Create a Memorial Page for Loved Ones">
<meta property="og:description" content="Easily create and share memorial pages to remember loved ones. Add stories, photos, music, and tributes.">
<meta property="og:url" content="{{ request.build_absolute_uri }}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="NeverForgotten - Create a Memorial Page">
<meta name="twitter:description" content="Create beautiful memorial pages to honor and remember loved ones. Share memories, photos, and tributes in one place.">

<!-- Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "NeverForgotten",
  "url": "{{ request.build_absolute_uri|slice:':-1' }}",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "{{ request.build_absolute_uri }}search/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>
```

---

## 📢 Marketing Strategy

NeverForgotten employs a compassionate, community-focused marketing approach that respects the sensitive nature of our services while effectively reaching those who need our platform.

### 📱 Facebook Marketing

#### 👥 **Facebook Business Page**
![Facebook Business Page Overview](docs/facebook_page.JPG)

**🎯 Page Structure & Branding**
- **Cover Photo**: Elegant, comforting imagery that reflects the memorial theme
- **Profile Picture**: NeverForgotten logo with transparent background
- **About Section**: Complete business information with contact details and website link
- **Call-to-Action Button**: "Create Memorial" linking directly to registration page

#### 📝 **Content Strategy**

**📅 Weekly Posting Schedule:**
- **Monday**: Inspirational quotes about remembrance and legacy
- **Wednesday**: Educational content about digital memorial benefits
- **Friday**: User stories and memorial highlights (with permission)
- **Sunday**: Community support and grief resources

#### 💬 **Engagement & Community Building**

**🤝 Community Management:**
- Respond to all comments and messages within 24 hours
- Host monthly Q&A sessions about digital memorialization
- Create private support groups for users to connect
- Share user-generated content (with explicit permission)

#### 🎯 **Facebook Advertising**

**🎯 Targeted Ad Campaigns:**
- **Demographic Targeting**: Adults 25+, all genders
- **Interest-Based**: Funeral services, grief support, legacy planning
- **Lookalike Audiences**: Based on current user profiles
- **Custom Audiences**: Website visitors and email subscribers

**📢 Ad Content Types:**
- Carousel ads showcasing different memorial features
- Video testimonials from satisfied users
- Educational content about digital legacy planning
- Seasonal campaigns (memorial days, holidays)

---

### 📧 Email Marketing & Newsletter

#### ✉️ **Newsletter Signup Implementation**
![Newsletter Signup Form](docs/newsletter.JPG)


**🎁 Lead Magnet Strategy:**
- Free "Creating Meaningful Memorials" guide
- Monthly memorial inspiration emails
- Platform updates and feature announcements
- Seasonal remembrance ideas

#### 📰 **Blog & Resource Center**
- SEO-optimized articles about grief support and memorial planning
- How-to guides for creating beautiful digital memorials
- Interviews with grief counselors and legacy experts
- Seasonal content aligned with remembrance days and holidays

This multi-channel approach ensures NeverForgotten reaches users through compassionate, relevant channels while building a supportive community around digital memorialization.

---

## 🙏 Credits

### 💻 Code & Resources
- **Django**: Web framework and documentation
- **Bootstrap 5**: Frontend components and responsive design
- **Stripe**: Payment processing integration
- **Cloudinary**: Image and media storage
- **Font Awesome**: Icons used throughout the site

### 📝 Content
- All text content and memorial templates created specifically for NeverForgotten
- Custom CSS and JavaScript written for the project
- Django models and views developed from scratch

### ✨ Special Thanks
- Code Institute for project guidance and learning materials

### ⚠️ Disclaimer
This project was developed for educational purposes as part of Code Institute's Full Stack Software Development program. All core functionality was implemented independently.

---

<div align="center">

**🕊️ Built with ❤️ for preserving precious memories**

</div>