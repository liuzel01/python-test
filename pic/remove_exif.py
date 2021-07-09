import subprocess
import os
import json
from pathlib import Path
from pprint import pprint


class ExifTool(object):

    sentinel = "{ready}\n"
    #windows
    #sentinel = "{ready}\r\n"

    def __init__(self, executable="/usr/bin/exiftool"):
        exiftool1 = Path("/usr/bin/exiftool")
        exiftool2 = Path("/usr/local/bin/exiftool")
        self.executable = executable
        if exiftool1.exists():
            self.executable = exiftool1.as_posix()
        elif exiftool2.exists():
            self.executable = exiftool2.as_posix()
        else:
            if Path(self.executable).exists():
                pass
            else:
                raise FileNotFoundError(self.executable)


    def __enter__(self):
        self.process = subprocess.Popen(
            [self.executable, "-stay_open", "True",  "-@", "-"],
            universal_newlines=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.process.stdin.write("-stay_open\nFalse\n")
        self.process.stdin.flush()

    def execute(self, *args):
        args = args + ("-execute\n",)
        self.process.stdin.write(str.join("\n", args))
        self.process.stdin.flush()
        output = ""
        fd = self.process.stdout.fileno()
        while not output.endswith(self.sentinel):
            # output += os.read(fd, 4096).decode('utf-8',errors=)
            output += os.read(fd, 4096).decode('utf-8',"ignore")
        return output[:-len(self.sentinel)]

    def get_metadata(self, *filenames):
        """
        返回多个文件的 exif 信息
        """
        return json.loads(self.execute("-G", "-j", "-n", *filenames))

    def get_exif_info(self, source_img):
        """
        返回单个文件的 exif 信息
        """
        return self.get_metadata(source_img)[0]

    def delete_exif_info(self, source_img):
        '''
        删除 exif 信息后，返回剩余的 exif 信息
        '''
        self.execute("-all=",source_img)
        metadata = self.get_metadata(source_img)
        return metadata[0]



if __name__ == '__main__':
    with ExifTool() as e:
        exif = e.get_exif_info('./download_images/images1.png')
        pprint(exif)
        exif = e.delete_exif_info('./download_images/images1.png')
        print("========删除 exif 信息后========")
        pprint(exif)