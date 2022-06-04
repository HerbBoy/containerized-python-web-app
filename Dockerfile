FROM redhat/ubi8:8.5

# Creating Demo Dir
RUN mkdir -p /demo

#Setting Working Dir to Flask app "demo"
WORKDIR /demo

# Setting Default Argument values
ARG CERT=cert.pem
ARG KEY=key.pem

# Update all base packages and ensure python3 is installed
RUN yum update -y
RUN yum install python3 -y
RUN yum clean all -y

# Install App Dependencies
RUN pip3 install Flask
RUN pip3 install requests
RUN pip3 install gunicorn

#Adding flask script to /demo dir (using abs path)
COPY py_data/app.py /demo/
COPY demo.sh /demo/

# Putting Certs into place (overwriting names to account for hardcoded certs values - no the most prod)
COPY $CERT /demo/cert.pem
COPY $KEY /demo/key.pem

# Make entrypoint executable
RUN chmod +x /demo/demo.sh

#Container listening port
EXPOSE 5000

# upon start what is executed
ENTRYPOINT [ "./demo.sh" ]