import subprocess
import os.path
import re


class TikaException(BaseException):
    def __init__(self, code, error):
        BaseException.__init__(self)
        self.code = code
        self.error = error


class Tika:
    def __init__(self, *, java_command='java', tika_path=None):
        self.java_command = java_command
        if tika_path is None:
            self.tika_path = os.path.join(os.path.dirname(__file__), 'tika-app.jar')
        else:
            self.tika_path = tika_path

    def get_file_content(self, file_path):
        return self.__call_tika(file_path, ['-t'])

    def get_file_metadata(self, file_path):
        """

        :param file_path: file to process
        :return: python dictionary
        """
        metadata = self.__call_tika(file_path, ['-m'])
        metadata = self.__patch_metadata_string(metadata)
        return metadata

    def __call_tika(self, file_path, options):
        base_options = [self.java_command, '-jar', self.tika_path, '-eUTF-8']
        command = base_options + options + [file_path]
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode is not 0:
            raise TikaException(process.returncode, err)
        return out.decode('utf-8')

    @staticmethod
    def __patch_metadata_string(metadata):
        metadata_array = {}
        for line in metadata.splitlines(True):
            entry = re.findall('(\S*): (.*)', line)[0]
            metadata_array[entry[0]] = entry[1]
        return metadata_array
