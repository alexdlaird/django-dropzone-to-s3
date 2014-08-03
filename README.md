Django Dropzone to S3
=====================

A simple Django application that file uploads directly to an Amazon S3 bucket.

# Basic Deployment
The following deployment setup is only meant as an example for those wishing to quickly deploy this application to a web server without necessarily understanding the code.

You'll need the following installed before cloning the source code:
x Python 2.7
x [PyCrypto](https://www.dlitz.net/software/pycrypto/)
x [PIP](http://pip.readthedocs.org/en/latest/installing.html)

You'll need to setup the following Amazon Web Services (AWS):
x Launch an EC2 instance running Ubuntu Server (or some other Debian-based operating system)
x Save the .pem key pair file for the EC2 instance as ~/.ssh/myserver.pem
x Create an EC2 Security Group that has port 80 opened
x Create an S3 bucket and make note of its name.
x Generate an AWS Access Key and Secret Access Key
x (Optional) An elastic IP associated with the VM
x (Optional) A DNS entry pointing to the elastic IP address

Now you're ready to checkout and deploy the code to your server.

- Clone the source code
- Modify the variables at the bottom of djangodropzonetos3/settings.py to customize the application
- You must specify valid values for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_STORAGE_BUCKET_NAME in settings.py
- From the Command Line at the root of the cloned source, execute "pip install -r reqs.txt"
- From the Command Line at the root of the cloned source, execute "fab deploy"

# More Information
If you're looking for a more detailed tutorial on the code and deployment options, check out the full tutorial found here: http://www.alexlaird.com/2014/08/django-dropzone-uploader