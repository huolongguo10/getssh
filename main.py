def read_file(filepath):
  with open(filepath) as fp:
      content = fp.read();
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
  c_m_d = ''
  for i in range targetpasswd :
    c_m_d += 'sshpass -p '
    c_m_d += targetpasswd[i]
    c_m_d += 'ssh'
    c_m_d += targetusername
    c_m_d += '@'
    c_m_d += targetip
    c_m_d += '\n'
    
