#%%

import os



#%% Create files to test the script

no_files = 5

working_directory = os.getcwd()
path_to_test_dir = os.path.join(os.getcwd(),'test')
name_list = ['bolt_', 'doodad_', 'whirlygig_']
ext = '.txt'

def create_files_for_test():
    for i in range(no_files):
        for name in name_list:
            with open(os.path.join(path_to_test_dir,name+str(i)+ext),'w') as fp:
                pass

# write list containing the names of the entries in the directory given by path to filenames_backup.txt
def create_filenames_backup(path):
    with open(os.path.join(os.listdir(path),'filenames_backup.txt'),'w') as backup_fp:
        for line in dir_list:
            backup_fp.write(line+'\n')


def rename(path,old,new):
    for f in os.listdir(path):
        os.rename(os.path.join(path, f), os.path.join(path, f.replace(old, new)))

create_files_for_test()

#%%

dir_list = os.listdir(path_to_test_dir)
print("List of directories and files before creation:")
print(dir_list)
print()

## user chooses to restore filenames from backup, or rename files according to pattern
while (True):
    replace_from_backup_input = input("restore filenames from filenames_backup.txt? Enter y or n:")
    if replace_from_backup_input == 'y':
        backup = True
    elif replace_from_backup_input == 'n':
        backup = False
    else:
        print('that was not "y" or "n"...')
        continue
    break





if backup == True:
    pass

else:
    directory = 'C:\Software\_code\search_replace_filenames\test'
#    directory = input ("Enter your directory")
    old = input ("Enter what you want to replace ")
    new = input ("Enter what you want to replace it with")
    
    create_filenames_backup()
    rename(directory,old,new)



dir_list = os.listdir(path_to_test_dir)
print("List of directories and files after creation:")
print(dir_list)
print()


    




#%%

print(os.getcwd())

# nick wants to replace:
# bag1_lots_of_stuff.csv
# bag1_something.csv
# bag1_somethingelse.csv
# bag1_dj4xcvld263.csv
# bag2_lots_of_stuff.csv
# bag2_something.csv
# bag2_somethingelse.csv
# bag2_dj4xcvld263.csv

# with:
# bag1_Sample1.csv
# bag1_Sample2.csv
# bag1_Sample3.csv
# bag1_Sample4.csv
# bag2_Sample1.csv
# bag2_Sample2.csv
# bag2_Sample3.csv
# bag2_Sample4.csv




# %%
