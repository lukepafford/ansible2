import sys, subprocess as sp

if len(sys.argv) < 3:
  print('{0}: envName packages...'.format(sys.argv[0]))
  sys.exit(1)
  
envName = sys.argv[1]
packages = sys.argv[2:]

condaList = [ 'conda', 'list', '-n', envName ]
installedPackages = sp.check_output(condaList, text=True).split()

packagesNeedingInstall = list(filter(lambda x: x not in installedPackages, packages))
if packagesNeedingInstall:
  condaInstall = [ 'conda', 'install', '-n', envName, *packagesNeedingInstall, '--yes' ]
  sp.check_call(condaInstall)
