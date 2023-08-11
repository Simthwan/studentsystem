import os

filename = 'student.txt'
def main():
	while True:
		menu()
		try:	
			choice=int(input('请选择'))
			if choice in [0,1,2,3,4,5,6,7]:
				if choice==0:
					answer=input('您确定要退出系统吗？y/n')
					if answer=='y' or answer=='Y':
						print('谢谢您的使用!!!')
						break #退出系统
					else:
						continue
				elif choice==1:
					insert() #录入学生信息
				elif choice==2:
					search()
				elif choice==3:
					delete()
				elif choice==4:
					modify()
				elif choice==5:
					sort()
				elif choice==6:
					total()
				elif choice==7:
					show()
			else:
				print('请选择0~7中的一个整数进行输入...')
		except:
			print('请选择0~7中的一个整数进行输入...')

def menu():
	print('================================学生信息管理系统================================')
	print('-----------------------------------功能菜单------------------------------------')
	print('\t\t\t\t\t\t1.录入学生信息')
	print('\t\t\t\t\t\t2.查找学生信息')
	print('\t\t\t\t\t\t3.删除学生信息')
	print('\t\t\t\t\t\t4.修改学生信息')
	print('\t\t\t\t\t\t5.排序')
	print('\t\t\t\t\t\t6.统计学生总人数')
	print('\t\t\t\t\t\t7.显示所有学生信息')
	print('\t\t\t\t\t\t0.退出系统')
	print('-------------------------------------------------------------------------------')

def insert():
	student_list=[]
	while True:
		id=input('请输入ID(如1001):')
		if not id:
			break
		name=input('请输入姓名:')
		if not name:
			break

		try:
			chinese=int(input('请输入语文成绩:'))
			math=int(input('请输入数学成绩:'))
			english=int(input('请输入英语成绩:'))
			science_integrated=int(input('请输入理综成绩:'))
		except:
			print('输入无效，不是整数类型，请重新输入...')
			continue
		#将录入的学生信息保存到字典当中
		student={'id':id,'name':name,'chinese':chinese,'math':math,'english':english,'science_integrated':science_integrated}
		#将学生信息添加到列表中
		student_list.append(student)
		answer=input('是否继续添加？y/n\n') #\n换行
		if answer=='y' or answer=='Y':
			continue
		else:
			break
	#调用save()函数将学生信息保存到文件当中
	save(student_list)
	print('学生信息录入完毕!!!')

def save(lst):
	try:
		stu_txt=open(filename,'a',encoding='utf-8')
	except:
		stu_txt=open(filename,'w',encoding='utf-8')
	for item in lst:
		stu_txt.write(str(item)+'\n')
	stu_txt.close()

def search():
	student_query=[]
	while True:
		id=''
		name=''
		if os.path.exists(filename):
			mode=input('按ID查找请输入1，按姓名查找请输入2:')
			if mode=='1':
				id=input('请输入要查询的学生的ID:')
			elif mode=='2':
				name=input('请输入要查询的学生的姓名:')
			else:
				print('您的输入有误，请重新输入')
				continue
			with open(filename,'r',encoding='utf-8') as rfile:
				student=rfile.readlines()
				for item in student:
					d=dict(eval(item))
					if id!='':
						if d['id']==id:
							student_query.append(d)
					elif name!='':
						if d['name']==name:
							student_query.append(d)
			#显示查询结果
			show_student(student_query)
			#清空列表
			student_query.clear()
			answer=input('是否要继续查询？y/n\n')
			if answer=='y' or answer=='Y':
				continue
			else:
				break
		else:
			print('暂未保存学生信息')
			return

def show_student(lst):
	if len(lst)==0:
		print('没有查询到学生信息，无数据显示!!!')
		return
	#定义标题显示格式
	format_title='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:8}'
	print(format_title.format('ID','姓名','语文成绩','数学成绩','英语成绩','理综成绩','总成绩'))
	#定义内容的显示格式
	format_data='{:^6}\t{:^12}\t{:^11}\t{:^11}\t{:^11}\t{:^11}\t{:4}'
	for item in lst:
		print(format_data.format(item.get('id'),
								 item.get('name'),
								 item.get('chinese'),
								 item.get('math'),
								 item.get('english'),
								 item.get('science_integrated'),
								 int(item.get('chinese'))+int(item.get('math'))+int(item.get('english'))+
								 int(item.get('science_integrated'))))

