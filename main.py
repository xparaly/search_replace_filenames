#%%
"""renames all files in a folder according to a user-defined pattern.  thats the goal.... currently is not a user-defined pattern.  would also like an interactive gui..."""


import os

def create_files_for_test(name_list: str):
    """create files from a list of names, to test the script"""
    path_to_test_dir = os.path.join(os.getcwd(),'test')
    ext = '.txt'
    for name in name_list:
        with open(os.path.join(path_to_test_dir,name+ext),'w') as fp:
            pass

def rename_and_backup(path: str, restore_from_backup: bool = False) -> list:
    """rename files in path and create backup of old filenames at path/filenames_backup.txt"""
    
    restore_from_backup = get_input()

    if restore_from_backup == False:
        name_dict = dict()
        old_names = os.listdir(path)

        if "filenames_backup.txt" in old_names: old_names.remove("filenames_backup.txt")

        new_names = list()
        for name in old_names:
            substring1, substring2 = name.split('_',1)
            if substring1 in name_dict.keys():
                name_dict[substring1] += 1
            else:
                name_dict[substring1] = 1
            new_names.append(name.replace(substring2,'Sample'+str(name_dict[substring1])+'.txt'))
        print("new names:")
        print(new_names)
        all_names = list(zip(old_names,new_names))

        with open(os.path.join(path,'filenames_backup.txt'),'w') as backup_fp:
            for line in all_names:
                backup_fp.write(','.join(line)+'\n')

    with open(os.path.join(path,'filenames_backup.txt'),'r') as backup_fp:
        for line in backup_fp.readlines():
            if restore_from_backup == False:
                old = line.split(',')[0]
                new = line.split(',')[1].rstrip()
            else:
                new = line.split(',')[0]
                old = line.split(',')[1].rstrip()
            os.rename(os.path.join(path,old), os.path.join(path,new))

    return all_names


def get_input() -> bool:
    """get user's choice of restoring filenames from backup or creating new filenames"""
    while (True):
        user_input = input("restore filenames from filenames_backup.txt? Enter y or n:")
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('that was not "y" or "n"...')
            continue

#%% Create files for the test


working_directory = os.getcwd()
path_to_test_dir = os.path.join(os.getcwd(),'test')
name_list = ['bolt_cmvu3e',
              'bolt_cddcb2az',
              'bolt_kveirbh',
              'doodad_pcawexfc',
              'doodad_qpv9213',
              'doodad_mbnqlgd37',
              'doodad_mwgeg',
              'whirlygig_vkbwbw',
              'whirlygig_qkenfiv3',
              'whirlygig_bnejkw0',
              'whirlygig_rrmew',
              'whirlygig_vmecq3']

create_files_for_test(name_list)





#%%

path_to_test_dir = os.path.join(os.getcwd(),'test')

print("List of directories and files before creation:")
print(os.listdir(path_to_test_dir))
print()

all_names = rename_and_backup(path_to_test_dir,False)

print("List of directories and files after creation:")
print(os.listdir(path_to_test_dir))
print()



#%%


def remove_files_for_test():
    path_to_test_dir = os.path.join(os.getcwd(),'test')
    pass
    # for file in os.listdir(path_to_test_dir):



"""
how to test that filenames can be renamed from backup?
how to remove old files?
"""


## for each common thing before underscore
##      replace thing after underscore with
##          Sample1, Sample2, Sample3, etc.

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


