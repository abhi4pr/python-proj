from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/files',
    tags=['file']
)

@router.post('/uploadfile')
def upload_file(upload_file: UploadFile = File(...)):
    path = f"uploaded_files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return{
        'filename': path
    }

# to download file 
@router.get('/download_file/{name}', response_class=FileResponse)
def get_file(name: str):
    path = f'uploaded_files/{name}'
    return path