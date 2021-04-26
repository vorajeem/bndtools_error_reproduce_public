# etc/

## These files are configuration files

# Files which have not been changed

All files except branding.properties

#Files which have been changed

- branding.properties\_old\_with\_styling: Karaf container start up screen (not currently in use). I has a styling 'INSPECTA' front. I've choosen not to use the style because the new branding.properties provides us with useful info.

- branding.properties: Karaf container start up screen. This is shown when we run the Karaf container. Since we're running the Karaf container in the 'inspecta-karaf' systemctl service, we will see this when we run the command to check the status of the inspecta-karaf.service (i.e. sudo systemctl status inspecta-karaf.service)

- jetty.xml: SSH Admin

- inspecta-wrapper:

- org.apache.karaf.features.repos.cfg: Features

org.ops4j.pax.web.cfg: Ports

- custom.properties : HTTP.port

org.ops4j.pax.logging.cfg :Trace, Inspecta logging specification


