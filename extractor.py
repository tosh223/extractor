import zipfile
import glob

import multiprocessing as multi
from multiprocessing.pool import Pool

processes = 4
search_path = "absolute path"
search_text = "file text what you want to extract"

class Extractor():
    ###############################################
    def extract(self):
        zip_files = glob.glob(f"{search_path}/**/**.zip", recursive=True)

        args = [[zip_file, search_text] for zip_file in zip_files]
        with Pool(processes=processes) as p:
            p.map(self.wrapper, args)

    ###############################################
    # Pool Method Wrapper
    def wrapper(self, args):
        return self.extract_file(*args)

    ###############################################
    # Pool Method
    def extract_file(self, zip_file, search_file):
        
        with zipfile.ZipFile(zip_file) as z:
            for info in z.infolist():
                # for japanese files
                # info.filename = info.filename.encode('cp437').decode('cp932')
                if search_text in info.filename:
                    z.extract(info)
                    break

###############################################
def main():
    extr = Extractor()
    extr.extract()

###############################################
if __name__ == '__main__':
    main()
