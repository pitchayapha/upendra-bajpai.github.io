import os
import datetime
import glob
def move_files():
	root=os.getcwd()
	date = datetime.date.today()
	fol_csv='csvs'
	fol_data='newsData'
	mv_csv=os.path(root,fol_csv,str(date))
	mv_files=os.path(root,fol_data,str(date))
	try:
		os.mkdirs(mv_csv)
		os.mkdirs(mv_files)
		md_
	except Exception as e:
		print(e)
		pass
	pass
move_files()