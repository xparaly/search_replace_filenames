#%%

import os

def create_files_for_test(no_files: int, name_list: str):
    path_to_test_dir = os.path.join(os.getcwd(),'test')
    ext = '.txt'
    for i in range(no_files):
        for name in name_list:
            with open(os.path.join(path_to_test_dir,name+str(i)+ext),'w') as fp:
                pass

def create_files_for_test2(name_list: str):
    path_to_test_dir = os.path.join(os.getcwd(),'test')
    ext = '.txt'
    for name in name_list:
        with open(os.path.join(path_to_test_dir,name+ext),'w') as fp:
            pass

def rename_and_backup2(path: str, restore_from_backup: bool = False) -> list:
    """write list containing the names of the entries in the directory given by path to filenames_backup.txt"""
    
    restore_from_backup = get_input()


    if restore_from_backup == False:
        name_dict = dict()
        
        old_names = os.listdir(path)
        new_names = list()
        for name in old_names:
            substring1, substring2 = name.split('_',1)
            if substring1 in name_dict.keys():
                name_dict[substring1] += 1
            else:
                name_dict[substring1] = 1
            new_names.append(name.replace(substring2,'Sample'+str(name_dict[substring1])+'.txt'))
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
    while (True):
        user_input = input("restore filenames from filenames_backup.txt? Enter y or n:")
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('that was not "y" or "n"...')
            continue

#%% Test the script


working_directory = os.getcwd()
path_to_test_dir = os.path.join(os.getcwd(),'test')
name_list = ['bolt_', 'doodad_', 'whirlygig_']
name_list2 = ['bolt_cmvu3e',
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
no_files = 5

# create_files_for_test(no_files, name_list)
create_files_for_test2(name_list2)

print("List of directories and files before creation:")
print(os.listdir(path_to_test_dir))
print()

all_names = rename_and_backup2(path_to_test_dir,False)

print("List of directories and files after creation:")
print(os.listdir(path_to_test_dir))
print()



#%%

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


