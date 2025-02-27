cd /home/pi/InfoHub-BackendDC
gunicorn app:app -w 3 --threads 2 -b 0.0.0.0:5000