def delete():
	while True:
		student_id=input('请输入要删除学生的ID:')
		if student_id != '':
			if os.path.exists(filename):
				with open(filename,'r',encoding='utf-8') as file:
					student_old=file.readlines() #读取所有的数据放到列表student_old当中
			else:
				student_old=[]
			flag=False #标记是否删除
			if student_old:
				with open(filename,'w',encoding='utf-8') as wfile:
					for item in student_old:
						d=dict(eval(item)) #将字符串转成字典 eval()方法通俗的讲就是去掉字符串的引号
						if d['id']!=student_id: #如果找不到这个id，那么else就不会执行flag=False,对应没有找到学生信息
							wfile.write(str(d)+'\n')
						else:
							flag=True
				if flag:
					print(f'ID为{student_id}的学生信息已被删除...')
				else:
					print(f'没有找到ID为{student_id}的学生信息...')
			else:
				print('无学生信息')
				break
		show()  #删除之后要重新显示学生信息
		answer=input('是否继续删除呢？y/n\n')
		if answer=='y' or answer=='Y':
			continue
		else:
			break

def modify():
	show()
	if os.path.exists(filename):
		with open(filename,'r',encoding='utf-8') as rfile:
			student_old=rfile.readlines()
	else:
		return
	student_id=input('请输入要修改的学员的ID:')
	if student_id!='':
		with open(filename,'w',encoding='utf-8') as wfile:
			d={}
			for item in student_old:
				d=dict(eval(item))
				if d['id']==student_id:
					print('找到学生信息，可以修改他的相关信息了!')
					while True:
						try:
							d['name']=input('请输入姓名:')
							d['chinese']=int(input('请输入语文成绩:'))
							d['math']=int(input('请输入数学成绩:'))
							d['english']=int(input('请输入英语成绩:'))
							d['science_integrated']=int(input('请输入理综成绩:'))
						except:
							print('您的输入有误请重新输入...')
						else:
							break
					wfile.write(str(d)+'\n')
					print('修改成功!!!')
				else:
					wfile.write(str(d)+'\n')
		answer=input('是否要继续修改其他学生信息？y/n\n')
		if answer=='y' or answer=='Y':
			modify()
	else:
		print('请输入有效信息...')

def sort():
	show()
	if os.path.exists(filename):
		with open(filename,'r',encoding='utf-8') as rfile:
			students=rfile.readlines()
		student_list=[]
		for item in students:
			student_list.append(dict(eval(item)))
	else:
		return
	asc_or_desc=input('请选择(0.升序 1.降序):')
	if asc_or_desc=='0':
		asc_or_desc_bool=False
	elif asc_or_desc=='1':
		asc_or_desc_bool=True
	else:
		print('您的输入有误，请重新输入...')
		sort()
	mode=input('请选择排序方式(1.按学号排序 2.按语文成绩排序 3.按数学成绩排序 4.按英语成绩排序 5.按理综成绩排序 0.按总成绩排序):')
	if mode=='1':
		student_list.sort(key=lambda x :int(x['id']),reverse=asc_or_desc_bool) #此处为sort()函数与匿名函数lambda的联用，sort()
																			   #sort()函数只用与列表排序，实际上还可写为
																	#sorted(student_list,key=lambda x :int(x['id']),reverse=False)
	elif mode=='2':
		student_list.sort(key=lambda x :int(x['chinese']),reverse=asc_or_desc_bool)
	elif mode=='3':
		student_list.sort(key=lambda x :int(x['math']),reverse=asc_or_desc_bool)
	elif mode=='4':
		student_list.sort(key=lambda x :int(x['english']),reverse=asc_or_desc_bool)
	elif mode=='5':
		student_list.sort(key=lambda x :int(x['science_integrated']),reverse=asc_or_desc_bool)
	elif mode=='0':
		student_list.sort(key=lambda x :int(x['chinese'])+int(x['math'])+int(x['english'])+int(x['science_integrated']),reverse=asc_or_desc_bool)
	else:
		print('您的输入有误，请重新输入!!!')
		sort()
	show_student(student_list)

def total():
	if os.path.exists(filename):
		with open(filename,'r',encoding='utf-8') as rfile:
			students=rfile.readlines()
			if students:
				print(f'一共有{len(students)}名学生')
			else:
				print('还没有录入学生信息')
	else:
		print('暂未保存数据信息...')

def show():
	student_list=[]
	if os.path.exists(filename):
		with open(filename,'r',encoding='utf-8') as rfile:
			students=rfile.readlines()
			for item in students:
				student_list.append(dict(eval(item)))
			if student_list:
				show_student(student_list)
	else:
		print('暂未保存过数据...')

if __name__=='__main__':
	main()