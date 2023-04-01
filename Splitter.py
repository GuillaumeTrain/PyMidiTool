import os
import spleeter
from IHM import MainWindow

def separate_instruments(main_window :MainWindow):
    # Créer un séparateur Spleeter avec les paramètres par défaut
    separator = spleeter.Separator('spleeter:2stems')
    audio_file_path = main_window.file_selector.file_path_edit.text()
    audio_filename = main_window.file_info.file_name
    output_folder_path = main_window.folder_selector.folder_path_edit.text()
    # Séparer les pistes audio avec Spleeter
    separator.separate_to_file(audio_file_path, output_folder_path)

    # Renommer les fichiers de sortie en fonction de l'instrument correspondant
    for file_name in os.listdir(output_folder_path):
        if file_name.endswith('.wav'):
            # Extraire le nom de l'instrument à partir du nom de fichier
            instrument_name = file_name.split(' - ')[1].split('.')[0]
            # Renommer le fichier avec le nom de l'instrument
            os.rename(os.path.join(output_folder_path, file_name), os.path.join(output_folder_path, f'{instrument_name}.wav'))
