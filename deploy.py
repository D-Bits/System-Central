from subprocess import run


deploy = run(['pyinstaller', 'main.py', '-F', '-n', 'SystemCentral'])

if deploy.returncode == 0:
    input('Deployment succesful. Press enter to exit.')
else:
    input('WARNING: Deployment failed. Press enter to exit.')