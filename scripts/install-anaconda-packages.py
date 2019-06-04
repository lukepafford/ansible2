import sys, subprocess as sp

if len(sys.argv) < 3:
  print('{0}: envName packages...'.format(sys.argv[0]))
  sys.exit(1)
  
envName = sys.argv[1]
packages = sys.argv[2:]
retCode = 0

condaList = [ 'conda', 'list', '-n', envName ]
installedPackages = sp.check_output(condaList).split()

packagesNeedingInstall = filter(lambda x: x not in installedPackages, packages)
if packagesNeedingInstall:
	retCode = 2
	condaInstall = [ 'conda', 'install', '-n', envName, '--yes' ] + packagesNeedingInstall
	sp.check_call(condaInstall)

sys.exit(retCode)
