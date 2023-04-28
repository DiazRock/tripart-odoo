FROM odoo:15
RUN pip3 install -U debugpy
COPY ./entry.sh /
#RUN chmod +x /entrypoint.sh
RUN  sh /entry.sh
