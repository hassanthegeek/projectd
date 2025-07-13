/home/ubuntu/work/project_d/venv/bin/python /home/ubuntu/work/project_d/manage.py collectstatic --noinput
/home/ubuntu/work/project_d/venv/bin/python /home/ubuntu/work/project_d/manage.py migrate
/home/ubuntu/work/project_d/venv/bin/python -m gunicorn --chdir /home/ubuntu/work/project_d/ project_d.wsgi:application -b 0.0.0.0:8000