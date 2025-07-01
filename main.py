import os

def rename_files(target_folder, remove_first_n_chars : int, prefix : str, suffix : str):
    for filename in os.listdir(target_folder):
        new_filename = os.path.splitext(os.path.basename(filename))[0]
        if remove_first_n_chars is not None and len(new_filename) > remove_first_n_chars:
            new_filename = new_filename[remove_first_n_chars:]
        if prefix is not None:
            new_filename = prefix + new_filename
        if suffix is not None:
            new_filename = new_filename + suffix
        new_filename = new_filename + os.path.splitext(os.path.basename(filename))[1]
        os.rename(os.path.join(target_folder, filename), os.path.join(target_folder, new_filename))

if __name__ == "__main__":
    rename_files('/Users/soerli/Pictures/Albigna Juni 2025', 6, None, '_Tibor')