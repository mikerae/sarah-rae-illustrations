![Am I Responsive](/readme_files/am-i-responsive.png)
# Sarah Rae Illustrations
An E-Commerce Site which facilitates the sale of Art Work products created by by Sarah Rae.
The site promotes the digital art work of Sarah Rae.

[View the site here](https://sarah-rae-illustrations-d721ea03fb61.herokuapp.com/)

### Code Institue Accreditation
This is fifth project contribution to the Code Institute Full Stack Diploma. It is inspired by and is closely modelled on the Code Institute E-Commerce Walkthrough project 'Boutique Ado'.
Appropriate accreditation is hereby given for any similarities between this project and the Code Institute E-Commerce Walkthrough project 'Boutique Ado'.
## Buisness Model: Buisness to Customer
This site presents the Artwork of Sarah Rae and facilitate the sale of this artwork though an e-commerce website.
## Artwork Purchase
### In the Minimum Viable Product (MVP), Customers will be able to:
- Purchase selected artwork products using Stripe as an industry standard purchasing method.
- Create a customer account to facilitate purchases and view order history
- View different categories of available artwork products
- View artwork product detail, with descriptions of the product.
- View digital art work in a gallery
- View details of a particular digital artwork
- Sign up to a Newsletter
- Access Sarah Rae’s  Social Media sites 
#### In Future versions, Customers will be able to:
- Be updated on the progress of their order, from placement to delivery.
- Indicate ‘liked’ artworks
- Commission bespoke artwork

### In the MVP, Sarah Rae will be able to:
- Sell her artworks to customers through the e-commerce site
- Promote her internet presence
- Develop a community of people interested her work through the circulation of a Newsletter
#### In Future versions, Sarah Rae will be able to:
- Negotiate commissioned art work.
- Analyse and manage her stock levels .
- Track Order progress from placement to delivery.
- Keep Customers informed of the progress of their orders.
## Commissioned Artwork
Commissions are not implemented in the MVP. A commissions business model will describe the services offered, the consultation process, the pricing structure and any terms and conditions.
#### In Future versions, Customers will be able to:
- Initiate dialogue with Sarah Rae regarding the commissioning of bespoke Artwork
#### In Future versions, Sarah Rae will be able to:
- Conduct dialogue with prospective commissioners with a view to developing a commissioned Artwork Service.

# User Experience Design (UXD)
[Back to Top](#sarah-rae-illustrations)
## Strategy
### User Stories
User Stories were generated through discussion with Sarah Rae, and were used to inform the strategy the UXD.
User Stories summarising project objectives may be viewed here:
- [User Stories 1](/readme_files/user_stories/user_stories_1.png)
- [User Stories 2](/readme_files/user_stories/user_stories_2.png)
- [User Stories 3](/readme_files/user_stories/user_stories_3.png)
- [User Stories 4](/readme_files/user_stories/user_stories_4.png)

## Scope
### Minimum Viable Product (MVP)
[The following features were included in the MVP and can be viewed in the MVP Sprint here:](https://github.com/users/mikerae/projects/12/views/6?visibleFields=%5B%22Title%22%2C%22Labels%22%2C%22Milestone%22%2C%22Status%22%5D&filterQuery=milestone%3AMVP&sliceBy%5BcolumnId%5D=Status&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Status&sliceBy%5Bvalue%5D=%E2%9C%85+Done)
#### Admin and Store Management
- Products and Digital Artworks can be added by the site owner
- Products and Digital Art Works can be edited by the site owner
- Products and Digital Art Works can be deleted by the site owner
#### Digital Art Works
- Digital Art Works selected by the Site Owner are displayed in a carousel on the landing page
- Digital Art works are displayed in the Gallery area of the site
#### Purchasing and Checkout
- Shoppers may add products to be purchased to their basket
- Shoppers may view basket items
- Shoppers may view a summary of basket items
- Shoppers may select and edit the quantity of products they wish to purchase
- Shoppers may remove items from their basket before checkout
- Shoppers will receive a confirmation email of purchases, summarising their order and also containing site contact details
- Shoppers may securely submit payment details to Stripe for purchase processing
- Shoppers are given feedback on the site for a successfully (or otherwise) processed purchase
#### Registration and User Accounts
The Django Security package 'Allauth' was used to manage account security and registration.
- Users may register with the site
- Users may log in and out of the the site
- Users may recover lost passwords
- Users are sent a confirmation of registration by email
#### Security and Site Access
- User role is authenticated using username, email and password.
- Passwords are encrypted in all areas of the site and cannot be read directly
- Passwords may be changes by the registered user and the super-user.
- Access to areas and features of the site is restricted by role as follows:
    - Anonymous users may view the Shop and Gallery and make purchases
    - Registered Shoppers may have their shipping details saved and have them populate future purchases for convenience
    - Registered Shoppers may save and view their order history
    - Registered Shoppers may view their profile
    - Registered Shoppers may sign up for and be sent a Newsletter
    - The Site Owner may add, edit and delete products and digital art works
    - The Site Owner, as super-user, my access and manage the Admin section of the site 
#### Sorting and Searching of Products
- The site user may view a list of products sorted by category
- The site user may search products by category
- The site user may search the shop using key words in the search bar
- The site user is shown a summary of their search results
- The site user may sort the list of products by name, price and category (Ascending and descending).
#### Viewing and Navigation
- A carousel of digital art works is displayed the site landing page
- Digital artworks are viewable in the Gallery
- Digital Artworks are stored securely on the site database
- Details of a particular digital artwork can be viewed when that item is clicked
- Products are viewed in the shop
- Details regarding a particular product are viewed by clicking on the item
- Different versions of a particular product are viewable for purchase
- A digital artwork my be zoomed in for detailed inspection
- Social media links for the site owner are available in the footer of each page and open in a new window
- The site user may easily navigate the site using the nav-bar at the top of each page
- The site user is given feedback for every interaction with the site.

### Features: Future Development
[Back to Top](#sarah-rae-illustrations)
- Commissions: A customer may enter into discussion with the site owner regarding the commissioning of art work
- Order Processing and Delivery: Order status tracking and delivery tracking will be provided to the customer and the site owner.
- Stock Management: Stock management will be provided to the site owner.
- Customer Product Interest: Customers may express interest in products when they are out of stock
## Structure
[Back to Top](#sarah-rae-illustrations)
The access to areas and features within the site is dependant on the user role.
The following Site Maps show the differences:
- [Anonymous User](/readme_files/site-maps/site-map-anonymous-user.png)
- [Registered Shopper](/readme_files/site-maps/site-map-registered-shopper.png)
- [Site Owner](/readme_files/site-maps/site-map-site-owner.png)
## Skeleton
[Back to Top](#sarah-rae-illustrations)

Wire frames modelling the Skeleton phase of UXD were constructed in Balsamiq
### Mobile Wire Frames
![Index m](/readme_files/wire_frames/mobile/index-m.png)
- [Index Hamburger m](/readme_files/wire_frames/mobile/index-hamburger-m.png)
- [Index Hamburger Expanded m](/readme_files/wire_frames/mobile/index-m-hamburger-expanded.png)
- [Index Search 1 m](/readme_files/wire_frames/mobile/index-m-search-1.png)
- [Index Search 2 m](/readme_files/wire_frames/mobile/index-m-search-2.png)
- [Index My Account m](/readme_files/wire_frames/mobile/index-m-my-account.png)
![Sign Up m](/readme_files/wire_frames/mobile/index-m-my-account-signup.png)
- [Sign In m](/readme_files/wire_frames/mobile/index-m-my-account-login.png)
- [Products m](/readme_files/wire_frames/mobile/products-m.png)
- [Category Selection m](/readme_files/wire_frames/mobile/category-selection-m.png)
- [Products Sort m](/readme_files/wire_frames/mobile/products-sort-m.png)
- [Products Detail m](/readme_files/wire_frames/mobile/product-detail-m.png)
- [Product or Art Work new Window .](/readme_files/wire_frames/mobile/product-or-art-work-image-new-window-m.png)
- [Add to Bag Success! m](/readme_files/wire_frames/mobile/add-to-bag-success!-m.png)
- [Shopping Bag Empty m](/readme_files/wire_frames/mobile/shopping-bag-empty-m.png)
- [Shopping bar Items m](/readme_files/wire_frames/mobile/shopping-bag-items-m.png)
- [Checkout 1 m](/readme_files/wire_frames/mobile/checkout-1-m.png)
- [Checkout 2 m](/readme_files/wire_frames/mobile/checkout-2-m.png)
- [Gallery m](/readme_files/wire_frames/mobile/gallery-m.png) 
- [About Sarah-m](/readme_files/wire_frames/mobile/about-sarah-m.png)
- [Commissions m](/readme_files/wire_frames/mobile/commissions-m.png)
![My Account Menu m](/readme_files/wire_frames/mobile/index-my-account-m.png)
- [Product Management m](/readme_files/wire_frames/mobile/product-management-m.png)
- [Gallery Management m](/readme_files/wire_frames/mobile/gallery-management-m.png)
### Tablet
![Index t](/readme_files/wire_frames/tablet/index-t.png)
- [Index Hamburger t](/readme_files/wire_frames/tablet/index-hamburger-t.png)
- [Index Hamburger Expanded t](/readme_files/wire_frames/tablet/index-t-hamburger-expanded.png)
- [Index Search 1 t](/readme_files/wire_frames/tablet/index-t-search-1.png)
- [Index Search 2 t](/readme_files/wire_frames/tablet/index-t-search-2.png)
- [Index My Account t](/readme_files/wire_frames/tablet/index-my-account-t.png)
![Sign Up t](/readme_files/wire_frames/tablet/index-t-my-account-signup.png)
- [Sign In t](/readme_files/wire_frames/tablet/index-t-my-account-login.png)
- [Products t](/readme_files/wire_frames/tablet/products-t.png)
- [Category Selection t](/readme_files/wire_frames/tablet/category-selection-t.png)
- [Sort t](/readme_files/wire_frames/tablet/shop-now-sort-t.png)
- [Product Detail t](/readme_files/wire_frames/tablet/product-detail-t.png)
- [Product or Artwork New Window t](/readme_files/wire_frames/tablet/product-or-artwork-image-new-window-t.png)
- [Add to Bag Success t](/readme_files/wire_frames/tablet/add-to-bag-success!-t.png)
- [Shopping Bag Empty t](/readme_files/wire_frames/tablet/shopping-bag-empty-t.png)
- [Shopping Bag Items t](/readme_files/wire_frames/tablet/shopping-bag-items-t.png)
- [Checkout 1 t](/readme_files/wire_frames/tablet/checkout-1-t.png)
- [Checkout 2 t](/readme_files/wire_frames/tablet/checkout-2-t.png)
- [Gallery t](/readme_files/wire_frames/tablet/gallery-t.png)
- [Commissions t](/readme_files/wire_frames/tablet/commissions-t.png)
- [About Sarah t](/readme_files/wire_frames/tablet/about-sarah-t.png)
- [My Account Menu t](/readme_files/wire_frames/tablet/index-t-my-account.png)
- [Product Management t](/readme_files/wire_frames/tablet/product-management-t.png)
- [Gallery Management t](/readme_files/wire_frames/tablet/gallery-management-t.png)
### Desktop
![Index d](/readme_files/wire_frames/desktop/index-d.png)
![Shop Landing d](/readme_files/wire_frames/desktop/shop-landing-d.png)
- [Shop Landing Menus d](/readme_files/wire_frames/desktop/shop-landing-menus-d.png)
- [Shop Category Selection d](/readme_files/wire_frames/desktop/shop-category-selection-example-d.png)
- [Product Detail d](/readme_files/wire_frames/desktop/product-detail-d.png)
- [Add to Bag Success! d](/readme_files/wire_frames/desktop/add-to-bag-success!-d.png)
- [Shopping Bag Empty d](/readme_files/wire_frames/desktop/shopping-bag-empty-d.png)
- [Shopping Bag Items d](/readme_files/wire_frames/desktop/shopping-bag-items-d.png)
- [Checkout d](/readme_files/wire_frames/desktop/checkout-d.png)
- [Gallery d](/readme_files/wire_frames/desktop/gallery-landing-d.png)
- [Product-ArtWork New Window d](/readme_files/wire_frames/desktop/product-or-art-work-image-new-window-d.png)
- [Commissions d](/readme_files/wire_frames/desktop/commissions-landing-d.png)
- [About Sarah d](/readme_files/wire_frames/desktop/about-sarah-landing-d.png)
- [My Account Menu](/readme_files/wire_frames/desktop/index-my-account-d.png)
- [Sign Up d](/readme_files/wire_frames/desktop/signup-d.png)
- [Sign In d](/readme_files/wire_frames/desktop/sign-in-d.png)
- [Product Management d](/readme_files/wire_frames/desktop/product-management-d.png)
- [Gallery Management d](/readme_files/wire_frames/desktop/gallery-management-d.png)
## Surface
[Back to Top](#sarah-rae-illustrations)
The colours, font style, logo and background image were derived from a mockup of the landing page for mobile made by Sarah Rae. The mockup can be viewed [here](/readme_files/surface-mockup.jpeg)

# Agile Development
[Back to Top](#sarah-rae-illustrations)

Agile development practices were used throughtout the development of this project.
## Platform
[Back to Top](#sarah-rae-illustrations)

The GitHub platform was used to facilitate Agile Development:
## User Stories - Github Issues
[Back to Top](#sarah-rae-illustrations)

- User stories were derived from discussions with Sarah Rae and notated as Github [issues](https://github.com/search?q=repo%3Amikerae%2Fsarah-rae-illustrations+USER+STORY&type=issues&p=1) These user stories were refined from 'epic' to more specific user-stories.
- For some user stories, Predicted Project Effort was defined, with story points being allocated to some user stories. 
- Issues were prioritised according to Moscow principles. Github Labels were used mark user stories accordingly.
    - Must have: < 60% of total story points in iteration
    - Should have: the rest
    - Could have: 20% of total story points in iteration
    - Won't have
### Bugs
Bugs were recorded as [issues](https://github.com/mikerae/sarah-rae-illustrations/issues?q=+is%3Aissue+label%3Abug+), and the progress towards resolution of these issues was tracked.
### Tests
Some Tests were recorded as [issues](https://github.com/mikerae/sarah-rae-illustrations/issues?q=+is%3Aissue+label%3ATest+), and their results were tracked.
## Information Radiators
[Back to Top](#sarah-rae-illustrations)

Information Radiators were used to monitor the progress of the project development.
- A Github [Project](https://github.com/users/mikerae/projects/12)  was used to hold all user stories for processing and allocation in a Kanban Board. User stories were allocated to the Project and their progress tracked through the following stages:
    - New Issue
    - Backlog
    - Ready
    - In Progress
    - In Review (Used when a branch pull-request was made)
    - Done
- Github [Milestones](https://github.com/mikerae/sarah-rae-illustrations/milestones) were used to define sprint content.
## Backlog
[Back to Top](#sarah-rae-illustrations)

The GitHub [Project Backlog](https://github.com/users/mikerae/projects/12) was used to hold user stories and other issues which were not allocated to the current sprint.
## Sprints - Github Milestones
[Back to Top](#sarah-rae-illustrations)

- [Sprints](https://github.com/mikerae/sarah-rae-illustrations/issues?q=is%3Aopen+is%3Aissue+milestone%3AMVP) were defined using Github milestones to define development tasks needed to bring the project to Minimum Viable Product level. Other Github Milestones were used to hold user stories allocated to these sprints.

Initially Milestones were used to group related issues for development. Later the following 2 sprints were used:
- MVP (Issues for the project submission)
- Resubmission (Issues arising from the projects assessment and initial failure)
# Database Design
[Back to Top](#sarah-rae-illustrations)
## Mission Statement
The purpose of the Sarah-Rae-Illustrations database is to hold data relating to the the sale of Products and display of Digital Art Works, by Sarah Rae.
## Models
[Back to Top](#sarah-rae-illustrations)
### The following models were used in the MVP:
- Product
- Category
- Orders
- OrderLineItem
- UserProfile
- DigitalArtWork
#### Models planned for future versions include:
- Stock
- ProcessingStatus
## Model Entity Relationship Diagram (EDR)
The entities for this project have the following relationships and attributes:
- [View Entity Relationship Diagram](/readme_files/erd/erd.png)
## Model Schemas
The Models Schemas for this project are:
- [View Schema](/readme_files/erd/schema.png)
#### Model Creation
The models were created from least dependant to most dependant.
## Data Input
[Back to Top](#sarah-rae-illustrations)
### Initial data input
Example products and digital art works, with associated data were created for the purpose of development.
### Subsequent data input
For Production, the Site Owner, Sarah Rae will load her own product images, and digital artworks with associated data.
# Technologies Used
[Back to Top](#sarah-rae-illustrations)
## Languages
- Python
- HTML5
- CSS
- Javascript
## Libraries
- Bootstrap 4
- JQuerry
## Framework
- Django
# Development
[Back to Top](#sarah-rae-illustrations)
## Remote Repository: GitHub
The project code was stored remotely in a Github repository.
### Code Institute template
- A gitHub repository was created using a Code Institute template. This would ensure that all initial code eg Python3 was made available in the GitPod workspace.
### Issues
Issues were used to identify and track the development and implementation of discrete elements of the project.
#### Issue Templates
Issue templates were created to facilitate the creation of project issues.
Templates for the following types of project issue were used:
- User Stories
- Bugs
- Tests
#### Issue Labels
Issues were allocated labels. These were useful to easily identify:
- The priority of an issues within a sprint (MOSCOW)
- The category of user story and is sequence in the development process.
- The type of user to which the issue related
### Milestones (Sprints)
Milestones were created to mark stages in development. The main ones which were eventually used were:
- MVP (initial project submission)
- Resubmission (of project after initial failure)
### Project (Kanban board)
A github project was created as an Information Radiator and project management tool.
The sections of the project were:
- New
- Backlog
- Ready
- In Progress
- In Review
- Done
As issues were created, they were added to the New section.
They were then moved to the Backlog section for storage and processing.
Epic issues were broken down into as many smaller issues as was appropriate.

For each issue the following were defined:
- Acceptance Criteria: Identifiable outcomes upon which the Site owner and developer could agree were evident
- Tasks needs to make effective the resolution of the issue.

Once an issue was prepared it was moved the the 'Ready' section of the Project board.

One or two issues were moved to the 'In Progress' section of the board whilst they were developed.

Once an issue was completed, it was closed and moved to the 'Done' section of the board.
The process of closing and moving issues was automated when a branch addressing these issues was merged with the main branch.

## Local Development: GitPod Workspace
[Back to Top](#sarah-rae-illustrations)
Code was developed locally in a browser using a GitPod Workspace.
The template used to create the GitHu repository ensured that all the necessary software was preloaded in the GitPod workspace to facility the start of development.
A browser based version of VS Code was used with this workspace to write the code.
## Git Version Control
[Back to Top](#sarah-rae-illustrations)

Version control was effected using Git.
### Commits
Incremental snapshots were taken as git commits to recored the stages of project development.
### Code Pushes
Once a commit was made locally, the committed code and the commit description was 'pushed' to the github repository. In this way, an exact copy of each of the commits (code snapshots) existed both on the local computer (via the browser to the  Gitpod workspace) and in the github repository.
### Issue Tracking
Issues created in GitHub were linked to commits to facilitate the tracking of the progress of a particular user story, bug-fix or other issue. This tracking proved a powerful tool in managing and monitoring the development of the project.
### Branches
Latterly, new branches were created away from the main branch. A particular branch was used to address a unique issue or collection of related issues. Code developed in these branches was separate from code in the main branch.
### Pull Requests
Once code in a branch had been sufficiently developed to resolve the issues assigned to it, a pull-request was made. This began the process of merging the branch being developed into the main (deployed) branch.
### Branch Merges
For the purpose of this project the creation and merging of branches was unnecessary. Branch creation and merging was used later on in the project for practice purposes.
Once a pull-request was made, and tests, discussions and reviews had been conducted, and the pull-request approved, the branch was then merged with the main branch. All discrete commits were retained so that a record for the the development progress could be shown.
Upon successful
## Stages of Development of MVP
Development closely matched the Code Institute walkthrough eCommerce project 'Boutique Ado' with appropriate adjustments and changes being made to match the requirements of this project.
The following stages of development were used as initial Github Milestones, matching the Boutique Ado Walkthrough chapter headings:
### Set Up
Issues associated with set up can be viewed [here](https://github.com/mikerae/sarah-rae-illustrations/issues?q=is%3Aissue+is%3Aclosed+label%3APrep)
#### Setting Up Local Gitpod Workspace Development Environment
[Back to Top](#sarah-rae-illustrations)

The gitpod environment was updated with additional requirements as and when they were needed in development. They were  downloaded them into the environment via the terminal, and the requirements.txt file was updated to recored their addition to the using the following code:
```
pip3 freeze  --local > requirements.txt
```
The requirements.txt file was used by Heruko to build each successive deployment of the project with the correct code dependancies.
#### Libraries
The current requirements used can be viewed [here](https://github.com/mikerae/sarah-rae-illustrations/blob/main/requirements.txt)
#### Creating a Django Project
A Django project was created:

```$ python3 django-admin startproject <project-name>```

A Local sql database was automatically created
#### Creating a project superuser
A superuser was created to access the django admin section of the site.
```$ python3 manage.py createsuperuser```
A username , email and password were provided, and this username was added to the django user model inside the project.
#### Creating Apps
Apps were created as required using:

``` $ python3 manage.py startapp <app name>```

The  app was added to the list of installed apps in the settings.py file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app-name',
]
```
#### Database Migrations
As models were created and changed, the changes were recorded in a set of sequential django records called 'migrations' and then applied to the database models either locally or remotely.
##### Make Migrations
The changes to the Django database were recorded by making migration records. First, a dry run was used to expose any errors in creating the records:

```$ python3 manage.py makemigrations -- dry-run ```
Once all issues were resolved, migrations were actually made using:

```$ python3 manage.py makemigrations```
##### Migrate
Changes to the database were made by applying the migrations.
The following command was used to simulate the application of migrations without actually making any changes. This identified any errors which might arise.
```$ python3 manage.py migrate --plan```
Once any issues were resolved, migrations were applied to the database using:
```$ python3 manage.py migrate```
### Registration & User Accounts
The Allauth library and django.contrib.auth api were used to register user accounts in the django User model.
When a user registers with the site, allauth requests a username, email and password. A request for verification is sent to the user's email, and upon confirmation , the user is registered. The password is accessible for a user is encrypted and not accessible anywhere in the font or back end. A passwords may be changed by the user or the superuser.

Roles may be defined in the administration section of the site, accessible by the superuser, and control access to certain parts of the site.

The login screen may be viewed [here](/readme_files/login.png).

Issues relating to Registration & User Accounts may be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3AMVP+label%3A%22Registration+and+User+Accounts%22)

### The Base Template
A [base template](/templates/base.html) was used to provide consistent content throughout the site.
The base template contains the header, navigation, content blocks and footer.
[Includes](/templates/includes/) were used where an area of the site needed variations to the base template eg.
- Navigation for the [Shop](/readme_files/includes-shop.png) and [Gallery](/readme_files/includes-gallery.png).
- The responsive display for mobile devices was handled by a dedicated [mobile include](/readme_files/include-mobile.png) whilst the display for larger screens was handled by a different [include](/readme_files/include-main.png).

All pages of the site were built upon this base template by adding the following code at the top of their html files:

```{% extends "base.html" %}```
### The Home Page
The [landing page](/readme_files/home-page.png) for the site was design to invite the user into the site using a door background image.
A carousel of selected digital artworks gives an immediate impression of the artwork to be found within.
The Sarah Rae Illustrations brand logo is present on [mobile](/readme_files/mobile-logo.png) and [larger](/readme_files/large-logo.png) screens.

### Viewing and Navigation
Issues relating to viewing and navigation may be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3AMVP+label%3A%22Viewing+and+Navigation%22).

#### Navigation
The all areas of the site are accessible via the nav-bar, with the two main areas (Shop and Gallery) easily available in the [mobile](/readme_files/mobile-nav-main.png) and [larger screen](/readme_files/large-main-nav.png) size.
The utility areas (Search, My Account, Shopping Bag) area accessed from the top line of the nav bar in both [mobile](/readme_files/mobile-nav-main.png) and [larger](/readme_files/main-full-nav.png) screens.
The logo, when clicked, will redirect the user to the home page.

In the Shop and Gallery areas of the site, where products and digital art works are listed, the user may easily navigate to the top of the page by clicking on the ['back to top arrow'](/readme_files/back-to-top.png).

The [footer](/readme_files/footer.png) has links to Sarah Rae's [Facebook Buisness page](https://www.facebook.com/profile.php?id=100094754029581) and her [Instagram](https://www.instagram.com/sarahrae.illustrations/?igshid=OGQ5ZDc2ODk2ZA%3D%3D) page.

##### Responsive Navigation
When the user hovers over a navigation feature of the page, it responsively changes colour indicating that an action is about to take place.
Examples are:
- [A drop-down menu item](/readme_files/responsive-1.png)
- A [button](/readme_files/responsive-3.png) when [hovered over](/readme_files/responsive-2.png).
- The [logo](/readme_files/responsive-4.png) when [hovered over](/readme_files/responsive-5.png).
#### Viewing Products
A list of [products](/readme_files/product.png) may be viewed on entry to the shop area of the site, and a [detailed description of a particular product](/readme_files/product-detail.png) is obtained by clicking on it.
#### Viewing Digital Art Works
A list of [Digital Art Works](/readme_files/gallery.png) may be viewed on entry to the Gallery area of the site, and a [detailed description of a particular art work](/readme_files/gallery-detail.png) is obtained by clicking on it.

### Products Filtering Sorting and Searching
Issues relating to product filtering, sorting and searching may be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3AMVP+label%3A%22Sorting+and+Searching%22&sortedBy%5Bdirection%5D=desc&sortedBy%5BcolumnId%5D=Labels).

#### Keyword Search
At the top of every page is a [search bar](/readme_files/search-bar.png). The user can enter any word or combination of words, and any products whose associated data (title, description, category, price etc) which match these keywords will be shown on the Shop main page.
#### Sorting Products
The list of products in the shop may be sorted from the [nav bar](/readme_files//sort-1.png) or in a more detailed way, from the [shop page body](/readme_files/sort-2.png). A variety of [sort options](/readme_files/sort-3.png) are provided.
#### Filtering by Category
Products may be [filtered by category](/readme_files/filter-category.png).
### The Shopping Cart
Issues relating to Purchasing and Checkout can be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3AMVP+label%3A%22Purchasing+and+Checkout%22&sortedBy%5Bdirection%5D=desc&sortedBy%5BcolumnId%5D=Labels)

Products are added to the shopping cart by clicking on a product, selecting the quantity of a product, then clicking '[Add to Cart'](/readme_files/add-to-cart.png).

An icon of the shopping cart is shown on every page. An empty cart shows ['0 Items'](/readme_files/empty-cart-icon.png).
When the user has items in their shopping cart, the [cart icon changes colour and shows the number of items in the cart](/readme_files/cart-with-items.png).

The [Shopping cart](/readme_files/shopping-cart.png) shows a list of products to be purchased, with product image, description, unit price, quantity and subtotal for each product. The quantity of a product can be updated, and a product can be removed from the cart.
### Checkout
When the user is reaches the [checkout area](/readme_files/checkout.png), a number of features are presented:
- The user may return to the shopping cart to make changes before committing to a purchase.
- A summary of the items to be purchased is presented, with the sub-total and total price clearly shown.
- If the user is not logged in, the options to [create and account, or log-in](/readme_files/anonymous-checkout.png) are offered .
- If the user is logged in, the user is invited to [save shipping details](/readme_files/registered-checkout.png) in their profile to facilitate quicker future purchases.
#### Stripe Payments
Payment is securely handled using [Stripe](https://stripe.com/gb?utm_campaign=UK_en_Search_Brand_Stripe_EXA-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450259&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=CjwKCAjwrranBhAEEiwAzbhNtcaozezcnkb4l0L0va3I_rzsTmkjyqlUF8ASjdiG8QGPiYYTtf3aphoCA0UQAvD_BwE).

In this app, the stripe ['Payment Element'](https://stripe.com/docs/payments/payment-element) was used in contrast to the more outdated ['Card element'](https://stripe.com/docs/payments/payment-card-element-comparison) used in the Boutique Ado walkthrough.
Since the integration of these elements into the app is significantly different, the fundamental payment , shipping details and order management architecture had to be reworked for this project compared to the Boutique Ado Walkthrough project.
This was not entirely successful in this version of the app, and there remain a number of outstanding issues which render the app less than satisfactory.
Purchases are able to be made successfully in this version, but an efficient integration was not achieved.
##### Outstanding Stripe Integration Issues 
- Webhook are active but not used
- Shipping data is added to the Payment Element on checkout, and not via the User Profile.
- The Payment element does not pre-populate with user profile shipping data
- A Session Variable is used to indicate that the user would like to store their shipping details for future use, rather than this being included in the Stripe Payment Element data.

Future versions will properly integrate with Stripe by including the following:
- A stripe product will be defined for each product on the site
- A stripe price will be allocated to each product
- Stripe analytics will thus be made available to the Site Owner.
#### Order Completion
When Stripe returns a response confirming that payment was successful, the [Order Success page](/readme_files/success.png) is shown.
This contains a summary of the order, including the user shipping details, and user email, the order id. and the order details.
The user is advised that a confirmation email is will be sent to the user's email address.
### Toasts
Feedback is given to the user throughout the site when actions or events take place.
These are made using the django messaging framework, and including these within Bootstrap toasts.
#### Django Messaging
Django makes it easy to send messages with a variety of status levels, from the backend to the front end for the application. The messages can by handled in different ways according to their status. eg. A warning status massage could be displayed in red, and a success message displayed in green etc.
#### Toasts
Toasts were used to provided a positive user experience when receiving site feedback with django messages.
Bootstrap toasts are 'pop-up' boxes which display information for particular events and whose behaviour and appearance can be customised.
An example of a toast may be viewed [here](/readme_files/toast.png):
### Profile App
Registered Users have a User Profile.
This is accessed via the main [nav-bar](/readme_files/my-profile-nav.png).

The ['My Profile'](/readme_files/profile.png) page shows the stored shipping details for the user, which may be edited by the User, and a summary of their order history.

If the user clicks on a particular order number, [the details for that order](/readme_files/order-hitory-item.png) are displayed. A toast with a message status of 'information' (blue) is displayed to the user in this case.
### Admin and Store Management
Issues relating to Admin and store management may be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3AMVP+label%3A%22Admin+and+Store+Management%22&sortedBy%5Bdirection%5D=desc&sortedBy%5BcolumnId%5D=Labels)

The Site Owner may administer the site in various ways.
The ['My Account' Nav-bar menu](/readme_files/admin-nav.png) allows the manager to add new products and digital art works, and provides access to the [django admin area.](/readme_files/django-admin.png).

#### CRUD Functionality
Full CRUD functionality is made available to the site owner. They may Create, Read, Update and Destroy products and digital art works.
#####  Adding Products and Digital Art Works
- New products can be added by the site owner using an [empty product form](/readme_files/add-product.png)
- New digital art works can be added by the site owner using an [empty digital art work form](/readme_files/add-art-work.png).

##### Product and Digital Art Work Modification
When the site owner clicks on a particular [product](/readme_files/edit-product.png) or [digital art work](/readme_files//edit-art.png), the option to edit or delete that product or digital art work is offered. When the option to edit is clicked, the form for that [product](/readme_files/edit-product-form.png) or [digital art work](/readme_files/edit-art-form.png) is presented for editing.

### Emails
The django email engine is used for the following tasks:
- Email authentication on registering
- [Order confirmation](/readme_files/email.png)
The Mailchimp email provider will be used to send out a Newsletter.

## Issues arising from Project assessment and initial failure
The project was submitted in an incomplete state, resulting in it failing to meet some pass level criteria.
Issues identified in the assessment can be viewed [here](https://github.com/users/mikerae/projects/12/views/4?filterQuery=milestone%3A%22P5+Resubmission%22)
# Testing
[Back to Top](#sarah-rae-illustrations)
### Incremental Feature Testing
As each feature was added, it was tested manually to ensure that it behaved as desired.
#### Manual Testing
The following manual tests were made:
- [Test Log 1](/readme_files/testing/test-log-1.png)
- [Test Log 2](/readme_files/testing/test-log-2.png)
- [Test Log 3](/readme_files/testing/test-log-3.png)
- [Test Log 4](/readme_files/testing/test-log-4.png)
- [Test Log 5](/readme_files/testing/test-log-5.png)
### Automatic Testing
No automatic testing was used for the MVP.
Future versions will have full django unit and integration testing.
#### Human Testing
No human testing was done for the MVP.
Feedback from the site owner and customers will be used to develop future versions.

# Code Validation
[Back to Top](#sarah-rae-illustrations)
Validators were used to ensure that all aspects of the code was 'clean' according to industry standards.
## Python PEP8CI 
Python code
The code was tested using PEP8CI online http:# and passed without issue.
- [CI Python Linter](#)
## Pylint VSCODE linter
The pylint linter was used throughout development to ensure that problematic code was corrected as it was written.

A number of the lines in the settings.py file were raising a linting error because they were too long for standard use in a terminal. Since these settings were not going to be visible in a terminal, the errors were suppressed by adding the following to the end of the long line:
```
  # noqa E501
```

There were several instances where the VSCode Pylint identified that some objects had no members associated with them. These objects were, in fact, populated and accessible. This error message was disables by placing the following code at the the top of a file which generated this error.
```
# pylint: disable=no-member
```

The state of the currently deployed python code shows minor issues:
- [Pylint Output]()

## JavaScript
JSHint was used to validate javascript code.
- [JSHint results may be viewed here:](#)
## HTML
The W3C NU html validator was used. 1 information element originating in allauth code was exposed. Otherwise the code passed without issue.
- [W3C HTML Validator 1](#)
- [W3C HTML Validator 2](#)
- [W3C HTML Validator 3](#)
- [W3C HTML Validator 4](#)
- [W3C HTML Validator 5](#)

## CSS
The W3C CSS Validator was used.
- [W3C CSS Validator results may be viewed here:](#)

# Bugs and Fixes
[Back to Top](#sarah-rae-illustrations)
Bugs are recored as Issues with a Bug template and Bug lable in the Github repo.
Bugs which have been fixed can be viewed [here](https://github.com/mikerae/sarah-rae-illustrations/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)
## Known Issues
[Back to Top](#sarah-rae-illustrations)
- [Search error does not show in messages #82](https://github.com/mikerae/sarah-rae-illustrations/issues/82)
- [Search in Gallery #83](https://github.com/mikerae/sarah-rae-illustrations/issues/83)
- [Update cart JS #84](https://github.com/mikerae/sarah-rae-illustrations/issues/84)
- [Mobile Cart #86](https://github.com/mikerae/sarah-rae-illustrations/issues/86)
- [Mobile Display: Quantity #87](https://github.com/mikerae/sarah-rae-illustrations/issues/87)
- [Order Line Items: No subcategories #92](https://github.com/mikerae/sarah-rae-illustrations/issues/92)
- [Admin LineItem Order: No category or subcategory #95](https://github.com/mikerae/sarah-rae-illustrations/issues/95)
- [lumberjackie.jpeg or .png #99](https://github.com/mikerae/sarah-rae-illustrations/issues/99)
- [Complete Purchase AnonymousUser #117](https://github.com/mikerae/sarah-rae-illustrations/issues/117)

# Resources
[Back to Top](#sarah-rae-illustrations)

The following resources were used:
+ Code Institute Training Material
+ Python Documentation: 
+ Django Documentation: https://docs.djangoproject.com/en/3.2/ref/
+ Stack Overflow: https://stackoverflow.com/
+ Wikipedia: https://en.wikipedia.org/wiki/Main_Page
# Marketing
[Back to Top](#sarah-rae-illustrations)
## Demographics
Who is your ideal customer and why do they buy your product?

⁃   A fantasy fairytale lover who enjoys a whimsigothic twist, they love the quirky characters of the Addams Family and the magical feeling of seeing Cinderella’s dress (Ever After) and Tinkerbell’s dress (Hook) and Sarah’s Ballgown (Labyrinth), they want to be sucked into an adventure they can imagine themselves loving.

⁃   They would buy my art to feel that magical wonder, and explore the richly coloured painterly illustrations that feel like a movie scene, to connect to that inner child that loves fairytales and whimsical people
## Branding
### Mission
What does the brand aim to achieve & how will it be achieved?

- Illustrations that explores and expands on whimsical magical worlds full of adventure so evocative the audience can imagine themselves there and what they’d want to do while there. Our brand will achieve this by creating narrative illustrations that show rich and wondrous experiences/ places/ people but with illustrations of everyday activities to ground it into reality, as if taking a snapshot of a character going about their day
- Explore these whimsical worlds by telling stories within the painting and grounding it with everyday experiences the viewer can see themselves in
### Purpose
- To create storybook illustrations that makes the viewer feel like someone from the story painted what happened and the paintings were found and put with the literature centuries later
- To bring a sense of “wow that’s a really cool creature!”, “I would love to fly over those lakes”, “that’s the dress I want for my wedding”, “I want them to be my friend”, “that would be my pet”
### Objective
- To bring people a whimsical magical world and adventures to imagine themselves in when they look at the artwork
### Serving its audience
- Through illustrated books or just solo paintings, to evoke that otherworldly magic and interest to know more about the story there eg. “That character likes soup and is looking at a photo, did the person in that photo like soup too?”
### Vision
- The illustrations take you into worlds so enchanting and real, it feels like coming home   
### Differentiators
- fantastical content in a realistic painterly style using film techniques such as shot framing, lighting and costume design to tell the story
- The priority is to evoke a specific emotion within the context of the narrative, so the viewer will receive more than a nicely painted image or an interesting character design
- Whimsical, enchanting elements with dark mystifying twists yet grounded with familiarity and comfort
- Communicate a story in such detail the characters or places feel real
### Tone
- whimsically inspiring and soulful 
### Brand Descriptors
- Accepting
- Exciting
- Imaginative
- Personal
- Thoughtful
- Wholesome

```
Fairytale              Whimsi-gothic          Quirky -characters.              Magical feeling.                       
       
                adventure.                 Wonder.                      Rich colour.            Painterly

 Movie scene.                Connect to inner child.           Grounded in reality.            Enchanting

        coming home.           Evoking emotion.          Inspiring.            Soulful             Mystifying Twists
```

## Search Engine Optimisation
The site optimises its visibility to prospective customers through Search Engines with the use of the following:
- A robots.txt file
- A sitemap.xml file
- Descriptive meta tags
- rel attributes on links to external resources
### Meta Data Tags
Meta Data tags showing semitics and keywords were used in headers and on elements.
#### Semiotics
```
Fairy.  Storybooks.    Curly branches.   Witches.    90s.      Burgundy.     Purples.         Orange.          Navy blue.     Velvet.    Wholesomely weird creatures.     Sparkles.        Clouds.     Treasure chest.      Pirate ship.      Stars.     Autumn/ gold + blue sky.        Dynamic framing/lighting.       Child reading
Child sleeping with dreams above.      Treehouses.      Kites.         Splashing in muddy puddles
Rope swing.      Playing dress up/pretend.           Reading under a tree.            Eating at home
Making something.      Soup.        Bread & butter.        Iridescent.        Shiny.       Glass.     Glowing white
Shimmering blue       Hobbit hole.       Gathered round Fireplace.     Blankets.     Tea.     Pet curled up.   
Mailbox.          Welcome mat.           Facial expression close-up.           Happy tears.           Wide-eyed.  Fireworks.    Flying.     Colourful lights.      Golden light.            Theatrical villains.        Wispy fabric
Dark forest
```
#### Keywords
```
sarah rae illustrations
sraeillustrations
sarah rae art
sarah rae artist
sarah rae art prints
```
## Social Media
Links to the following Sarah Rae Illustrations social media platforms are found in the footer of each page and may be viewed here:
- [Facebook Buisness page](https://www.facebook.com/profile.php?id=100094754029581)
- [Instagram Page](https://www.instagram.com/sarahrae.illustrations/?igshid=OGQ5ZDc2ODk2ZA%3D%3D)

# Deployment
[Back to Top](#sarah-rae-illustrations)

The project was deployed to Heroku in the initial stages of development in order to resolve early and fundamental deployment issues.
### Deployed App Cloud Server: Heruko
Heroku was used to deploy the django project backend

### Cloud Database: ElephantSql
ElephantSql was used for data storage

### Cloud Static and Media Server: AWS3

#### Add Heroku Host Name in Settings.py
- in ALLOWED_HOSTS add the heroku app name
```
ALLOWED_HOSTS = ['#sarah-rae-illustrations.herokuapp.com', 'localhost']
```
#### Create 3 directories in the top level directory, next to manage.py
- 'media'
- 'static'
- 'templates'
#### Create a Procfile
This tells Heroku that thew app will be displayed using the gunicorn webserver
- Create 'Procfile' at the top level, next to manage.py
```
web: gunicorn django_string_rota.wsgi
```
#### Push to GitHub and connect repository to Heroku
- Push to git hub
- In Heroku, #sarah-rae-illustrations:
    - Click on 'Deploy"
    - Select GitHub Connect to Github
    - Select the #sarah-rae-illustrations repository
    - choose automatic deployment

#### Create app on Heroku
The app "#sarah-rae-illustrations" was created on Heroku by:
- Logging into Heroku
- Clicking on New
    - Click "Create new app"
- Giving the app a unique name.
    - "#sarah-rae-illustrations" was accepted as unique
- The region was chosen as:
    - Europe
- The app was created:
    - Click "Create app"

#### Create database on ElephantSQL
The database "#sarah-rae-illustrations" was created on ElephantSQL by:
- Logging into ElephantSQL
- Click on "Create New Instance"
- The plan was named "#sarah-rae-illustrations"
- The plan type was " Tiny Turtle (Free)
- Click on "Select Region"
- "EU-West-1 (Ireland)" was selected by default
- Click on "Review"
- Click on "Create Instance"

#### Store database environment variables in env.py
- create a file "env.py" at the top directory in the workspace, at the same level as requirements.txt
- ensure that "env.py" is added to .gitignore so that it's sensitive contents are not pushed to github.
- In env.py
    - Import the os library
    - Add the DATABASE URL to the environment

        ``` 
        import os
        os.environ["DATABASE_URL"] = "<copiedURL>"
        ```
    where "copiedURL" is replaced by the copied elephantSQL "#sarah-rae-illustrations" URL

    - Add a secret key to the environment
        ```
        os.environ["SECRET_KEY"] = "my_super^secret@key"
        ```
#### Modify settings.py
- The following code was added to the settings.py file below PATH import:
```
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
- Replace the insecure Django SECRET_KEY with the env.py SECRET_KEY
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
- Comment out the default database url variable (which would have connected Django to the internal db.sqlite3 database) and add a link to the env.py database url (the ElephantSQL remote database)
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
#### Migrate changes to django database
```
gitpod /workspace/#sarah-rae-illustrations (main) $ python3 manage.py migrate
```
#### Test connection with remote ElephantSQL database
- In the dashboard for ElephantSQL (logged in)
    - select "#sarah-rae-illustrations" instance
    - on the left menu
        - select BROWSER
        - select 'Table queries'
            - observe the dropdown is populated. This means that tables have been created by django in this database, and that the connection between django and the database is made.
#### Add Environment Variables to Heroku
- In '#sarah-rae-illustrations'
    - Click on 'Reveal Config Vars'
    - Add the following KEYS and their corresponding VALUES (without "")from env.py:
        - DATABASE_URL
        - SECRET_KEY
        - PORT 8000

####  data to Django db.sql and ElephantSql
##### Initial Data Loading
Initial data was imported into the project using set_up.py and associated utilities. This data was available from a spreadsheet stored in googledocs. set_up.py securely logged into the spreadsheet and retrieved the required data, then loaded the data into the models in the correct order.
#### Subsequent Data Loading
Once a credible starting data set was established, this data set was dumped into a db.json file in the fixtures dir using the following command.

```
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 > db.json
```
When the local  database needed to be reset:
- The db.sql file was deleted
- Migrations were run
- The db.json file was loaded using Loaddata

When the remote database needed to be reset:
- The database dashboard was accessed from the ElephantSql site
- The database was reset
- DEVELOPMENT variable was commented out in  env.py 
- Migrations were run
- The db.json file was loaded using Loaddata
#### Add AWS Environment Variable
- In created AWS Account
    - Copy 
- In env.py
    - add environment variable:
    ```
    os.environ["CLOUDINARY_URL"] = "copied_url"
    ```
- In Heroku Config Vars
    - Add CLOUDINARY_URL: copied_url
#### Add Temporary Config Var to Heroku
There are no static files yet, and without the following variable set, the build will fail on Heroku.
Once static files are introduced into the project, this variable can be removed.
- DISABLE_COLLECTSATICK:1
#### Update Installed Apps and media/ static files in settings.py
The deployment platform, Heroku, is ephemeral i.e. when it is not being used, it stops running actively and any state data is lost. It is necessary, therefore, to store static files in a permanent state location. For this project, Amazon AWS3 was used as the permanent storage location for the static and media files.

```
INSTALLED_APPS = [
   
]
```
- below STATIC_URL = '/static/'  add the following:
```

```
#### Add a Templates Directory in settings.py
- under BASE_DIR = Path(__file__).resolve().parent.parent add the following:
```
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
- in TEMPLATES give 'DIRS' the value 'TEMPLATES'
```
TEMPLATES = [
   
]
```
#### Build, deploy and open app on Heroku
After some trouble-shooting (see bugs and fixes) the default Django landing page was shown on the Heroku deployed site.

#### Deployment Process
The project was deployed to the Heroku platform using the following steps:
- Delete unused resources/libraries
- Add \n to input line
- pip3 freeze > requirements.txt
- commit & push to gitHub
- make Heroku account
- create new app (in Heroku)
- in dashboard : open settings
- in settings : open config vars
    - add config vars
- in deploy
    - choose deployment method
        - GitHub
        - connect to GitHub
        - Authorise Heroic to access your gitHub
        - search for and connect to repository name
        - choose a deployment method (Enable Automatic Deploys)
        - main branch
        - click view to open a web page with the deployment in a browser

#### Freeze requirements
Before deployment, the imported libraries were frozen into the requirement.txt file so that they could be available in the deployed virtual environment. The following code was used:
```
pip3 freeze > requirements.txt
```
### Final Deployment
The following additional steps were taken before final deployment
- The GitHub Repository was made public
- Django debug mode was set to FALSE
The project was deployed to the Heroku platform using the following steps:
- Delete unused resources/libraries
- Add \n to input line
- pip3 freeze > requirements.txt
- commit & push to gitHub
- make Heroku account
- create new app (in Heroku)
- in dashboard : open settings
- in settings : open config vars
    - add config vars
- in deploy
    - choose deployment method
        - GitHub
        - connect to GitHub
        - Authorise Heroic to access your gitHub
        - search for and connect to repository name
        - choose a deployment method (Enable Automatic Deploys)
        - master/main branch
        - click view to open a web page with the deployment in a browser

# Resources
[Back to Top](#sarah-rae-illustrations)

The following resources were used:
+ Code Institute Training Material
+ Python Documentation: 
+ Django Documentation: https://docs.djangoproject.com/en/3.2/ref/
+ Stack Overflow: https://stackoverflow.com/
+ Wikipedia: https://en.wikipedia.org/wiki/Main_Page
# Acknowledgments
[Back to Top](#sarah-rae-illustrations)

Grateful acknowledgment is given to the following:
- Mentor: Dario Carrasquel for encouraging and focused support
- Particular thanks are offered to the Code Institute Tutors who patiently and most helpfully enabled me to make progress on the many occasions when I got stuck on an issue.

- Code Institute: for training materials, training environment and specific code
- Stack Overflow https://stackoverflow.com/
- Django Documentation https://docs.djangoproject.com/en/3.2/ref/models/fields/

 