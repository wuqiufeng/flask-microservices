FROM python:3.6-alpine


#ENV UWSGI_INI /app/uwsgi.ini
#ENV PYTHONPATH=/app

# 设置工作目录
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


#COPY ./app /app
#WORKDIR /app


ADD . /usr/src/app
#RUN /bin/sh -c pip install uwsgi
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#RUN chmod +x ./start.sh
# 运行服务
CMD [ "python", "run.py" ]
#CMD ["./start.sh"]
