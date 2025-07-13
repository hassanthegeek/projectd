/home/ubuntu/work/projectd/venv/bin/python /home/ubuntu/work/projectd/manage.py collectstatic --noinput
/home/ubuntu/work/projectd/venv/bin/python /home/ubuntu/work/projectd/manage.py migrate
/home/ubuntu/work/projectd/venv/bin/python -m gunicorn --chdir /home/ubuntu/work/projectd/ project_d.wsgi:application -b 127.0.0.1:8000