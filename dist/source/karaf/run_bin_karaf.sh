#-------- Clean up temp files

#These lines removes the data/tmp and data/cache files so that any changes made to Inspecta .jar files can be reflected the next time Inspecta backend runs

echo "Removing data/tmp ..."
rm -f -R data/tmp
echo "Removing data/cache"
rm -R data/cache
source /etc/environment
rm lock #remove LOCK file
#Solving error: INFO: Trying to lock /opt/inspecta/inspecta-0.9.4/lock
#Jun 19, 2020 10:00:19 AM org.apache.karaf.main.lock.SimpleFileLock lock
#-------- Run Inspecta Backend
echo "Running Inspecta backend"
#----- run Karaf in normal mode
bin/karaf
#----- run Karaf in debug mode
#bin/karaf debug
