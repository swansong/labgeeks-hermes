"""
update_permissions is a management command that creates
any new permissions and content types
in the database for use
"""
from django.core.management.base import BaseCommand, CommandError
from django.core.management import setup_environ
from django.contrib.contenttypes.management import update_all_contenttypes
from django.contrib.auth.management import create_permissions
from django.db.models import get_apps

class Command(BaseCommand):
    args = ''
    help = 'Updates custom content-types and permissions in South-managed apps'

    def handle(self, *args, **options):
	try:
	    import labgeeks.settings
	except ImportError:
	    import sys
	    sys.stderr.write("Couldn't find the settings.py module.")
	    sys.exit(1)

	setup_environ(labgeeks.settings)

	# Add any missing content types
	update_all_contenttypes()

	# Add any missing permissions
	for app in get_apps():
	   create_permissions(app, None, 2)
