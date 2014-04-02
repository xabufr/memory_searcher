import os

os.environ['CLASSPATH'] = os.path.join(os.path.dirname(__file__), "tika-app.jar")

from jnius import autoclass

class TextExtractor():
    def __init__(self):
        self.Tika = autoclass('org.apache.tika.Tika')
        self.Metadata = autoclass('org.apache.tika.metadata.Metadata')
        self.FileInputStream = autoclass('java.io.FileInputStream')

    def extract_text(self, file_path):
        tika = self.Tika()
        meta = self.Metadata()
        return tika.parseToString(self.FileInputStream(file_path), meta)
