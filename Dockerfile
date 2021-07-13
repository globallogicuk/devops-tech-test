FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
mysql-client \
python3
COPY createdatabase.sql /app
# COPY dbconnect.sh /scripts/dbconnect.sh
# CMD /scripts/dbconnect.sql
