import os

path = str(input("Введите путь: "))
find_ = input('Что ищем?: ')
replace_ = input('На что меняем?: ')


def obxof_file(path, level=1):
	#print('Level=',level,"Content:",os.listdir(path))
	for i in os.listdir(path):
			if os.path.isfile(path+'\\'+i):
				if find_ in i:
					name = i
					#print(newname)
					newi = name.replace(find_, replace_)
					#print(newi)
					os.rename(path+'\\'+i, path+'\\'+newi)
					print(path+'\\'+newi)

			if os.path.isdir(path+'\\'+i):
				if find_ in i:
					name = i
					newi = name.replace(find_, replace_)
					os.rename(path+'\\'+i, path+'\\'+newi)
				#try:	
					#path(path+'\\'+newi)
					print(path+'\\'+newi)
				#except:
				#	pass

				#print('Спускаемся', path+'\\'+i)
					obxof_file(path+'\\'+newi, level+1)  #ТУТ ПЕРЕЧИТЫВАЕМ ЗНАЧЕНИЕ ДЛЯ ЦИКЛА, ЧТОБЫ НОВЫЙ ПУТЬ СЧИТАТЬ!
				#print('Возвращаемся в',path)
obxof_file(path)