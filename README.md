# maths Catalog
This is one of the projects of the [Full Stack Nanodegree on Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). Named in the course _**"Item Catalog"**_.

It runs a website called Book Catalog that contain suggestions of books (referred to them in the code as "items") in 6 categories.

The user can login via Google in order to add their own suggestions of books.

# Set up and run
Do the following instructions
## Install prerequisite
* [Python 2.7 or above](https://www.python.org/downloads/).
* Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
* Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
* Clone or download the Vagrant VM configuration file from [here](https://github.com/udacity/fullstack-nanodegree-vm)
* The following Python packages: 
  - flask
  - oauth2client
  - sqlalchemy
  - requests
 * You may need to install some other modules if the application threw module-not-found error. Do this by running `sudo pip install [module name]` inside vagrant.
## Run
* Clone the _**Vagrantfile**_ from Udacity [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repo.
* **From the terminal**, run `vagrant up` to run the virtual machine, then `vagrant ssh` to login to the VM.
* cd to the project directory.
* Setup the database by running `python database_setup.py`.
* Populate the database by running `python items.py`.
* Run `python app.py`.
* Go to http://localhost:5000/ to access the application.

### JSON endpoints
#### Returns JSON of all restaurants

```
/mathsCatalog/JSON
```
