import app_convert
index = 0
installs=[]
print(type(installs))

package = app_convert.get_package()
#print(package)
for item in package:
    package =item.split('==')
    installs.append(package[index]+'\n')

print(installs)
app_convert.write_package(installs)
   



