===============
django-gravatar
===============

`django-gravatar` makes it easy to add Gravatar support to your Django
application through the addition of a template tag.


*******
History
*******

This code was taken from http://django-gravatar.googlecode.com, but it
was superseded by the https://github.com/ericflo/django-avatar package,
which provides a way more general approach to avatars in Django (not
Gravatar-specific, with local Django caching).

If, however, you want to stick to a Gravatar-only solution, this package
may a bit more "lightweight" and easier to start using.


************
Installation
************

To install it, use pip::

    pip install django-gravatar


*****
Usage
*****

To use it with a Django installation, first place 'gravatar' in the
``INSTALLED_APPS`` tuple of your settings.py file like so::

    INSTALLED_APPS = (
        # ...
        'gravatar',
    )

Here is sample usage in a template::

    {% load gravatar %}
    {% gravatar user 40 %}

In the previous example, a gravatar will be displayed for the specified
author at a size of 40 pixels square.  The second argument is optional and
if not supplied the gravatar image will be 80 pixels square, the default
gravatar image size.

In addition to supplying a user object, you can also provide a username as
a string.  For instance::

    {% gravatar 'jtauber' %}

Or by email::

    {% gravatar_img_for_email 'someone@example.com' %}

If you only want the URL and not the full blown ``img`-tag, you can use the
following functions::

    {% gravatar_for_user 'jtauber' %}
    {% gravatar_for_email 'someone@example.com' %}

There are a few configuration variables available that you can use in your
Django's ``settings.py``:

- **GRAVATAR_URL_PREFIX**: The gravatar URL to use.  Default:
  ``http://www.gravatar.com/``
- **GRAVATAR_DEFAULT_IMAGE**: The default image to use, see
  http://en.gravatar.com/site/implement/images/#default-image
- **GRAVATAR_IMG_CLASS**: The default CSS class name to add to generated
  ``<img>``-tags.
