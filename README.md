# Shopify
Simple E-commerce website created using Django.

## Technologies Used
**Front-end:**
- HTML 5
- CSS 3
- jQuery 3.5.1
- Bootstrap 4.5.2

**Back-end:**
- Django 3.1.5

**Database:**
- PostgreSQL 13

**Web Server:**
- Apache 2.4

**Cloud Platform:**
- Amazon Web Services Windows Server 2019 

## Data Flow
User navigates to Homepage, logins or signs-up. If it's a sale, few products will be discounted. User selects products and adds them to Cart. User navigates to Cart and after verification of Cart, checks-out. On successful Checkout, Invoice is downloaded and User is redirected to orders page. User has privilege of filling up Cart first and then logging in. While logging in, if user is Staff member (Admin/Staff), User is redirected to Admin Panel.

## User Roles
**1. Admin**
- Admin can view/add/update/delete Users, Products, Discounts.

**2. Staff**
- Staff can view/update Products and Discounts.

**3. Customer**
- Customer has no staff rights. Customer can only login/signup and buy products.

