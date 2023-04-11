import subprocess as s
import os
print('')
flow = open('file', mode='r+' )
res = s.run(['ls', '-a'],
            stdout=s.PIPE,
            stdin=s.PIPE,
            stderr=s.PIPE,
            shell=True)
print(res.stdout.decode('utf_8').count('LICENSE'))
del(res)
flow.truncate(0)
print(res)

flow.close()