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
    gravatar_url += urllib.urlencode({'s':str(size)})
    return """<img src="%s" alt="Avatar for %s" height="%s" width="%s"/>""" % (escape(gravatar_url), username, size, size)

register.simple_tag(gravatar)