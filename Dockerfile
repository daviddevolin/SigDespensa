FROM python

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# create the necessary folders
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/SigDespensa
RUN mkdir -p /opt/app/SigDespensa/sig-despensa

# copy source
COPY sig-despensa/requirements.txt /opt/app/SigDespensa/
COPY start-server.sh /opt/app/SigDespensa/
COPY sig-despensa /opt/app/SigDespensa/sig-despensa

RUN touch /opt/app/SigDespensa/sig-despensa/.env
RUN echo "DEBUG_STATE=False" >> /opt/app/SigDespensa/sig-despensa/.env

WORKDIR /opt/app/SigDespensa

# install dependencies 
RUN pip install -r requirements.txt --cache-dir /opt/app/SigDespensa/pip_cache
RUN chown -R www-data:www-data /opt/app/SigDespensa

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/SigDespensa/start-server.sh"]