import subprocess
import sys
from functools import partial
import basic_pitch
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication

from IHM import *


class EventHandler(QObject):
    def __init__(self, main_window):
        super().__init__()

        # Connecte les signaux de l'interface utilisateur aux fonctions de traitement correspondantes
        main_window.file_selector.select_file_button.clicked.connect(main_window.file_selector.open_file_dialog)
        main_window.file_selector.file_path_edit.textChanged.connect(
            partial(self.onFile_Selector_File_Path_Change, main_window))
        main_window.rythm_info.bpm_button.clicked.connect(
            partial(main_window.rythm_info.set_bpm, main_window.file_selector.file_path_edit.text))
        main_window.folder_selector.folder_path_edit.textChanged.connect(
            partial(self.onfolder_Selector_Folder_Path_Change, main_window))
        main_window.processing_options.isolate_tracks_checkbox.clicked.connect(partial(self.refresh_processing_options_checkbox,1,main_window))
        main_window.processing_options.two_stems_checkbox.clicked.connect(
            partial(self.refresh_processing_options_checkbox, 2, main_window))
        main_window.processing_options.four_stems_checkbox.clicked.connect(
            partial(self.refresh_processing_options_checkbox, 3, main_window))
        main_window.processing_options.five_stems_checkbox.clicked.connect(
            partial(self.refresh_processing_options_checkbox, 4, main_window))
        main_window.folder_selector.select_folder_button.clicked.connect(main_window.folder_selector.open_folder_dialog)
        main_window.folder_selector.folder_path_edit.textChanged.connect(
            partial(self.onfolder_Selector_Folder_Path_Change, main_window))
        main_window.process_button.process_button.clicked.connect(partial(self.split,main_window))
        main_window.file_selector_audio_to_midi.select_file_button.clicked.connect(main_window.file_selector_audio_to_midi.open_file_dialog)
        main_window.file_selector_audio_to_midi.file_path_edit.textChanged.connect(partial(self.file_selector_audio_to_midi_path_changed,main_window))
        main_window.process_audio_to_midi_button.process_button.clicked.connect(partial(self.convert_audio_to_midi,main_window))

        # Connecte le signal de changement d'option de traitement à la fonction de traitement correspondante
        # main_window.processing_options.processing_option_changed.connect(self.handle_processing_option_changed)
    def convert_audio_to_midi(self, main_window):
        print("conversion audio => MIDI")
        output_subfolder_path = main_window.folder_selector.folder_path_edit.text()
        audio_file_path = main_window.file_selector_audio_to_midi.file_path_edit.text()
        cmd = f'basic-pitch {output_subfolder_path} {audio_file_path}'
        subprocess.run(cmd, shell=True, capture_output=True)

    def file_selector_audio_to_midi_path_changed(self,main_window,args):
        print('debug 1')
        main_window.process_audio_to_midi_button.process_button.setEnabled(True)

    def refresh_processing_options_checkbox(self,choice, mainwindow):
        if choice == 1:
            if not(mainwindow.processing_options.isolate_tracks_checkbox.isChecked()):
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(False)
            elif mainwindow.processing_options.isolate_tracks_checkbox.isChecked():
                mainwindow.processing_options.two_stems_checkbox.setChecked(True)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(True)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(True)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(True)
        elif choice == 2:
            if mainwindow.processing_options.two_stems_checkbox.isChecked():
                mainwindow.processing_options.two_stems_checkbox.setChecked(True)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(True)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(True)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(True)
            else :
                mainwindow.processing_options.isolate_tracks_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(False)
        elif choice == 3:
            if mainwindow.processing_options.four_stems_checkbox.isChecked():
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(True)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
            else :
                mainwindow.processing_options.isolate_tracks_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(False)
        elif choice == 4:
            if mainwindow.processing_options.five_stems_checkbox.isChecked():
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setChecked(True)
            else :
                mainwindow.processing_options.isolate_tracks_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setChecked(False)
                mainwindow.processing_options.two_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.four_stems_checkbox.setChecked(False)
                mainwindow.processing_options.four_stems_checkbox.setEnabled(False)
                mainwindow.processing_options.five_stems_checkbox.setChecked(False)
                mainwindow.processing_options.five_stems_checkbox.setEnabled(False)
        mainwindow.folder_selector.select_folder_button.setEnabled(True)


    def onFile_Selector_File_Path_Change(self, main_window, args):
        main_window.processing_options.isolate_tracks_checkbox.setEnabled(True)
        main_window.file_info.update_file_info(main_window.file_selector.file_path_edit.text())

    def onfolder_Selector_Folder_Path_Change(self, main_window, args):
        main_window.process_button.process_button.setEnabled(True)

    def split(self, main_window):
        print("lancement")
        output_subfolder_path = main_window.folder_selector.folder_path_edit.text()
        audio_file_path = main_window.file_selector.file_path_edit.text()
        stems_nbr = 2
        isolate = True
        if not (main_window.processing_options.isolate_tracks_checkbox.isChecked()):
            isolate = False
        elif main_window.processing_options.two_stems_checkbox.isChecked():
            stems_nbr = 2
        elif main_window.processing_options.four_stems_checkbox.isChecked():
            stems_nbr = 4
        elif main_window.processing_options.five_stems_checkbox.isChecked():
            stems_nbr = 5
        if isolate:
            print("lancement du split")
            cmd = f'spleeter separate -p spleeter:{stems_nbr}stems -o {output_subfolder_path} {audio_file_path}'
            subprocess.run(cmd, shell=True,capture_output=True)
            main_window.file_selector_audio_to_midi.select_file_button.setEnabled(True)






if __name__ == "__main__":
    # Crée l'application Qt
    app = QApplication(sys.argv)

    # Crée la fenêtre principale
    main_window = MainWindow()
    event_handler = EventHandler(main_window)
    main_window.setWindowTitle("Cmlit v alpha 0.0.1")
    main_window.file_selector_audio_to_midi.select_file_button.setEnabled(False)
    # Affiche la fenêtre
    main_window.show()

    # Exécute l'application Qt en boucle
    sys.exit(app.exec())
