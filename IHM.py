import os

from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QProgressBar, QFileDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QHBoxLayout, QCheckBox, QGroupBox, QFormLayout, QListWidget, QListWidgetItem, QMainWindow
import MediaInfo

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()

        # Crée un champ de texte pour afficher le chemin du fichier sélectionné
        self.file_path_edit = QLineEdit()
        self.file_path_edit.setReadOnly(True)
        self.file_path = None
        # Crée un bouton pour ouvrir une boîte de dialogue de sélection de fichier
        self.select_file_button = QPushButton('Sélectionner un fichier...')
#        self.select_file_button.clicked.connect(self.open_file_dialog())


        # Ajoute les éléments à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_edit)
        layout.addWidget(self.select_file_button)
        self.setLayout(layout)

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Sélectionner un fichier audio')
        self.file_path_edit.setText(self.file_path)
        self.file_path = self.file_path_edit.text()
        #self.file_path_edit.textChanged.connect(update_file_info())


class RythmInfo(QWidget):
    def __init__(self):
        super().__init__()

        # Crée un label pour afficher les informations de tempo en bpm
        self.bpm_button = QPushButton("analyser le tempo du fichier")
        self.bpm_label = QLabel('Tempo : -')

        # Ajoute le label à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.bpm_button)
        layout.addWidget(self.bpm_label)
        self.setLayout(layout)

    def set_bpm(self,file_path):
        print("file",file_path())
        bpm=MediaInfo.get_bpm(file_path())
        self.bpm_label.setText('Tempo : {} bpm'.format(bpm))


class AudioPlayer(QWidget):
    def __init__(self, audio_path):
        super().__init__()

        # Crée un lecteur audio pour jouer le fichier audio
        self.player = QMediaPlayer()
        self.player.setsetMedia(QUrl.fromLocalFile(audio_path))

        # Crée un label pour afficher le nom de la piste audio
        self.track_label = QLabel('Piste audio')

        # Crée des boutons pour jouer et arrêter la piste audio
        self.play_button = QPushButton('Play')
 #       self.play_button.clicked.connect(self.player.play)
        self.stop_button = QPushButton('Stop')
#        self.stop_button.clicked.connect(self.player.stop)

        # Ajoute les éléments à une mise en page horizontale
        layout = QHBoxLayout()
        layout.addWidget(self.track_label)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)


class ProcessButton(QWidget):
    def __init__(self):
        super().__init__()

        # Crée un bouton pour lancer le traitement du fichier audio
        self.process_button = QPushButton('Traiter le fichier')
        self.process_button.setEnabled(False)  # Désactive le bouton tant qu'aucun fichier n'a été sélectionné

        # Ajoute le bouton à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.process_button)
        self.setLayout(layout)
    def set_disabled(self):
        self.process_button.setEnabled(False)
    def set_enabled(self):
        self.process_button.setEnabled(True)


class ProcessingOptions(QWidget):
    def __init__(self):
        super().__init__()

        # Crée une case à cocher pour activer/désactiver l'isolation des pistes
        self.isolate_tracks_checkbox = QCheckBox('Isoler piste')
        self.isolate_tracks_checkbox.setChecked(False)
        self.isolate_tracks_checkbox.setEnabled(False)
        self.two_stems_checkbox = QCheckBox('Voix/Accompagnement')
        self.two_stems_checkbox.setChecked(False)
        self.two_stems_checkbox.setEnabled(False)
        self.four_stems_checkbox = QCheckBox('Voix/Percussions/Basse/Autres')
        self.four_stems_checkbox.setChecked(False)
        self.four_stems_checkbox.setEnabled(False)
        self.five_stems_checkbox = QCheckBox('Voix/Percussions/Basse/Piano/Autres')
        self.five_stems_checkbox.setChecked(False)
        self.five_stems_checkbox.setEnabled(False)
        # Crée une boîte pour regrouper les options de traitement
        options_groupbox = QGroupBox('Options de traitement')
        options_layout = QFormLayout()
        options_layout.addRow(self.isolate_tracks_checkbox)
        options_layout.addRow(self.two_stems_checkbox)
        options_layout.addRow(self.four_stems_checkbox)
        options_layout.addRow(self.five_stems_checkbox)
        options_groupbox.setLayout(options_layout)

        # Ajoute la boîte d'options à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(options_groupbox)
        self.setLayout(layout)

    def isolate_tracks(self):
        return self.isolate_tracks_checkbox.isChecked()


