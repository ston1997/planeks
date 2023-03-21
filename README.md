- Online Service for Generating CSV Files with Fake (Dummy) Data

This is a web application built using Python and Django that generates CSV files with fake (dummy) data. It allows registered users to create data schemas with a specified number of columns and data types. Users can then generate datasets with a specified number of records for each schema.

- User Authentication

Users can log in to the system with their username and password. User registration can be done via the admin interface. The Django's built-in LoginView and LogoutView are used to implement user authentication.

- Creating Data Schemas

Any logged-in user can create data schemas with a name and a list of columns with names and specified data types. The application supports at least 5 different types of data:

- Full name (a combination of first name and last name)
- Job
- Email
- Domain name
- Phone number
- Company name
- Text (with a specified range for the number of sentences)
- Integer (with a specified range)
- Address
- Date

Users can build the data schema with any number of columns of any type described above. Some types support extra arguments (like a range), while others do not. Each column also has its own name (which will be a column header in the CSV file) and order (just a number to manage column order).

- Generating Datasets

After creating the schema, the user can input the number of records he/she needs to generate and press the “Generate data” button. After pressing the button, the frontend sends an AJAX request to the server to generate the data. When the CSV file of the specified structure is ready, the file is saved to the “media” directory. The interface shows a colored label of generation status for each dataset (processing/ready). Users can download the generated CSV file by clicking the "Download" button for the datasets that are available for download.

- Deployment

The application is deployed to PythonAnywhere and is available online at https://ston1997.pythonanywhere.com/. A test user is created for testing purposes, and the credentials can be provided upon request.

- URLs

The URLs for the application are defined in the urls.py file of the app. The following URLs are currently available:

- '': The homepage of the application. Users need to log in to access this page.
- 'generate_data/<int:id>/': This URL is used to generate the data for a specific schema with the given id.
- 'schemas/<int:pk>/': This URL shows the details of a schema with the given pk.
- 'create/': This URL is used to create a new schema.
- 'list/': This URL shows the list of all schemas created by the logged-in user.
- 'edit/<int:pk>/': This URL is used to edit an existing schema with the given pk.
- 'delete/<int:pk>/': This URL is used to delete an existing schema with the given pk.
- 'login/': This URL is used for user login.
- 'logout/': This URL is used for user logout.

The 'login_required' decorator is used to restrict access to certain pages to only logged-in users.