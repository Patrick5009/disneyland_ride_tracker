# Welcome to The Disneyland Ride Tracker App
<img width="1267" alt="log in page" src="https://github.com/user-attachments/assets/0c7f4a9e-57b7-4c8e-8a74-5687a4228d4b" />

## Project Description
### The Disneyland Ride Tracker app will help you visit the rides you plan for in the limited time you have.
This responsive app will let you create a personalised list of all the rides you want to visit while on your trip at Disneyland. You'll be able to add whatever ride is available at the resort, activley keep track of any rides you have already been on and see any of the remaining ones you have yet to visit, easily and responsively on your phone while you travel around the resort. You can easily pick from a list of pre-built ride names or add your own name for the ride. Once you have marked them as complete, their status is marked as such, making it easy to see any rides you have yet to visit. If you add an incorrect ride you can easily delete it or edit it. The Disneyland Tracker app will save you so much time and get you organised for maximum fun. If you only have a single day pass at the resort then this app is a must have. 
# [Link to Live Disneyland Tracker site](https://disneyland-ride-tracker-07b2f49cf7e9.herokuapp.com/accounts/signup/)
This project was built by Patrick Walsh and is to be graded by Code Institute as his final project in an intensive Full Stack software developer bootscamp.
---
# Table of Contents  
 1. [UX](#ux)
 2. [Agile Development](#agile-development)
 3. [Features Implemented](#features-implemented)  
 4. [Features Left to Implement](#future-features)  
 5. [Technology Used](#Technology-used) 
 6. [Testing](#testing-and-validation)  
 7. [Deployment](#deployment)
 8. [Resources](#resources)  
 9. [Credits and Acknowledgements](#credits-and-acknowledgements)
---
## User Demographics
This app is designed for Disneyland visitors looking to make the most of their time—whether they’re first-time guests eager to see it all, seasoned park-goers optimizing their schedule, or families navigating a packed day with kids. It’s ideal for anyone who values efficiency, wants clear visibility into their ride checklist, and prefers a convenient mobile solution to plan their day on-the-go. Whether you have a single-day pass or a multi-day trip, if your priority is to stay organized, save time, and ensure you don’t miss the must-do attractions, this app was built for you.
# UX
## Database Planning
The chosen Entity Relationship Diagram (ERD) is deliberately kept simple to maintain a clear focus on delivering the Minimum Viable Product (MVP). This straightforward approach sets a well-defined foundation while preserving the flexibility to develop a new ERD if substantial features or changes are introduced later on.

<img width="633" alt="ENTITY RELATIONSHIP DIAGRAM" src="https://github.com/user-attachments/assets/4fd3d89f-51f8-4c97-8a73-c71acc622b78" />

Below is a basic user flow chart that focuses on the foundational interactions—registering, logging in, configuring a custom user model, and reaching the home page. Features like adding, deleting, or editing items aren’t included in this initial diagram, as it’s centered on the core functionality required to get users into the app and ready to engage. Future iterations of the flow chart will incorporate these additional steps as the project evolves beyond the Minimum Viable Product stage.

<img width="517" alt="USER FLOW CHART" src="https://github.com/user-attachments/assets/646baedb-cb49-48d2-94b1-bd33156810a6" />

## UX Design
### Overview
The Disneyland Tracker app is designed with a user-centric approach, focusing on simplicity, responsiveness, and efficiency. The app’s UX prioritizes an intuitive interface that allows users to easily manage their ride list while navigating Disneyland.The user stories guided the design process, ensuring the app addresses key user goals, such as creating and managing a personalized ride list, account security, and mobile usability. Clear Feedback mechanisms enhance the user experience, making the app a reliable tool for Disneyland visitors.
### Site User
- Casual park visitors: Individuals visiting Disneyland for the first time or infrequently, looking to maximize their experience with minimal planning.
- Disney enthusiasts: Regular visitors who want a convenient way to keep track of rides and explore new attractions.
- Families and groups: Visitors managing multiple schedules who need an organized way to coordinate and track rides for everyone.
  
These users share a need for efficiency, ease of use, and a mobile-friendly solution to manage their Disneyland experience.
### Goal
The main goal of the Disneyland Tracker app is to provide users with an efficient and stress-free way to plan and track their Disneyland experience. By enabling users to create a personal ride list, manage their progress. The app helps visitors make the most of their time at the park. This ensures users can focus on enjoying their trip rather than worrying about logistics.
## Wireframes
The Disneyland Tracker app’s wireframes were created using Balsamiq, focusing on both full-screen and mobile layouts. These wireframes provide a visual blueprint of the app's design and functionality.
The full-screen wireframe illustrates the layout for desktop and larger devices. It emphasizes clarity with a central ride tracker section to manage and view rides efficiently.
Clear buttons for adding, editing, and deleting rides.

<img width="812" alt="WIREFRAME big screen" src="https://github.com/user-attachments/assets/60886411-736d-4df5-8185-531d5668dfe6" />

The mobile wireframe is optimized for smaller screens, ensuring usability on the go. Key features include a responsive design that adapts the navigation bar into a collapsible menu and Stacked content layout to accommodate vertical scrolling.

<img width="206" alt="WIREFRAME mobile" src="https://github.com/user-attachments/assets/88fa41b4-2740-4c28-891b-0374e755b7fd" />

# Agile Development
These user stories provided a clear roadmap for development, ensuring each feature was aligned with the app’s purpose. They also helped prioritize functionality, starting with core features like account creation, ride management, and responsive design. 

https://github.com/users/Patrick5009/projects/7
<img width="1279" alt="ScreenHunter 1265" src="https://github.com/user-attachments/assets/ac6d45c3-674d-4a5e-b68a-31c89598f890" />

### User Stories Overview
As a User I can create an account so that I have a personal ride list that keeps track of what rides I have been on.
 - Sign up page includes fields for name password and email.
 - A confirmation message is shown upon registration.
   
As a User I can log in to my account so that I can access my personal ride tracker and continue tracking my rides.
- Login page includes name and password fields.
- Login page redirects to the ride tracker page after login.
  
As a user I can add a ride to my ride list so that I can track which attractions I want to visit during my time at Disneyland.
- Have a text input field for entering a ride name.
- Clicking "Add Ride" button adds the ride to the ride list.
- The ride is saved to the user’s account in the database.
  
As a user I can delete a ride from my list so that I can remove rides I’ve already been on or no longer have time for.
- Each ride in the list has a "Delete" button.
- Clicking the delete button removes the ride from the list and database.
- An 'Are You Sure' prompt appears before accepting delete.
  
As a user I can edit the name of a ride on my list so that I can correct any mistakes or update my ride plans.
- Each ride has an "Edit" button.
- Clicking "Edit" creates a text field with the current ride name in it
- Clicking "Update Ride" saves the new ride name and updates the ride list.
  
As a user I can log out of my account so that my ride list remains private.
- A "Log Out" button is present on the navbar.
- Clicking "Log Out" logs out user and redirects to the login page.
  
As a user I can use an clean and simple interface so that I can quickly and easily manage my ride list without confusion.
- The ride tracker page has clear buttons for adding, editing, and deleting rides.
- The list updates immediately after any action is performed.
- Navigation between pages is obvious and simple.
- Wrong login shows error message.
  
As a user I can see a confirmation message when I perform an action so that I know my changes were successful.
- A pop-up message appears after adding editing or deleting a ride.
- The message disappears after clicking "Dismiss."
  
As a user I can view my list of rides so that I know exactly how many rides I have left to go on.
- All rides added are shown in a list.
- All ride entries include the ride name and edit/delete buttons.
  
As a user I can use the app on my phone so that I can manage my ride list on the go.
- Acceptance Criteria
- The app layout is responsive and elements resize for smaller screens.

# Features Implemented
## Home Page 

<img width="1267" alt="home page" src="https://github.com/user-attachments/assets/a1def1d1-c114-4f78-8612-a421bb630947" />

The home page of the Disneyland Tracker app serves as the central hub for managing and tracking rides. Its key features include:
1. Ride List Display
Displays a list of all rides added by the user.
Each ride entry includes:
The ride name.
"Edit" and "Delete" buttons for easy management.
Status indicator showing whether the ride is marked as "Completed" or "Pending."
2. Add Ride Section
A text input field for entering the name of a ride.
An "Add Ride" button that adds the new ride to the user’s list and saves it in the database.
3. Action Feedback
Confirmation messages appear after actions such as adding, editing, or deleting a ride.
Messages provide real-time feedback, ensuring users know their actions were successful.
4. Edit Ride
Clicking "Edit" opens a text field with the current ride name pre-filled.
The "Update Ride" button saves the updated name, refreshing the list with the changes.
5. Delete Ride
Each ride has a "Delete" button.
A confirmation prompt ("Are you sure?") appears before removing the ride from the list.
Deleted rides are also removed from the database.
6. Navigation
Clear and intuitive navigation links in the navbar for:
Logging out.
Returning to the home page (if applicable).
The navbar is responsive, collapsing into a hamburger menu on smaller screens.
7. Mobile-Responsive Design
Optimized for use on mobile devices.
Layout adjusts for smaller screens with:
Vertical stacking of rides.
Large, touch-friendly buttons for actions.
Collapsible navigation bar for space efficiency.
8. Dynamic Updates
The ride list updates in real time after any action, such as adding, editing, or deleting rides, without requiring a page reload.
These features make the home page the core of the user experience, providing a clean, efficient, and user-friendly platform to manage Disneyland ride plans.


## Login Page

<img width="1267" alt="log in page" src="https://github.com/user-attachments/assets/f55adbc1-1626-4232-ae40-a50f1bb72e92" />

The login page ensures only authorized users can access the app while providing a clean, secure, and efficient login experience. 

Input Fields
Fields for username/email and password.
Clearly labeled for easy navigation.
Login Button
A "Log In" button submits credentials for verification.
Redirects to the home page on success.
Error Handling
Displays error messages for incorrect credentials (e.g., "Invalid username or password").
Prompts users to try again.
Forgotten Password
Link to the registration page for new users.
Mobile-Friendly Design
Fully responsive layout with touch-friendly elements for mobile users.
Security
Uses HTTPS for encrypted data transmission.
Secure password hashing ensures user safety.
Redirects
Redirects to the home page after login.
Automatically directs unauthorized users to the login page.

## Registration Page

<img width="1267" alt="register page" src="https://github.com/user-attachments/assets/6a16e898-c471-4d30-9144-b0faa40388e5" />

The registration page allows new users to create an account for accessing their personalized Disneyland ride tracker. It is designed for simplicity and security.

Input Fields
Fields for username, email, and password.
Clear instructions for required information.
Sign-Up Button
A "Sign Up" button submits the form for account creation.
Redirects to the login page or home page upon successful registration.
Error Handling
Displays error messages for invalid inputs (e.g., "Email already in use").
Ensures users know how to fix errors.
Confirmation Message
A success message confirms account creation.
Login Redirect
Link to the login page for users who already have an account.
Mobile-Friendly Design
Optimized for all devices with responsive input fields and buttons.
Security
Uses HTTPS for secure data transmission.
Ensures password hashing for account safety.

## Logout Page

<img width="1267" alt="logout page" src="https://github.com/user-attachments/assets/077add03-d460-4104-b693-076c76751676" />

Log-Out Button

A prominent "Log Out" button allows users to securely end their session.
Clicking the button redirects to the login page.
Confirmation
Users receive feedback confirming they have logged out successfully.
Navbar Update
After logging out, the navbar adjusts to display login and registration options only.
Security
Ends the session securely to prevent unauthorized access to the user's account.
Mobile-Friendly Design
Fully responsive layout ensures accessibility on all devices.

### Responsive Design

<img width="185" alt="ScreenHunter 1309" src="https://github.com/user-attachments/assets/da5154df-6802-4cf4-b83b-02c2ecebc2ca" />

The responsive design ensures that users can efficiently manage their ride lists whether they’re at home on a desktop or navigating Disneyland on their mobile devices, providing flexibility and convenience.

Flexible Layout
Automatically adjusts the layout to fit screen sizes, from large desktop monitors to small mobile screens.
Content stacks vertically on smaller screens for better readability.
Responsive Navbar
Collapsible navbar transforms into a hamburger menu on smaller screens for easy navigation.
Touch-Friendly Elements
Buttons and interactive elements are sized and spaced for optimal usability on touchscreens.
Dynamic Content Display
Ride lists and forms adapt to the available screen space without losing functionality.
Optimized Fonts and Images
Scalable fonts and images maintain clarity and usability on all screen sizes.


## Additional Security Features
These security features ensure that user data remains private and protected, fostering trust and providing a secure environment

- Secure Authentication
User credentials are securely encrypted during login and registration using HTTPS.
Passwords are hashed and stored securely in the database to prevent unauthorized access.

- Session Management
User sessions are terminated securely upon logging out, preventing access from other devices or browsers.

- Input Validation
All user inputs are validated to prevent SQL injection, XSS, and other vulnerabilities.
Invalid inputs display clear error messages for correction.

- Access Control
Pages requiring authentication are restricted to logged-in users.
Unauthorized users are redirected to the login page with a notification.

- CSRF Protection
Cross-Site Request Forgery (CSRF) tokens are implemented on all forms to prevent unauthorized actions.

# Future Features

- Progress Tracking
Visual progress tracker (e.g., percentage of rides completed).
Achievement badges for milestones (e.g., "5 Rides Completed," "Thrill Seeker").

- Park Navigation
Interactive map integration to locate rides within the park.
Directions to rides from the user’s current location using GPS.

- Ride Categories and Sorting
Group rides by categories like "Thrill Rides," "Family Rides," or "Kid-Friendly."
Sort rides by priority, location, or estimated wait time.



# Color Scheme

The Disneyland Tracker app utilizes a carefully selected color scheme to create a visually appealing and functional design:

<img width="564" alt="COLOR SCHEME" src="https://github.com/user-attachments/assets/e7ac2c70-1f7e-45b4-a9e5-4e957aa88eb0" />

- Primary Colors
#A6490E (Burnt Orange)

Adds warmth and energy to the design, drawing attention to key interactive elements such as buttons and highlights.
- #304C6B (Deep Blue)

Provides a calm and professional tone, used for backgrounds and sections to ensure readability and balance.
- #100F2E (Midnight Navy)

A rich, dark shade that serves as the foundation for the app's design, providing excellent contrast for text and elements.

Purpose
This color scheme was chosen to ensure a cohesive, visually pleasing aesthetic while maintaining accessibility and readability across devices. It balances vibrancy with professionalism, aligning with the app’s purpose of engaging and assisting Disneyland visitors.



# Technology used

Frontend
- HTML5: For structuring the content and creating semantic web pages.
- CSS3: For styling and ensuring a visually appealing design.
- Bootstrap: A responsive front-end framework for mobile-first design.

Backend
- Python: For server-side logic and handling backend functionality.
- Django: A robust web framework for managing the app’s backend, authentication, and database interactions.

Database
- PostgreSQL: A reliable and scalable relational database for storing user accounts and ride data.

Hosting and Deployment
- Heroku: For deploying and hosting the live app.
- Gunicorn: As the HTTP server for running the Django application.

Version Control
- Git: For version control during development.
- GitHub: For code storage, collaboration, and project management.

Additional Tools
- Balsamiq: For creating wireframes and planning the app’s design.
- Cloudinary: For potential hosting of static files and images (optional or planned future use).


# Testing and Validation

## Testing with Lighthouse

Lighthouse was used to test the app’s performance, accessibility, best practices, and SEO. This tool provided insights to ensure a smooth and optimized user experience.

Key Metrics
- Performance: Checked page load times and responsiveness.
- Accessibility: Evaluated semantic HTML, ARIA roles, and color contrast.
- Best Practices: Verified secure links, JavaScript integrity, and HTTPS usage.
- SEO: Ensured proper meta tags, titles, and alt attributes.

  <img width="415" alt="LIGHTHOUSE performance check" src="https://github.com/user-attachments/assets/3efcde78-4509-4403-a0de-5182ba41ce25" />

## WCAG Contrast Checker
 
The WCAG Contrast Checker was used to ensure that the Disneyland Tracker app adheres to Web Content Accessibility Guidelines (WCAG) for color contrast. This ensures text and interactive elements are readable for users with visual impairments or low vision.

<img width="1267" alt="CONTRAST home page" src="https://github.com/user-attachments/assets/bdedf183-235d-4f07-895f-3076e8dd924e" />

<img width="1268" alt="CONTRAST register page" src="https://github.com/user-attachments/assets/329ed0a6-e2cd-4c20-9b31-9f94280d38e3" />


<img width="1267" alt="CONTRAST sign in page" src="https://github.com/user-attachments/assets/dc02e3ba-37a1-40a8-a91b-b2a2aad5a0da" />


<img width="1266" alt="CONTRAST sign out page" src="https://github.com/user-attachments/assets/33bfbbc7-113f-4228-81f5-cda4108b868b" />


<img width="1277" alt="CONTRAST update page" src="https://github.com/user-attachments/assets/387c47f2-9f68-4e29-aff7-b8b87888561b" />

<img width="1280" alt="CONTRAST delete page" src="https://github.com/user-attachments/assets/a3b14f64-c4a2-46ee-b4ce-abd02a528b1d" />


## W3C CSS Validation Service

The Disneyland Tracker app's CSS was validated using the W3C CSS Validation Service to ensure the code adheres to modern web standards and best practices.


<img width="1269" alt="No Errors CSS The W3C CSS Validation Service" src="https://github.com/user-attachments/assets/78e289dc-4c06-42b5-b19f-4d7d53f83708" />



## HTML Validation
The Disneyland Tracker app's HTML was validated using the W3C HTML Validator to ensure it adheres to web standards and provides a strong foundation for accessibility and performance.
All my HTML errors have been resolved, ensuring compliance with web standards apart from some related to content generated by the Django Summernote editor in the admin panel. These are inherent to the editor's output and do not affect the app’s functionality or user experience.


<img width="1267" alt="VALIDATOR W3 html rides" src="https://github.com/user-attachments/assets/0580626c-e0c4-4de5-a2f6-6d5326a028ab" />



## Python Linter
The Python files were validated using the Code Institute Python Linter to ensure compliance with PEP 8 standards and maintain code quality.

<img width="798" alt="admin py" src="https://github.com/user-attachments/assets/b80eeb2a-b206-4680-aa90-c03173bcb16d" />

<img width="803" alt="forms py" src="https://github.com/user-attachments/assets/2ea1464d-a182-465e-8aea-4c3c7bc0310e" />


<img width="802" alt="models py" src="https://github.com/user-attachments/assets/accfbd89-7fb8-42df-8d5f-1e8384e03e87" />

<img width="897" alt="setting py" src="https://github.com/user-attachments/assets/9e2e92e1-03e1-4b92-9d41-16a74c2cc8b5" />


<img width="809" alt="urls app py" src="https://github.com/user-attachments/assets/15c3e284-eb04-4569-ac40-8b30ab516735" />


<img width="806" alt="urls py" src="https://github.com/user-attachments/assets/a4c366d8-38de-43c7-a7f2-aa63fc13745d" />


<img width="808" alt="view py" src="https://github.com/user-attachments/assets/5fd6d073-fce7-43ca-9f32-1e500eb13f25" />






## Home Page:
 - PASS - Input/Write functionality allows users to write or pick a ride.
 - PASS - Users must be logged in to create rides.
 - PASS - Users cannot delete or edit rides or created by other users.
    
## Login Page:
 - PASS - Secure signup functionality allows users to register securely.
 - PASS - Successful login redirects users to the home page.   

 ## Registration Page:
 - PASS - Secure login functionality allows users to log in securely.
 - PASS - Successful registration redirects users to the home page.

 ## Logout Page:
 - PASS - Logout functionality allows users to sign out securely.
 - PASS - After successful logout, users are redirected to the home page.

 ## Edit / Delete Pages:
 - PASS - Users can edit and delete their own rides.
 - PASS - Users must be logged in to edit or delete their own rides.
 - PASS - Users can click cancel buttons to exit from edit and delete pages 


# Deployment 
### Development
- Repository: The repository was created on GitHub, serving as the central location for code storage, version control, and collaboration.

- Coding Environment: The code was written and updated using Gitpod, a cloud-based development environment.

### Deployment
- Hosting: The app was deployed on Heroku, ensuring reliable and scalable hosting.
  The live app is accessible [Click Here](https://disneyland-ride-tracker-07b2f49cf7e9.herokuapp.com/accounts/signup/)

### Configuration
- Secret Keys: Sensitive data such as secret keys were securely added to Heroku's Config Vars to protect the application.
- Database: The Code Institute PostgreSQL database was connected to Heroku to manage and store app data.


# Resources
- [Pexels](https://www.pexels.com/)
- [bootswatch](https://www.bootswatch.com/)
- [Code Institute Full Stack Development course materials](https://codeinstitute.net/)
- [Cloudinary docs](https://cloudinary.com/documentation/programmable_media_overview)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Balsamiq](https://balsamiq.com/)

##### [ Back to Top ](#table-of-contents)
# Credits and Acknowledgements
Thanks to [to-do genie](https://github.com/Tedbot2000/todo-genie-01/tree/main) for inspiration,
Thanks to Dennis for his tutorial for help with the views [Dennis Ivy](https://www.youtube.com/watch?v=4RWFvXDUmjo),
Implementation of dropdown list and bug fixes [Chat gpt](https://chatgpt.com/),
Thanks to Steve for a Read me template to get me started [Steven Bevan](https://github.com/Stephen-Bevan)
Thanks to David Calikes my scrum master and tutor for the motivation and help [David Calikes](https://github.com/davidcalikes)
##### [ Back to Top ](#table-of-contents)
