import pip
import subprocess


'''
@author: Bilal Ahmad
@description: I created this tool to make the dev of py based projects easier.
@requirements: requires fabric, fabric-virtualenv, (maybe) paramiko=1.15.2
'''


def subprocess_cmd(cmd):
    """
        Runs a local command on the os e.g. cd ~/Desktop
    """
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()


def get_os_distributions():
    """
        Retrieves list of installed packages (pip)
    """
    installed_dist = pip.get_installed_distributions()
    flat_installed_dist = [dist.project_name for dist in installed_dist]
    return flat_installed_dist



def check_fab_requirements():
    """
        Checks requirements for fabric and fabric virtualenv
    """
    dists = ''
    try:
        dists = get_os_distributions()
    except ImportError:
        print "Check if pip is installed"
        raise

    try:
        if not 'Fabric' in dists or not 'fab' in dists:
            subprocess_cmd('pip install fabric')

        if not 'fabric-virtualenv':
            subprocess_cmd('pip install fabric-virtualenv')
    except OSError:
        print "Print could not install fabric and fabric-virtualenv"
        raise



import os.path
import getpass
from fabric.api import *

try:
    import psycopg2
except:
    subprocess_cmd("sudo pip install psycopg2")

try:
    from fabvenv import virtualenv
except:
    subprocess_cmd("sudo pip install fabric-virtualenv")


home = os.path.expanduser('~')
user = getpass.getuser()

virtualenv_dir_name = 'workspace'
virtualenv_dir = os.path.join(home, virtualenv_dir_name)

virtualenv_name = 'env_fifo'
virtualenv_path = os.path.join(virtualenv_dir, virtualenv_name)

#github info
git_addr = 'https://github.com/username/fifo.li.git'
git_branch = 'master'

#db info
db_name = 'fifodb'
db_user = 'fifouser'
db_password = ''
db_host = '127.0.0.1'
db_port = '5432'


#django project info
project_root = os.path.dirname(os.path.abspath(__file__))
manage_path = os.path.join(project_root, 'manage.py')

env.hosts = ['user@localhost']

# local command
def local_command(cmd):
    local(cmd)


# virtual_env command
def env_command(cmd, env):
    with virtualenv(env):
        local(cmd)


def create_virtualenv(dir=virtualenv_dir, name=virtualenv_name):
    """
    Creates virtualenv directory if it does not exist
    Then creates the virtualenv
    :param name: name of virtualenv
    :return: None
    """


    # try create virtualenv directory
    try:
        os.makedirs(dir)
    except OSError:
        if not os.path.isdir(dir):
            print "The directory is a file, please rename that or change this."
            raise

    path = os.path.join(dir, name)
    if not os.path.isfile(path):
        local_command('virtualenv '+path)



def set_db():
    conn = psycopg2.connect(database=db_name, user=db_user)
    cur  = conn.cursor()


def install_postgresql():
    local_command('brew install postgresql')
    local_command('export PATH="/usr/local/Cellar/postgresql/9.4.4/bin:$PATH"')


def install_requirements(name='local.txt'):
    env_command('pip isntall -r requirements/'+name)


def create_db(name='fifodb'):
    local_command('createdb name')


########### git ###########

# git clone
def git_clone(branch=git_branch, folder=git_branch):
    local_command('git clone -b '+branch+' '+git_addr+' '+remote_home+'/'+folder)

# git add
def git_add():
    local_command('git add -A')

# git commit
def git_commit(msg):
    local_command('git commit -am '+msg)

# git status
def git_status():
    local_command('git status')

# git new branch
def git_branchout(branch="new_branch"):
    local_command('git branch '+branch+'')
    local_command('git checkout '+branch+'')
    local_command('git branch')

# git merge
def git_merge(branch="new_branch"):
    local_command('git checkout master')
    local_command('git merge '+branch)

# git pull
def git_pull():
    local_command('git pull')

