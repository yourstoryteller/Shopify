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
- Amazon Web Services EC2 With Windows Server 2019 

## Data Flow
User navigates to Homepage, logins or signs-up. If it's a sale, few products will be discounted. User selects products and adds them to Cart. User navigates to Cart and after verification of Cart, checks-out. On successful Checkout, Invoice is downloaded and User is redirected to orders page. User has privilege of filling up Cart first and then logging in. While logging in, if user is Staff member (Admin/Staff), User is redirected to Admin Panel.

## User Roles
**1. Admin**
- Admin can view/add/update/delete Users, Products, Discounts.

**2. Staff**
- Staff can view/update Products and Discounts.

**3. Customer**
- Customer has no staff rights. Customer can only login/signup and buy products.

## Usage
Open your browser and hit http://15.206.226.180/ OR    
- Download and install Python 3.7 (Apache won't run on Python 3.8 and higher versions), PostgreSQL, Apache.
- Install and activate Virtual Environment (using pip).
- Install requirements.txt (using pip).
- Copy contents of httpd.conf.template and add to your Apache24/conf/httpd.conf.
- Modify variables of Apache24/conf/httpd.conf and save.
- Run Apache Server and hit http://localhost/ on your browser.
 

## References
- [E-commerce Django Project Tutorial] (https://www.youtube.com/watch?v=APESx65wpBc&list=PLdBwVRHjcI__NWxctXUSLz1Gg2Mb-B-O-)  
- [Django Pagination Tutorial] (https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)  
- [Downloading XHTML2PDF Generated PDF Tutorial] (https://stackoverflow.com/questions/60831569/django-xhtml2pdf-download-pdf-instead-open-in-browser)  
- [Hosting Django Website On Amazon EC2 Tutorial] (https://www.youtube.com/watch?v=OLS0XD6oINA)  
- [Connecting Apache To Django Tutorial] (https://www.youtube.com/watch?v=frEjX1DNSpc&t=642s)  





