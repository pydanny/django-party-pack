# Some helpful utility commands.
# TODO - maybe convert to Fabric scripts

deploy:
	heroku pgbackups:capture --expire
	git push heroku master
	heroku run python {{ project_name }}/manage.py syncdb --noinput  --settings={{ project_name }}.settings.heroku
	heroku run python {{ project_name }}/manage.py migrate --settings={{ project_name }}.settings.heroku

style:
	git push heroku master
	heroku run python {{ project_name }}/manage.py collectstatic --noinput --settings={{ project_name }}.settings.heroku

restorepgsql:
	heroku pgbackups:capture --expire
	curl -o latest.dump `heroku pgbackups:url`
	dropdb {{ project_name }}
	createdb {{ project_name }}
	pg_restore --verbose --clean --no-acl --no-owner -d {{ project_name }} latest.dump
