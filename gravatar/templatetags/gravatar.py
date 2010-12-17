import urllib

from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.hashcompat import md5_constructor
from django.utils.html import escape

GRAVATAR_URL_PREFIX     = getattr(settings, "GRAVATAR_URL_PREFIX", "http://www.gravatar.com/avatar/")
GRAVATAR_DEFAULT_IMAGE  = getattr(settings, "GRAVATAR_DEFAULT_IMAGE", "")
GRAVATAR_DEFAULT_RATING = getattr(settings, "GRAVATAR_DEFAULT_RATING", "g")
GRAVATAR_DEFAULT_SIZE   = getattr(settings, "GRAVATAR_DEFAULT_SIZE", 80)
GRAVATAR_IMG_CLASS      = getattr(settings, "GRAVATAR_IMG_CLASS", "gravatar")

register = template.Library()

def _imgclass_attr():
    if GRAVATAR_IMG_CLASS:
        return ' class="%s"' % (GRAVATAR_IMG_CLASS,)
    return ''

def _wrap_img_tag(url, info, size):
    return """<img src="%s"%s alt="Avatar for %s" height="%s" width="%s"/>""" % \ 
            (escape(url), _imgclass_attr(), info, size, size)

def _get_user(user):
    if not isinstance(user, User):
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            raise Exception, "Bad user for gravatar."
    return user

@register.simple_tag
def gravatar_for_email(email, size=None, rating=None):
	"""
	Generates a Gravatar URL for the given email address.

	Syntax::

		{% gravatar_for_email <email> [size] [rating] %}
	
	Example::

		{% gravatar_for_email someone@example.com 48 pg %}
	"""
	gravatar_id = md5_constructor(email).hexdigest()
    gravatar_url = GRAVATAR_URL_PREFIX + gravatar_id
	
	parameters = [p for p in (
		('d', GRAVATAR_DEFAULT_IMAGE),
		('s', size or GRAVATAR_DEFAULT_SIZE),
		('r', rating or GRAVATAR_DEFAULT_RATING),
	) if p[1]]

	if parameters:
    	gravatar_url += '?' + urllib.urlencode(parameters, doseq=True)

    return escape(url)

@register.simple_tag
def gravatar_for_user(user, size=None, rating=None):
	"""
	Generates a Gravatar URL for the given user object or username.

	Syntax::

		{% gravatar_for_user <user> [size] [rating] %}
	
	Example::

		{% gravatar_for_user request.user 48 pg %}
		{% gravatar_for_user 'jtauber' 48 pg %}
	"""
    user = _get_user(user)
    return gravatar_for_email(user.email, size, rating)

@register.simple_tag
def gravatar_img_for_email(email, size=None, rating=None):
	"""
	Generates a Gravatar img for the given email address.

	Syntax::

		{% gravatar_img_for_email <email> [size] [rating] %}
	
	Example::

		{% gravatar_img_for_email someone@example.com 48 pg %}
	"""
    url = gravatar_for_email(email, size, rating)
    return _wrap_img_tag(url, email, size)

@register.simple_tag
def gravatar_img_for_user(user, size=None, rating=None):
	"""
	Generates a Gravatar img for the given user object or username.

	Syntax::

		{% gravatar_img_for_user <user> [size] [rating] %}
	
	Example::

		{% gravatar_img_for_user request.user 48 pg %}
		{% gravatar_img_for_user 'jtauber' 48 pg %}
	"""
    url = gravatar_for_user(user, size, rating)
    return _wrap_img_tag(url, user.username, size)

