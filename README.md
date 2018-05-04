# Getting started with Python web development:
### Creating a portfolio/blog using Django web framework

I want to create my website using the Django web framework for Python. I will use this repository to document my process and share my code.

#### Goal:
`To create a python/django powered website capable of serving as my portfolio and blog. I will attempt to use binary (text) files on the local filesystem as the content repository (instead of using a traditional relational database like MySQL or MariaDB).`

#### Assumptions
```
This project assumes you are using a Mac OS X system with root/admin privileges.     
```

#### Package Versions:
> Python: 2.7     
> Django: 1.11.13     
> pytz: 2018.3     

---

## Quick start

This project is too early in it's lifecycle. There is no quick start yet.

## Prerequisites

You should have `Python` and  `Django` installed on your development machine.

I prefer to use the `brew install <package-name>` to install and maintain most components on my mac development environment. `brew` is short for `Homebrew`, a package manager for `Mac OS X` (similar to `yum` or `apt-get` on UNIX systems).

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

### Verify Python installation

Make sure you have python 2.7 installed. Use `python -V` to check.

### Brew update and clean up

```sh
brew update
brew upgrade
```

### Install Django web framework

Django is NOT included with `homebrew`. Therefore, we will use `pip` -- Python's package manager.   

> Depending on your setup, you might have multiple versions of `pip` installed. For example I have:

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

THIS SECTION IS NOT COMPLETE.     
_Unformatted dev notes -- will format this later._

#### Create a Django project
Use `django-admin.py startproject <project-name>` to initialize project:

```
django-admin.py startproject webdoraweb
```

#### Django and MVC
You are probably already familiar with the Model View Controller (MVC) framework. My understanding is that Django is pretty similar to MVC. **I will need to study the two architectures in more detail before I can extend this section.**



























## Deployment notes

```
This project is NOT deployment ready. Currently under active development.
```

## Credits

THIS SECTION IS NOT COMPLETE.

**Some resources I used:**
* https://github.com/prameya/webdora-d8
* https://code.tutsplus.com/articles/python-from-scratch-create-a-dynamic-website--net-22787
