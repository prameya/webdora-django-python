# Getting started with Python web development:
### Creating a Django powered portfolio/blog using local filesystem (binary/text/blob) as content repository (not using RDB like MySQL or MariaDB).

I will use this repository to document my process and share my code.

#### Assumptions
```
This project assumes you are using a Mac OS X system with root/admin privileges.     
```

#### Package Versions
> Python: 2.7     
> Django: 1.11.13     
> pytz: 2018.3     

---

## Quick start

This project is too early in it's lifecycle. There is no quick start yet.

## Prerequisites

You should have `Python` and  `Django` installed on your development machine.

I prefer to use the `brew install <package-name>` command to install and maintain most components on my mac development environment. `brew` is short for `Homebrew`, a package manager for `Mac OS X` (similar to `yum` or `apt-get` on UNIX systems).

Prepare your machine for development:

### Install XCode CLI tools

```sh
xcode-select --install
```

### Install Homebrew

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

To make sure brew was installed use `brew --version`. To be safe, let's run `brew doctor`.

### Brew update and clean up

```sh
brew update
brew upgrade
```

### Verify Python installation

Make sure you have python 2.7 installed. Use `python -V` to check. To install python:

```sh
brew install python@2
```

### Install Django web framework

Django is NOT included with `homebrew`. Therefore, we will use `pip` -- Python's package manager.   

Depending on your setup, you might have multiple versions of `pip` installed. I have:

```sh
$ pip --version
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

$ pip2 --version
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

$ pip3 --version
pip 10.0.1 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
```

Let's use `pip2` to install Django for `python v2.7`:

```sh
pip2 install django
```

THIS SECTION IS NOT COMPLETE.

## How I did it

Below I will outline how I created this project. I will cite sources and document my process for anyone that might be interested.

#### Django and MVC
You are probably already familiar with the Model View Controller (MVC) framework. My understanding is that Django is pretty similar to MVC. **I will need to study the two architectures in more detail before I can extend this section.**

THIS SECTION IS NOT COMPLETE.     
_Unformatted dev notes -- will format this later._

#### Create Django project
Use `django-admin.py startproject` to initialize the project:

```sh
django-admin.py startproject webdoraweb
```

#### Initialize blog app
```sh
python manage.py startapp blog
```

























## Deployment notes

```
This project is NOT deployment ready. Currently under active development.
```

## Credits

THIS SECTION IS NOT COMPLETE.

**Some resources I used:**
* https://github.com/prameya/webdora-d8
* https://docs.djangoproject.com/en/1.7/intro/tutorial01/
* https://code.tutsplus.com/articles/python-from-scratch-create-a-dynamic-website--net-22787
