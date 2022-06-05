# JC Project

- [x] Can accept the proper api requests.
- [x] Dockerfile built out to support containerized deployement
- [x] Leverages Gunicorn for HTTP serivice
- [x] Logs data to syslog (in real world I would want to point this to a syslog server or have a SIEM like splunk have an forwarder monitor the local syslog)
- [x] Leverages SSL (self signed at this point with ability to dynamically take it properly signed certificates).
- [x] Automated deployment with ansible. 
- [x] Automated build from source with ansible
- [x] Automated export of container image with ansible


# Requirements/Dependencies
- Python >= 3.6
- Podman >= 3.4
- Ansible >= 2.9

# Notes:

This was built for localalized deployment to say a Podman or Docker Pod running on a VM/Baremetal system running a given OS. Given the resources this could be built to be deployed against a cloud solution.
