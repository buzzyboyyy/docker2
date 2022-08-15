Here is my example of a python flask API call!

1. First thing you're going to want to do is create a youtube API key by going to 

https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=youtube-api-357100&supportedpurview=project

and sign in with a google account.

2. Click "Enable" to enable the Youtube Data API v3 API on your account that will allow us to create a "project" and access an API for our demo

3. Once you're into your Google Cloud project, you can click "credentials" and then "Create Credentials" at the top to generate an API key that will stay active for 30 days. Copy this and save it for later.

4. Create a .env file with an editor of your choice to pass our API environmental variable to our main project
Use the syntax API_KEY=PlaceAPIkeyhere.
Save the file in the root folder of your project with the rest of our files

5. cd to the root folder of our project in a terminal and run docker build -t PythonFlaskImage .
this will create a docker image with the name PythonFlaskImage

6. run docker run -d -p 5000:5000 PythonFlaskImage to run our project on port 5000 in detached mode
by going to http://127.0.0.1:5000/ you should be able to access the home page
WELCOME TO THE THUNDERDOME

7. http://127.0.0.1:5000/youtube should show us the top viewed youtube video of the day if our youtube API call worked correctly
you can run a curl http://127.0.0.1:5000/health for some web status details in a split terminal
/name will grab the /value and display Hello "name"!

8. Congrats on running my flask python program :D