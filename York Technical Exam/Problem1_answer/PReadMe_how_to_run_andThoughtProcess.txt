Hello

This file has information on how to run this solution as well as my thought process.

Here is how to run this soulution.
======================================
we start by running the backend:
1.Navigate to the "Django Backend" folder
2. Activate the virtual environment, by running this command "myenv\Scripts\activate"
3.Navigate to this folder "LogViewer". it is inside the "Django Backend" folder.
4. run the following command "python manage.py runserver"
5.keep the terminal open....

We are going to run the from end, 
1.open another terminal
2.navigate to the "React_front_end/my-app" folder.
3. run the following command "npm start"

Here are a few API calls example that you can try in postman if you want to test the back end
1.for uploading the file: http://127.0.0.1:8000/log (post request, and upload the file in the body)
2.for general reading of data in the database: http://127.0.0.1:8000/log (get request)
3.for sorting by LOG_PRODUCER: http://127.0.0.1:8000/logByProducer/database (get request)
4.for sorting by LOG_SEVERITY:http://127.0.0.1:8000/logBySeverity/2 (get request)
5.for sorting by TIMESTAMP: http://127.0.0.1:8000/logByDate/2020-01-17 02:37:41/2020-01-17 02:37:45 (get request)

About the project:

Answering the question: Written description describing your approach to the problem statement.
===============================================================================================
The backend is develloped in Django. and front end is develloped using ReactJs
1. When I saw that we are going to be dealing with files and showing information to the user, I choose to two different applications
so we can have one for the front end and another for the back end. It is much easier to mantain the code this way.
I wanted to first make sure that the back end works perfecty and be able to debug it on its own. 
And the front end is basically independant as well, I was able to make sure that it works perfectly before linking the database to it.
and if needed more than one person can work on the solution, with everyone having total freedom and accountability.

2.I choose python because it is relatively easy to work with, can run on multiple platforms and its code is very understandable
if you are going to share it with others as it looks more like english.


3. I choose React for the front end because it is fast.(helps you put together a decent webpage quickly)



