import ConfigParser

config=ConfigParser.ConfigParser()
# config['main']={
#     'port':2222,
#     'threads':10,
# 'Compression': 'yes'
# }
#
#
# config['skg.com']={}
# config['skg.com']['user']='liujie'
# config['skg.com']['dev']='wang'
#
#
# with open('config2.ini','w') as f:
#     config.write(f)

config.read('config.ini')

print config.sections()

print config.items('LiveUpdate')
print  config.options("LiveUpdate")