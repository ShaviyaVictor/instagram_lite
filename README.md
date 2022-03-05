# Instagram Lite

This is a clone of Instagram where people share their images and videos for other users to view. Users can sign up, login, view and post photos, search and follow other users.     
Below is the project's screenshot:     
![Instagram_Lite_Screenshot](#)


#### Live link to site
The project was deployed to Heroku and GitHub pages for publication.     
* To view the [project's Heroku live site](#).         
* To view the [project's Figma mockup design](https://www.figma.com/file/AG9vo9vvA4n4UvvpuWSFR6/Instagram-clone?node-id=0%3A1).

## Application Setup Instructions
- Open Terminal {Ctrl+Alt+T}     
- git clone [instagram_project](#)      
- cd instagram_project      
- code . or atom . based on the text editor you have.


### Running the application

To run the application locally, open the cloned file in terminal and run the following commands:     
  > `$ python manage.py runserver`  

### Installing

Below is a step by step series of how to work on the project after cloning it:

Navigate into the folder and install requirements by running the below command:

```
$ cd instagram_project pip install -r requirements.txt 
```

Create a new directory and inside it create a new environment(virtual) by running the below command:

```
$ python3 -m venv --without-pip virtual
```

Activate the virtual environment:

```
$ source virtual/bin/activate
```

View the **cloned project** and continue editting or follow the below commands to build your own Django application.

Install pip in the virtual environment for installing additional packages for the project:

```
$ curl https://bootstrap.pypa.io/get-pip.py | python
```

Use pip to install Django inside your vrtual environment:

```
$ pip install django
```

SetUp your database User,Password, Host then make migration:

```
$ python manage.py makemigrations instagram_project
```

Make migrations:

```
$ python manage.py migrate 
```



## Running the tests

Below is a command for running the TestCases of the application:      
  > `$ python3 manager.py test`


Open the application on your browser:
```
127.0.0.1:8000
```



## Deployment

Follow along with this [Deployment Documentation](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0) to deploy your version of the application to Heroku.

## Built With

* [Python](https://docs.python.org/3/)        
* [Django](https://docs.djangoproject.com/en/4.0/)       
* [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)       
* [Heroku](https://devcenter.heroku.com/categories/reference)       


## Authors

* **Victor Shaviya** - *On LinkedIn as* - [ShaviyaVictor](https://www.linkedin.com/in/victor-shaviya-532ab0110/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ShaviyaVictor/instagram_lite/blob/main/LICENSE) file for details.

## Acknowledgments

* Corey Schafer
* Pretty Printed
* Inspiration by Instagram
