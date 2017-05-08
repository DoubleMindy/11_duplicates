import os

if __name__ == '__main__':
    list_of_all = []
    list_of_path = []
    full_path_n_size = {}
    
    path_to_dir = input('Enter path to directory: ')
    
    for top, dirs, files in os.walk(path_to_dir):     
        list_of_all.append(files)
        list_of_path.append(top)
        
biglist =  sum(list_of_all, [])
set_of_pretends = set([i for i in biglist if biglist.count(i) > 1])

for files in set_of_pretends:
    for paths in list_of_path:
        if os.path.exists(paths + '\\' + files):
            full_path_n_size[os.path.getsize(paths + '\\' + files)] = paths + '\\' + files

only_names = [os.path.basename(k) for k in full_path_n_size.values()]
files_to_delete = [c for c in only_names if only_names.count(c) == 1]

print('I delete these files:  ')
for files in files_to_delete:
    for paths in full_path_n_size.values():
        tmp_path = os.path.dirname(paths) + '\\' + files
        if os.path.exists(tmp_path):           
            os.remove(tmp_path)
            break
        
print(' ---------------DONE---------------')    
