## Junior Developer Applicant Dashboard
This project is a simple web application built with Django that serves as a dashboard for managing Junior Developer applicants. It allows you to list applicants, view their detailed portfolios, and manage their records.

## Features
* Applicant Listing: A dashboard page displaying a list of Junior Developer applicants with their basic information (first name, last name, email).
* Portfolio Details: Dedicated pages for each applicant to describe their portfolio and projects.
* Django Admin Integration: All data can be managed through Django's built-in administration panel.
* Bootstrap Styling: Utilizes Bootstrap for a clean and responsive user interface.

## Step-by-step guide on how to clone.
1. **Clone the repository:**
    ```bash
   git clone https://github.com/polynexe/JuniorDev.git
    cd JuniorDev
    ```

2. **Create and activate a virtual environment:**
    ```bash
     python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
   
4. **Database setup (for Django):**
    ```bash
    python manage.py migrate
    ```
   
5. **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
# Run the project

```bash
python manage.py runserver
 ```