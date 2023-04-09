import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_FILE = []
DOCX_FILE = []
TXT_FILE = []
PDF_FILE = []
XLSX_FILE = []
PPTX_FILE = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

ARCHIVES = []
MY_OTHER = []  



REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_FILE,
    'DOCX': DOCX_FILE,
    'TXT': TXT_FILE,
    'PDF': PDF_FILE,
    'XLSX': XLSX_FILE,
    'PPTX': PPTX_FILE,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES,
    'GZ' : ARCHIVES,
    'TAR' : ARCHIVES
}
# TODO: add video and archives formats

FOLDERS = []
EXTENTIONS = set()
UNKNOWN = set()


def get_extention(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():

        # Робота з папкою
        if item.is_dir():

            # Перевіряємо, щоб папка не була тією в яку ми складаємо файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'other'):
                FOLDERS.append(item)
                scan(item) # Скануємо цю вкладену папку

            continue # Переходимо до наступного елементу в сканованій папці
        
        # ПРацюємо з файлом
        ext = get_extention(item.name) # Беремо розширення файлу
        full_name = folder / item.name # Берео повний шлях до файлу
        if not ext:
            MY_OTHERS.append(full_name)
        else:
            try:
                container = REGISTER_EXTESION[ext]
                EXTENTIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.set(ext)
                MY_OTHERS.append(full_name)

if __name__ == '__main__':
    folder_for_scan = sys.argv[1]

    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")

    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video jmov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")

    print(f"File doc: {DOC_FILE}")
    print(f"File docx: {DOCX_FILE}")
    print(f"File txt: {TXT_FILE}")
    print(f"File pdf: {PDF_FILE}")
    print(f"File xlsx: {XLSX_FILE}")
    print(f"File pptx: {PPTX_FILE}")

    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio mwav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")

    print(f"ARCHIVES: {ARCHIVES}")
    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')