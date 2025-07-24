import os

def rename_files(target_folder, remove_n_chars, prefix : str, suffix : str, replace):
    """
    :param remove_n_chars: int[remove_n_from_start, remove_n_at_end]
    :param replace: str[['replace_a', 'with_a'],['replace_b', 'with_b'], ...]
    """
    for filename in os.listdir(target_folder):
        if os.path.extsep not in os.path.basename(filename):
            #ignore directories
            pass
        else:
            extsep_index = os.path.basename(filename).index(os.path.extsep)
            new_filename = os.path.basename(filename)[:extsep_index]
            extension = os.path.basename(filename)[extsep_index:]
            if remove_n_chars is not None and len(remove_n_chars) > 1 and remove_n_chars[1] is not None and remove_n_chars[1] > 0 and len(new_filename) > remove_n_chars[1]:
                new_filename = new_filename[:len(new_filename) - remove_n_chars[1]]
            if remove_n_chars is not None and len(remove_n_chars) > 0 and remove_n_chars[0] is not None and remove_n_chars[0] > 0 and len(new_filename) > remove_n_chars[0]:
                new_filename = new_filename[remove_n_chars[0]:]
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
    rename_files('/Users/soerli/Downloads/Bill Willingham & Mark Buckingham', [0,7], None, None, None)