def server(c9=True, ip='127.0.0.1', port='8000'):
    if c9:
        print "https://<workspace>-<username>.c9users.io/"
    
    if c9:
        local_command('python manage.py runserver_plus 0.0.0.0:8080')
    else:
        local_command('python manage.py runserver_plus '+ip+':'+port)

def migrate():
    local_command('python manage.py migrate')

def collectstatic():
    local_command('python manage.py collectstatic')

def startapp(name, path='fifo/'):
    app_path = project_root+'/'+path+name
    try:
        local_command('mkdir '+app_path)
        local_command('python manage.py startapp '+name+' '+app_path)
        local_command('cp '+project_root+'/app_templates/* '+app_path+'/')
    except:
        print "Could not create app "+name










"""
PostgreSQL users and databases
==============================

This module provides tools for creating PostgreSQL users and databases.

"""

from fabric.api import cd, hide, sudo, settings


def _run_as_pg(command):
    """
    Run command as 'postgres' user
    """
    with cd('~postgres'):
        return sudo(command, user='postgres')


def user_exists(name):
    """
    Check if a PostgreSQL user exists.
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = _run_as_pg('''psql -t -A -c "SELECT COUNT(*) FROM pg_user WHERE usename = '%(name)s';"''' % locals())
    return (res == "1")


def create_user(name, password, superuser=False, createdb=False,
                createrole=False, inherit=True, login=True,
                connection_limit=None, encrypted_password=False):
    """
    Create a PostgreSQL user.

    Example::

        import fabtools

        # Create DB user if it does not exist
        if not fabtools.postgres.user_exists('dbuser'):
            fabtools.postgres.create_user('dbuser', password='somerandomstring')

        # Create DB user with custom options
        fabtools.postgres.create_user('dbuser2', password='s3cr3t',
            createdb=True, createrole=True, connection_limit=20)

    """
    options = [
        'SUPERUSER' if superuser else 'NOSUPERUSER',
        'CREATEDB' if createdb else 'NOCREATEDB',
        'CREATEROLE' if createrole else 'NOCREATEROLE',
        'INHERIT' if inherit else 'NOINHERIT',
        'LOGIN' if login else 'NOLOGIN',
    ]
    if connection_limit is not None:
        options.append('CONNECTION LIMIT %d' % connection_limit)
    password_type = 'ENCRYPTED' if encrypted_password else 'UNENCRYPTED'
    options.append("%s PASSWORD '%s'" % (password_type, password))
    options = ' '.join(options)
    _run_as_pg('''psql -c "CREATE USER %(name)s %(options)s;"''' % locals())


def drop_user(name):
    """
    Drop a PostgreSQL user.

    Example::

        import fabtools

        # Remove DB user if it exists
        if fabtools.postgres.user_exists('dbuser'):
            fabtools.postgres.drop_user('dbuser')

    """
    _run_as_pg('''psql -c "DROP USER %(name)s;"''' % locals())


def database_exists(name):
    """
    Check if a PostgreSQL database exists.
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        return _run_as_pg('''psql -d %(name)s -c ""''' % locals()).succeeded


def create_database(name, owner, template='template0', encoding='UTF8',
                    locale='en_US.UTF-8'):
    """
    Create a PostgreSQL database.

    Example::

        import fabtools

        # Create DB if it does not exist
        if not fabtools.postgres.database_exists('myapp'):
            fabtools.postgres.create_database('myapp', owner='dbuser')

    """
    _run_as_pg('''createdb --owner %(owner)s --template %(template)s \
                  --encoding=%(encoding)s --lc-ctype=%(locale)s \
                  --lc-collate=%(locale)s %(name)s''' % locals())


def drop_database(name):
    """
    Delete a PostgreSQL database.

    Example::

        import fabtools

        # Remove DB if it exists
        if fabtools.postgres.database_exists('myapp'):
            fabtools.postgres.drop_database('myapp')

    """
    _run_as_pg('''dropdb %(name)s''' % locals())