class AudioTrackList(QWidget):
    def __init__(self):
        super().__init__()

        # Crée une liste pour afficher les pistes audio isolées
        self.track_list = QListWidget()

        # Ajoute la liste à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.track_list)
        self.setLayout(layout)

    def add_track(self, track_name, track_path):
        item = QListWidgetItem(track_name)
        item.setToolTip(track_path)
        self.track_list.addItem(item)


class FolderSelector(QWidget):
    def __init__(self):
        super().__init__()

        # Crée un champ de texte pour afficher le chemin du dossier sélectionné
        self.folder_path_edit = QLineEdit()
        self.folder_path_edit.setReadOnly(True)

        # Crée un bouton pour ouvrir une boîte de dialogue de sélection de dossier
        self.select_folder_button = QPushButton('Sélectionner un dossier...')
        self.select_folder_button.setEnabled(False)

        # Ajoute les éléments à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.folder_path_edit)
        layout.addWidget(self.select_folder_button)
        self.setLayout(layout)
    def setenabled(self):
        self.select_folder_button.setEnabled(True)
    def setdisabled(self):
        self.select_folder_button.setEnabled(False)
    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Sélectionner un dossier de sortie')
        self.folder_path_edit.setText(folder_path)


class FileInfo(QLabel):
    def __init__(self):
        super().__init__()
        self.file_name = None
        self.file_size = None
        self.media_info = None
        self.codec = None
        self.sample_rate = None
        self.channels = None
    def set_info(self):
        self.setText(f"Nom du fichier : {self.file_name}\nTaille du fichier : {self.file_size} octets\nCodecs: {self.codec}\nSample rate: {self.sample_rate}\nNumber of Channels: {self.channels}")
    def update_file_info(self,file_path):
        path = file_path
        print ("file:",path)
        # Met à jour les informations sur le fichier sélectionné
        self.file_name = os.path.basename(path)
        self.file_size = os.path.getsize(path)
        self.media_info = MediaInfo.get_media_info(path)
        self.codec = self.media_info["codec_name"]
        self.sample_rate = self.media_info["sample_rate"]
        self.channels = self.media_info["channels"]
        print(MediaInfo.get_media_info(path))
        self.set_info()

        # Active le bouton de traitement
        #self.process_button.set_enabled(True)

class ProgressWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crée une barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)

        # Ajoute la barre de progression à une mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def set_progress(self, value):
        self.progress_bar.setValue(value)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crée les différents éléments de l'interface utilisateur
        self.file_selector = FileSelector()
        self.file_info = FileInfo()
        self.rythm_info = RythmInfo()
        self.processing_options = ProcessingOptions()
        self.folder_selector = FolderSelector()
        self.process_button = ProcessButton()
        self.file_selector_audio_to_midi = FileSelector()
        self.process_audio_to_midi_button = ProcessButton()
        self.track_list = AudioTrackList()


        # Ajoute les éléments à une mise en page verticale
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.file_selector)
        layout.addWidget(self.file_info)
        layout.addWidget(self.rythm_info)
        layout.addWidget(self.processing_options)
        layout.addWidget(self.folder_selector)
        layout.addWidget(self.process_button)
        layout.addWidget(self.file_selector_audio_to_midi)
        layout.addWidget(self.process_audio_to_midi_button)
        layout.addWidget(self.track_list)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connecte les signaux et les slots
        #self.file_selector.on_file_selected(self.update_file_info)
#        self.process_button.on_click(self.process_file)



    def process_file(self):
        # Désactive le bouton de traitement
        self.process_button.set_enabled(False)

        # Récupère les options de traitement
        isolate_tracks = self.processing_options.isolate_tracks()

        # TODO : Traiter le fichier audio en utilisant les options sélectionnées

        # Met à jour la liste des pistes audio isolées
        if isolate_tracks:
            self.track_list.add_track('Piste 1', '/chemin/vers/piste_1.wav')
            self.track_list.add_track('Piste 2', '/chemin/vers/piste_2.wav')