import os
from PIL import Image, ExifTags
import datetime
from pathlib import Path

def rename_files(target_folder, include_subfolders, remove_n_chars, prefix : str, suffix : str, replace):
    """
    :param remove_n_chars: int[remove_n_from_start, remove_n_at_end]
    :param replace: str[['replace_a', 'with_a'],['replace_b', 'with_b'], ...]
    """
    filenames = None
    if not include_subfolders:
        filenames = Path(target_folder).glob('*')
    else:
        filenames = Path(target_folder).rglob('*')

    for filename in filenames:
        if filename.is_file():
            new_filename = filename.stem
            if remove_n_chars is not None and len(remove_n_chars) > 1 and remove_n_chars[1] is not None and remove_n_chars[1] > 0 and len(new_filename) > remove_n_chars[1]:
                new_filename = new_filename[:len(new_filename) - remove_n_chars[1]]
            if remove_n_chars is not None and len(remove_n_chars) > 0 and remove_n_chars[0] is not None and remove_n_chars[0] > 0 and len(new_filename) > remove_n_chars[0]:
                new_filename = new_filename[remove_n_chars[0]:]
            if prefix is not None:
                new_filename = prefix + new_filename
            if suffix is not None:
                new_filename = new_filename + suffix

            new_filename = new_filename + filename.suffix
            if replace is not None:
                for replace_tuple in replace:
                    new_filename = new_filename.replace(replace_tuple[0], replace_tuple[1])        
            if new_filename != filename.name:
                os.rename(filename._str, os.path.join(filename.parent._str, new_filename))

def image_get_capture_datetime(image_path: str):
    try:
        exif = Image.open(image_path)._getexif()
    except:
        return None
    if exif is not None:
        try:
            return datetime.datetime.strptime(exif[36867], '%Y:%m:%d %H:%M:%S')
        except:
            pass
    return None

def rename_image_files(target_folder, prefix : str, suffix : str, original_filename : bool):
    """
    prefix + YYYYMMDD_HHmmSS + original_filename + suffix
    """
    for filename in os.listdir(target_folder):
        creation_time = image_get_capture_datetime(os.path.join(target_folder, filename))
        if creation_time is not None:
            extsep_index = os.path.basename(filename).rfind(os.path.extsep)
            extension = os.path.basename(filename)[extsep_index:]
            if filename.endswith('.PHOTOSPHERE' + extension):
                extension = '.PHOTOSPHERE' + extension
            new_filename = creation_time.strftime("%Y%m%d_%H%M%S") #+ creation_time.strftime("%f")[:3]
            if original_filename:
                new_filename = new_filename + '_' + os.path.basename(filename)[:extsep_index]
            if prefix is not None:
                new_filename = prefix + new_filename
            if suffix is not None:
                new_filename = new_filename + suffix  
            new_filename = new_filename + extension
            os.rename(os.path.join(target_folder, filename), os.path.join(target_folder, new_filename))

if __name__ == "__main__":
    target_folder = '/Users/soerli/AndroidStudioProjects/Topos/itsrox route scraper/val calanca/images_verified'
    rename_files(target_folder, True, None, None, None, [['_1.webp','.webp']])
    #rename_image_files(target_folder, None, '_PXL', False)