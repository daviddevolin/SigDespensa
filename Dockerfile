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
RUN mkdir -p /opt/app/SigDespensa/sigdespensa

# copy source
COPY sigdespensa/requirements.txt /opt/app/SigDespensa/
COPY start-server.sh /opt/app/SigDespensa/
COPY sigdespensa /opt/app/SigDespensa/sigdespensa
WORKDIR /opt/app/SigDespensa

# install dependencies 
RUN pip install -r requirements.txt --cache-dir /opt/app/SigDespensa/pip_cache
RUN chown -R www-data:www-data /opt/app/SigDespensa

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/SigDespensa/start-server.sh"]