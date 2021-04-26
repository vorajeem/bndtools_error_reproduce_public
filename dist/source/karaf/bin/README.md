# bin/
Control scripts to start, stop login of Karaf container

# Default scripts

- karaf : Regular start for Karaf
- start : Start Karaf container in background
- status 
- stop : Works only for background (bin/start) or in regular with another terminal
- instance
- setenv : Scripts to set environment variables
- shell
- client : SSH connect to console

## Scripts which have been added

inspecta-wrapper : Unknown
inspecta-service : Defines the various commands for the Inspecta Karaf container
inspecta.service : Points the start/stop scripts for the Inspecta Karaf container (It has nothing to do with the systemctl inspecta-karaf background)
