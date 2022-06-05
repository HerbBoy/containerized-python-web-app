# Module Requirements:

Run: ```ansible-galaxy collection install containers.podman```

## Note Ensure Variables are set ##

# To encrypt vauld
```ansible-vault encrypt vault.yml```

# To Run
Build from source and run: ```ansible-playbook manage_flask_app.yml --tag build_and_run --ask-vault```
Load from tarball and run: ```ansible-playbook manage_flask_app.yml --tag load_and_run --ask-vault```
