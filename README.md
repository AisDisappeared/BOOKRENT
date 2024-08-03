# BookRent

BookRent is a Django-based web application that allows users to rent books with a modern interface styled using Tailwind CSS. The application supports both light and dark modes, features OTP for secure logins, and utilizes Linux scripts for automation. It also includes custom Django management commands and integrates the django-import-export package for data management.

## Features

- Book Rental: Users can browse and rent books.
- Tailwind CSS: Styled with Tailwind CSS, supporting both dark and light modes.
- Django widget tweaks: Forms Styled with django-widget-tweaks package.
- Class-Based Views: Utilizes Django's class-based views (CBVs) for better organization.
- OTP Authentication: Secure login and registration using one-time passwords (OTP).
- Custom Management Commands: Custom Django commands for various administrative tasks.
- Data Import/Export: export data to different formats such as json , xml and etc . with the django-import-export package.
- Linux Automation Scripts: Scripts for automating tasks.

## Installation

1. Clone the repository:

     ~~~bash
     git clone https://github.com/AisDisappeared/BOOKRENT.git
     ~~~

2. Navigate to the project directory:

     ~~~bash
     cd BOOKRENT
     ~~~

3. Create and activate a virtual environment:

   ~~~bash
   python -m venv venv
   ~~~

   source venv/bin/activate  //  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:

     ~~~bash
     pip install -r requirements.txt
     ~~~

5. Install Tailwind CSS:
   Follow the instructions in the [django-tailwind documentation](https://django-tailwind.readthedocs.io/en/latest/installation.html) to set up Tailwind CSS.

6. Apply migrations:

     ~~~bash
     python manage.py migrate
     ~~~

7. Run the development server:

     ~~~bash
     python manage.py runserver
     ~~~

8. Visit <http://127.0.0.1:8000/> in your browser.

## Usage

- Book Rental: Browse and rent books from the main interface.
- Dark/Light Mode: Toggle between dark and light modes using the provided switch.
- Manage Data: Use the django-import-export package to import and export book data.
- Admin Interface: Access the Django admin panel to manage books and user data.

## Configuration

- Django-Tailwind: Follow the [installation guide](https://django-tailwind.readthedocs.io/en/latest/installation.html) to configure Tailwind CSS.
- OTP: Set up OTP for authentication by using pyotp package.
- Linux Scripts: Execute provided scripts for automation tasks.
- Custom Commands: Use custom Django management commands as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Aliseyfi0841@gmail.com](mailto:Aliseyfi0841@gmail.com).
