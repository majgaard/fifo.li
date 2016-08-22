fifo.li
==============================

fifo.li is a Django based queueing app built for the 2016 Colby College Hackathon.

By leveraging an existing RFID system built into student ID cards, fifo.li allows
users to instantly join any queue of their choosing (TA assistance,
Professorial assistance during office hours, Tech Helpdesk) by simply tapping
their Student ID at a public fifo.li dashboard (or by logging in on their device).

Users are shown who is available to help, what their subjects of expertise are,
and how many people are in line. Driven by statistics, the system also lets
users see approximately how long they have to wait before a given host can
help them.

Queue hosts are empowered with a powerful dashboard which lets them keep track
of who is next as well as log statistics about their sessions and info about
particular users. These statistics also help supervisors/employers see who isn't
pulling their weight, or who might need a little more help.



LICENSE: MIT


Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Installing OS & Python Dependencies
^^^^^^^^^^^^^^^^^^^^^
Clone this repo in your private C9 workspace::

    git clone https://github.com/username/repo.git

Or clone a specific branch::

    git clone -b <branch_name> https://github.com/username/repo.git

Install OS dependencies first::

    sudo ./install_os_dependencies.sh install

Create a virtual environment::

    virtualenv <env_name>

Activate the virtual environment::

    source /path/to/<env_name>/bin/activate

Install Python dependencies::

    ./install_python_dependencies.sh

Deactivate the virtual environment::

    deactivate



Activate PostgresSQL
^^^^^^^^^^^^^^^^^^^^^
Start the service (Ubuntu)::

    sudo service postgresql start

Access the shell (Ubuntu)::

    sudo sudo -u postgres psql

Create a new user::

    CREATE USER fifouser WITH PASSWORD '7xkKBfRbkMg9dk';

Create a new database::

    CREATE DATABASE fifodb;

Grant a privileges::

    GRANT ALL PRIVILEGES ON DATABASE fifodb to fifouser;

Show Databases::

    \list

Quit::

    \q

Drop a new database::

    DROP DATABASE fifodb;

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html








Deployment
----------





Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html
