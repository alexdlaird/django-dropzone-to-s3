Django Dropzone to S3
=====================

A simple Django application that file uploads directly to an Amazon S3 bucket.

# Basic Deployment
The following deployment setup is only meant as an example for those wishing to quickly deploy this application to a web server without necessarily understanding the code.

You'll need the following installed before cloning the source code:
- [Python 2.7](https://www.python.org/downloads/)
- [PyCrypto](https://www.dlitz.net/software/pycrypto/) (if you're on Windows, look at [these installers](http://www.voidspace.org.uk/python/modules.shtml#pycrypto))
- [PIP](http://pip.readthedocs.org/en/latest/installing.html)

You'll need to setup the following [Amazon Web Services (AWS)](http://aws.amazon.com/):
- [Launch an EC2 instance](http://aws.amazon.com/ec2) running Ubuntu Server (or some other Debian-based operating system)
- Save the .pem key pair file for the EC2 instance as ~/.ssh/myserver.pem
- Create an EC2 Security Group that has port 80 opened
- [Create an S3 bucket](http://aws.amazon.com/s3/).
- Generate an AWS Access Key and Secret Access Key
- (Optional) Create an elastic IP and associate it with the EC2 instace you created
- (Optional) Create a DNS entry of your choosing to point to the elastic IP (AWS will generate their own DNS entry that you can also use, if you don't have your own domain name)

Now you're ready to checkout, configure, and deploy the code to your EC2 server.

- Fork the repository on GitHub
- Clone your forked repository
- Modify the variables at the bottom of djangodropzonetos3/settings.py to customize the application
- You must specify valid values for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_STORAGE_BUCKET_NAME in settings.py
- Modify the HOSTNAME variables at the top of fabfile.py to point to your EC2 instance's DNS entry
- Modify the REPO_URL variable at the top of fabfile.py to point to your fork of the repository
- From the Command Line at the root of the cloned source, execute "pip install -r reqs.txt"
- From the Command Line at the root of the cloned source, execute "fab deploy"
