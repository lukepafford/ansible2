import sys, subprocess as sp

if len(sys.argv) == 1:
	print('{0}: envName [pythonVersion = 3.7.3]'.format(sys.argv[0]))
	sys.exit(1)

envName = sys.argv[1]
version = sys.argv[2] if len(sys.argv) > 2 else '3.7.3'
retCode = 0

condaList = [ 'conda', 'env', 'list']
condaCreate = ['conda', 
							 'create', 
							 '-n', 
							 envName, 
							 'python={0}'.format(version), 
							 '--yes'
							 ]

condaEnvironments = sp.check_output(condaList)

if envName not in condaEnvironments:
	retCode = 2
	sp.check_call(condaCreate)

sys.exit(retCode)
