import os
from os.path import isdir
class Read_Custom_Files:
    # All of the custom files will be held in the custom file directory

	def __init__(self):
		self.file_names = None
		if not isdir('custom_files_directory'):
			os.makedirs('custom_files_directory')
		else:
			self.file_names = self.get_file_names_in_dirs()
			
	
	def get_file_names_in_dirs(self):
		dirs = os.listdir()
		for x in dirs:
			for dir, subdir, files in os.walk(x):
				for file in files:
					file_dest = os.path.join(dir,file)
					yield file_dest

