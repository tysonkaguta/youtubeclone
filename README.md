**Youtube Clone**

A video viewiwng app experiment

**To setup your EC2**
sudo apt-get update

**Step 1: Clone the Repository**
Open your terminal or command prompt.

Change to the directory where you want to clone the Youtube Clone app. For example: cd youtubeclone-django

Clone the repository by running the following command:

git clone https://github.com/tysonkaguta/youtubeclone

**Step 2: Install Dependencies**
Once the repository is cloned, change to the app's directory:
cd youtubeclone-django

**Step 3: Install Dependencies**
Install the required Python packages from the 'requirements.txt' file:
pip install -r requirements.txt

**Step 4: Set Up the Database**
Apply the database migrations to create the necessary database schema:
python manage.py migrate

**Step 5: Create a Superuser (Optional but Recommended)**
Creating a superuser allows you to access the Django admin interface and manage the app's data.

Create a superuser by running: python manage.py createsuperuser

Follow the prompts to set a username, email, and password for the superuser.

**Step 6: Run the Development Server**
Start the development server by running: python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/. You should see the Youtube Clone app's homepage.

**Step 7: Access the Admin Interface (Optional)**
To access the Django admin interface, go to http://127.0.0.1:8000/admin/.

Congratulations! You've successfully cloned and run the Youtube Clone Django app on your local machine. You can now explore and interact with the app using your web browser. Enjoy viewing videos on the app!
