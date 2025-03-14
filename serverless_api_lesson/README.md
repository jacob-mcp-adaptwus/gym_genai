
# Mathtilda API

![architecture](img/arch.png)

This project is an [Serverless](https://github.com/serverless/serverless) enabled project, Python, npm and the serverless ci/cd that will act am api portal
then uses various lambda function

## Getting Started

Make sure you are added as a user to the particular in the (AWS dev account) 



### Deployments

| [DEV](http://localhost:9527/)  | [STG] | [PRD]) |


### Prerequisites

download [node](https://nodejs.org/en/download/)


Install Python 3.  Note that the AWS python version for Lambdas is v3.12



### Installing

After all of the prerequisites are satisfied, clone the repo:

```
git clone 
cd spot-backend
```

This project expects the use of python3 virtual environments ..
(https://docs.python.org/3/library/venv.html).

```
# install node dependecies
npm install

# Initialize the virtual environment in bash
#Mac
pip install pipenv 

#windows
pip3 install pipenv


# Install the project specific depdencies into 
# the pipenv virtual environment

#Mac
pipenv install

#windows
pipenv install


###validate your env
pipenv shell

# When you are done, you can deactivate the environment by 
# explicitly deactiving it *OR* closing your terminal window.
# You will need to re-initialize the environment again.

pipenv exit
```


This is a serverless project, so there isn't anything to project-specific to install.  However, it
is sometimes useful during development to run locally vs going through a full 
commit->pull request->merge to master->create release cycle. The project is npm driven

## Running the tests

This project using pytest for testing.  Tests are found in the src/tests/* 
directory.  By convention, pytest looks for test_* (prefix) or *_test (suffix) 
files during discovery.  Follow python file naming conventions and use underscores ('_') 
between words.  If you use dashes in the test filename, the test will fail discovery.*

There is a make target test you can use to run the tests.

```
npm run test
```


### coding style tests

```
npm run lint
```


## Deployment
All build activity is visible via 


## Built With

* [Python](https://www.python.org/) - The code execution runtime language
* [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework
* [Serverless](https://github.com/serverless/serverless)- Open-source framework for building serverless applications

## Acknowledgments

* PurpleBooth for the awesome readme template: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
