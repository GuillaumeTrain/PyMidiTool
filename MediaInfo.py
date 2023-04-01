import librosa as librosa
from pydub.utils import mediainfo
import librosa

def get_media_info(filepath):
    info = mediainfo(filepath)
    return info

def get_bpm(audio_file_path):
    # Charger le fichier audio et extraire les caractéristiques audio avec librosa
    y, sr = librosa.load(audio_file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # Estimer le tempo en bpm avec la fonction de détection de battement de librosa
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    return tempo