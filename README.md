<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/petrov8/DjangoAcademy">
    <img src="static/images/logo.jpg" width="240" height="200" alt="accessibility text">
  </a>

<h3 align="center">Careers Website</h3>

  <p align="center">
    Your fast track to a new career !
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An online platform enabling lecturers to create and publish online programming courses. 
Registered students can then choose relevant courses and sign-up for them. 
Administrators and Master Users oversee the entire process. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With: 

* Django (SSR) - https://www.djangoproject.com
* PostgreSQL - https://www.postgresql.org


### Deployment:

* Docker - https://www.docker.com
* NGINX - https://www.nginx.com
* AWS EC2 - https://aws.amazon.com/ec2/

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

1. Clone the repo
   ```sh
   git clone https://github.com/petrov8/DjangoAcademy.git
   ```

Ensure your machine has 'Python3' and 'pip' installed: 
* python 
  ```sh
  python --version 
  pip --version 
  ```
  Alternatively download and install from https://www.python.org/downloads/


### Installation:

1. Install dependencies:    
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Setting up DB:

1. Create Migrations:    
   ```sh
   python manage.py makemigrations 
   ```

2. Set-up database:    
   ```sh
   python manage.py migrate
   ```

3. Upload permission groups in 'Django Admin' :    
   ```sh
   python manage.py migrate
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Creating Master User:

1. Create Master User :    
   ```sh
   python manage.py createmasteruser
   ```

Users may choose from the following profile options:

Profile Options:

    "Guest" (no login required):
    - Can access course listings with no further details.

    "Student" (logged in):
    - Can access course listings and additional details.
    - Can update or delete profile. 

    "Lecturer" (logged in):
    - 
    - Can access course listings and additional details.
    - Can update or delete profile. 
    - Can publish new courses.
    - Can edit own publications.
    - Can delete own publications.

    "Admin" (logged in):
    - Can change user roles to Admin or Lecturer.
    - Can access course listings and additional details.
    - Can update or delete profile. 
    - Can edit any course listing.
    - Can delete any course listing.

    "Master" (logged in):
    - Can change user roles to Admin or Lecturer. 
    - Can access course listings and additional details.
    - Can publish new courses.
    - Can update or delete profile. 
    - Can edit any course listing.
    - Can delete any course listing.
    - Can delete any user profile. 


Functionalities:

    "Publish Course":
    - Lecturers or Masters can publish new courses. 

    "Catalogue": 
    - Shows basic info about available courses.

    "Details": 
    - Shows further details about a specific course listing. 

        "Participate":
        - Student (only) can apply for a given course.

        "Course Opt Out":
        - Students (only) can sing-out from a given course.

        "Edit Course": 
        - Allows lecturers to edit their courses. 
        - Listings can be edited by their owners, admins or masters .

        "Delete Course": 
        - Allows lecturers to delete their courses. 
        - Listings can be deleted by their oners, admins or masters .

    "Profile": 
    - Shows personal details of logged-in users. Automatically extended for Lecturers. 
    - Profiles can be edited or deleted by their owners, by admins or masters.
    - In case user hasn't provided a profile photo link, a default one will be rendered.

        "My Courses": 
        - Students: shows catalogue of courses the student has signed-up for. 
        - Lecturer or Master: shows catalogue of courses the user has published.

Features:

    - Deployed at http://django-academy.tk with Docker and Amazon EC2. 
    - Seach Bar - users can search for available courses by name. 
    - Student have to pay before signing-up for a course (to be extended with PayPal or Wise Sandbox API).
    - Django Admin:
        - Admins can see total number of courses, students and average course price per lecturer. 
        - Admins can see total number of courses a student has signed-up for an average amount spent.
        - Other small improvements. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap


- [1] REST API - Re-factor into Client side and Server side. 
- [2] Adjust HTML & CSS theme. 
- [3] Payments - simulate payments via PayPal or Wise sandbox mode.


See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Angel Petrov - a.petrov089@outlook.com

Project Link: [https://github.com/petrov8](https://github.com/petrov8/CareersWebsite)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

