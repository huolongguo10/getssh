def read_file(filepath):
  with open(filepath) as fp:
      content=fp.read();
  return content
def write_file(filepath,things)
  fo = open(filepath, "w")
  fo.write(things)
if __name__ = '__main__' :
  targetip = input('target:')
  targetusername = input('username:')
  passwd = input('password:')
  _targetpasswd=read_file(passwd)
  targetpasswd = _targetpasswd.split(',')
  
