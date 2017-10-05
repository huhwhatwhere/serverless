# Serverless using Zappa

Using Zappa (Serverless Python Framework) to build a static website

Dependencies
------------
* Homebrew (OSX)
* Python 2.7
* Python Pip
* Python Virtualenv
* awscli
* AWS account

Setup
-----
##### Base install

The assumption is that an Apple Mac will be used to run this proof of concept.
Install HomeBrew
- https://brew.sh/

Install Python 2.7 and pip
- brew install python

Install virtualenv
- pip install virtualenv

Install awscli
- brew install awscli

Clone the respository and change directory so that you're in the "serverless" folder from there create a virtualenv
- virtualenv env
- cd ansible
- source ../env/bin/activate

Once created, install requirements.txt
- pip install -r ../requirements.txt

## Running the anisble Playbook
- ansible-playbook -i inv abz.yml -vv
