import re

def mappathf(path):
    with open('/tmp/paths.txt', 'a') as f:
        f.write("------path--------\n")
        f.write(path)
        f.write("\n")
    #if re.search(r'([^;]*)/([^;]*)/([^;]*)/([^;]*)/([^;]*)/pycharm/',path):
    if path=="/":
        p = '/?username=domino&password=domino'
    else:
        p = path
    with open('/tmp/paths.txt', 'a') as f:
        f.write(p)
        f.write("\n------end--------\n")
    return p
    
def setup_pycharm():
  return {
    'command': ['/var/opt/workspaces/pycharm/start.sh'],
    'port': 8080,
    'timeout': 300,
    'absolute_url': True,
    'mappath' : mappathf,
    'launcher_entry': {
            'title': 'pycharm: Login domino/domino'
    }
  }
