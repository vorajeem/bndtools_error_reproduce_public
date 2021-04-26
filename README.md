# bndtools-reproduce-tools

## Tested development environment
- Eclipse: 2020-03 (Eclipse IDE for Enterprise  Developers)
- Java 8 (OpenJdk)
- bndtools 5.3.0.REL
- Ubuntu 16.04 Desktop environment

## Steps to reproduce the error


1. Clone the repo
2. Open Eclipse with the repo directory as the workspace
3. Import the 'Existing Bndtools workspace'
4. Run OSGi file using 'runtime/stub.bndrun' file.
5. You should see the following error on the console ```Error: Could not find or load main class aQute.launcher.Launcher```
