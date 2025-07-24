import os

def rename_files(target_folder, remove_first_n_chars : int, prefix : str, suffix : str, replace):
    for filename in os.listdir(target_folder):
        extsep_index = os.path.basename(filename).index(os.path.extsep)
        new_filename = os.path.basename(filename)[:extsep_index]
        extension = os.path.basename(filename)[extsep_index:]
        if remove_first_n_chars is not None and remove_first_n_chars > 0 and len(new_filename) > remove_first_n_chars:
            new_filename = new_filename[remove_first_n_chars:]
        if prefix is not None:
            new_filename = prefix + new_filename
        if suffix is not None:
            new_filename = new_filename + suffix
        if replace is not None:
            for replace_tuple in replace:
                new_filename = new_filename.replace(replace_tuple[0], replace_tuple[1])        
        new_filename = new_filename + extension
        os.rename(os.path.join(target_folder, filename), os.path.join(target_folder, new_filename))

if __name__ == "__main__":
    rename_files('/Users/soerli/Downloads/Akira', 0, None, None, [['- c','- Chapter ']])