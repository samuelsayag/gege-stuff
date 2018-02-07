#!/home/sam/envs/venv3.5/bin/python3.5

# The atomic operation is the following
#	Params:
#		- directory source
#		- directory target
#		- list of index (default to all)
#		- optional filter (default to identity)
# 1. list the files in a given directory
# 2. filter the files we want
# 3. apply the given index list
# 4. create the target directory if does not exist
# 5. copy the list of files to it

# your operation is constitute of 3 call to this operation with different index and target directories

# Note: point 5 may be replace by a function paramter according to what you want to do ex: cp, mv...

def selected_copy(source_path, target_dir_name, index_list, fileFilter = lambda x: True):
	from os import listdir, mkdir
	from os.path import isfile, join, isdir
	from shutil import copy
	# check all the element of a list are int
	if (not index_list) or (not all(map( lambda i : isinstance(i, int), index_list))):
		raise Exception("list is empty or not all element are int in: " + str(index_list))
	# check that the path is a dir
	if not isdir( source_path ):
		raise Exception("path does not exist: " + str(source_path))

	lf = list( filter( fileFilter, listdir(source_path) ) )

	# see the interesting: https://stackoverflow.com/questions/6632188/explicitly-select-items-from-a-python-list-or-tuple
	# for other (interesting) way to do this	
	# possible to replace i by i-1 if you want the index of the file beginning with one for the function user.
	final_l = list(join(source_path, lf[i]) for i in index_list if isfile(join(source_path, lf[i])))

	target_dir = join(source_path, target_dir_name)
	if final_l:
		if not isdir(target_dir): 
			mkdir(target_dir)

	for f in final_l:
		copy(f, target_dir)

	return 0

def main():
	# selected_copy("/home/sAm", "blahblah", ["baby"]) # fail
	# selected_copy("/home/sam", "blahblah", ["baby"]) # fail
	# selected_copy("/home/sam", "blahblah", []) # fail
	l = selected_copy("/home/sam/Documents/ctrecords/06-02-2018", "blahblah", [0,2,4,6,8]) 
	print(l)

if __name__ == "__main__":
	main()



