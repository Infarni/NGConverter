import os

from pathlib import Path


BASE_DIR = Path(__file__).parent

FORMATS = [
    '.docx',
    '.odt',
    '.pdf'
]

MEDIA_DIR = os.path.join(BASE_DIR, 'media/')
