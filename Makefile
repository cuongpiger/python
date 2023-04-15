normal-run:
	@uwsgi --wsgi-file app.py --http :5000

filed-run:
	@uwsgi --ini uwsgi.ini

debug-run:
	@python app.py