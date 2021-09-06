#Flaskapp
This project will post the data into csv files users.csv and locations.csv. Before it is posting it will verify that data is present or not. If data is already existing It will raise an error(If same data already present It will allow but while doing changes it wont allow multiple updations)
Please follow below steps to run this application
Pre-requesites: Machine should contain docker and should be enabled.
Please create a flask_app folder and place the files list given[Dockerfile,requirements.txt,users.csv,locations.csv,test_user_location.py,flask_api.py] inside your machine ex: /home/praveen/flask_app
Now go to inside flask_app(Please go via terminal). Now you can see a Dockerfile and users.csv and location.csv and test_users_locations.py,requirements.txt files
Now please run this docker command :   **sudo docker build -t <flask_app> . (you can give the name you want, . is mandatory. please copy properly)**
The above step will build a docker image. Now your flask server is dockerised and it is available to take requests.
We have one more file test_user_locations.py where test cases +ve and -ve written (For now I gave 4 tests 3 for post 1 for Put)
Now we need to run docker .Please use below command.
**sudo **docker run -d -p 80:5000 flask_app**** (Running docker and mapping 5000 port to 80).
Now your docker container is avilable on port 80
Inside test_user_locations.py file urls were given to send POST ans PUT requests over port no 80
Now in another terminal you can run this pytest file  pytest test_user_locations.py
Now you can see in the console test were passed and failed. It means that you are able send requests flask from pytest(with already written test cases).
Please check users.csv and locations.csv file .The data will be updated when you run the above test
If you want detailed report in browser format,Plese run this command pytest -sv --html report.html
All tests will run asynchronously since requirement is to send requests in async mode. Please look into test_user_location.py file for async implementation

