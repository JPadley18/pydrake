===============
Getting Started
===============

To get started with PyDrake, you will need to register for an API key.

API Keys
--------
There are three types of API keys available from Riot:

`Development Key <https://developer.riotgames.com/>`_
  These keys are generally used for testing API endpoints or libraries (like this one).
  They must be regenerated every 24 hours and have a heavy rate limit of 10 requests per
  second and up to 100 per 2 minutes.
`Personal Projcet Key <https://developer.riotgames.com/app-type>`_
  These keys never expire, but require an application to Riot in order to obtain one.
  They are also subject to the same rate limiting as Development Keys.
`Application Project Key <https://developer.riotgames.com/app-type>`_
  These keys also never expire, but require an application along with a functional
  prototype in order to obtain one. However, these keys have much more relaxed rate
  limits, allowing you to handle the large amount of traffic a production app would create.

You can click any of the above titles to see where you can apply for each of the keys.

Installing PyDrake
------------------
To install the latest version of PyDrake, simply run:

.. code::

	pip install pydrake

Creating an API Instance
------------------------
Now in order to access Riot's API, all you have to do is create a ``PyDrake`` object.

.. code:: python

	from pydrake import PyDrake

	api = PyDrake("my_api_key")