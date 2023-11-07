# Required library: google-cloud-storage and google

# Import packages
from google.cloud import storage
import os

# Set key credentials file path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'archive.json'


def list_cs_files(bucket_name): 
    """
    Lista los archivos en un bucket de Google Cloud Storage.

    Esta función utiliza la biblioteca de cliente de Google Cloud Storage
    para listar los nombres de archivos en el bucket especificado.

    Parameters
    ----------
    bucket_name : str
        Nombre del bucket de Google Cloud Storage.

    Returns
    -------
    list
        Lista de nombres de archivos en el bucket especificado.
    """
    storage_client = storage.Client()

    file_list = storage_client.list_blobs(bucket_name)
    file_list = [file.name for file in file_list]

    return file_list


def download_cs_file(bucket_name, file_name, destination_file_name): 
    """
    Descarga un archivo desde un bucket de Google Cloud Storage.

    Esta función utiliza la biblioteca de cliente de Google Cloud Storage
    para descargar un archivo específico desde el bucket especificado.

    Parameters
    ----------
    bucket_name : str
        Nombre del bucket de Google Cloud Storage.
    file_name : str
        Nombre del archivo en el bucket que se va a descargar.
    destination_file_name : str
        Ruta del sistema de archivos donde se guardará el archivo descargado.

    Returns
    -------
    bool
        Devuelve True si la descarga se realiza correctamente, 
        False en caso contrario.
    """
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_file_name)

    return f'El archivo {file_name} se descargo correctamente'


def upload_cs_file(bucket_name, source_file_name, destination_file_name):
    """
    Sube un archivo al bucket de Google Cloud Storage.

    Esta función utiliza la biblioteca de cliente de Google Cloud Storage
    para cargar un archivo desde el sistema de archivos local al bucket especificado.

    Parameters
    ----------
    bucket_name : str
        Nombre del bucket de Google Cloud Storage.
    source_file_name : str
        Ruta del sistema de archivos del archivo que se va a subir.
    destination_file_name : str
        Nombre del archivo en el bucket al que se subirá el archivo.

    Returns
    -------
    bool
        Devuelve True si la carga se realiza correctamente, False en caso contrario.
    """ 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return f'El archivo {destination_file_name} se subió correctamente'



