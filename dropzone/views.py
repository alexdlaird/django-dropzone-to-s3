import time
import json

from boto.exception import S3ResponseError
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from boto.s3.connection import S3Connection
from boto.s3.key import Key


def home(request):
    response = render_to_response('home.html', {'SITE_TITLE': settings.SITE_TITLE, 'host': request.get_host()},
                                  context_instance=RequestContext(request))

    return response


def get_settings(request):
    # This function allows the client-side JavaScript to ask the server what file types it allows for uploads
    response = HttpResponse(json.dumps(
        {'ALLOWED_FILE_MIME_TYPES': settings.ALLOWED_FILE_MIME_TYPES, 'ANNONYMOUS_UPLOADS': settings.ANNONYMOUS_UPLOADS,
         'CONTACT_EMAIL': settings.CONTACT_EMAIL}))

    return response


def check_shared_key(request):
    # Check if the given shared key matches the server
    if request.method == 'POST' and 'shared_key' in request.POST and request.POST['shared_key'] == settings.SHARED_KEY:
        response = HttpResponse()
    else:
        response = HttpResponseBadRequest('Invalid shared key.')

    return response


def upload(request):
    # Only allow access to this view if we're posting
    if request.method == 'POST' and len(request.FILES) > 0:
        file = request.FILES['file']
        # Ensure we have a valid file type
        if request.FILES['file'].content_type in settings.ALLOWED_FILE_MIME_TYPES:
            # Check if we're allowing annonymous uploads, otherwise ensure the give shared password is correct
            if settings.ANNONYMOUS_UPLOADS or (
                            'shared_key' in request.POST and request.POST['shared_key'] == settings.SHARED_KEY):
                try:
                    # Looks like we're good, so connect to the S3 bucket and upload the file (which is currently stored in memory)
                    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
                    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
                    k = Key(bucket)
                    k.key = settings.MEDIA_ROOT + str(int(time.time())) + '_' + str(file)
                    k.set_contents_from_file(file)

                    response = HttpResponse()
                except S3ResponseError:
                    response = HttpResponseBadRequest('Could not connect to the Amazon S3 upload server.')
            else:
                response = HttpResponseBadRequest(
                    'Incorrect password. Contact ' + settings.CONTACT_EMAIL + ' and ask for the shared key.')
        else:
            response = HttpResponseBadRequest('Sorry, valid file types are: ' + str(settings.ALLOWED_FILE_MIME_TYPES))
    else:
        response = HttpResponseBadRequest('This view is only accessible via a POST request.')

    return response