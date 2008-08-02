from django import template
from django.utils.html import escape
from django.contrib.auth.models import User
from django.conf import settings

import urllib, hashlib

GRAVATAR_URL_PREFIX = getattr(settings, "GRAVATAR_URL_PREFIX", "http://www.gravatar.com/")

register = template.Library()

def gravatar(user, size=80):
    if not isinstance(user, User):
        try:
            user = User.objects.get(username=user)
            email = user.email
            username = user.username
        except User.DoesNotExist:
            email = "?"
            username = user
    else:
        email = user.email
        username = user.username
        
    gravatar_url = "%savatar/%s/?" % (GRAVATAR_URL_PREFIX, hashlib.md5(email).hexdigest())
    query_args = {'s':str(size)}
    if GRAVATAR_URL_PREFIX != "http://www.gravatar.com/":
        default = "http://www.gravatar.com/avatar/%s/?" % hashlib.md5(email).hexdigest()
        default += urllib.urlencode({'s': str(size)})
        query_args['d'] = default
    gravatar_url += urllib.urlencode(query_args)
    return """<img src="%s" alt="Avatar for %s" />""" % (escape(gravatar_url), username)

register.simple_tag(gravatar)