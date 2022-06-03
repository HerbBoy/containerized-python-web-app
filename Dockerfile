FROM redhat/ubi8:8.5

# Creating Demo Dir
RUN mkdir -p /demo

# Update all base packages and ensure python3 is installed
RUN yum update -y
RUN yum install python3 -y

# Install Flask Module
RUN pip3 install Flask

COPY py_data/app.py /demo

EXPOSE 80

CMD [ "python3" , "/demo/app.py" ]