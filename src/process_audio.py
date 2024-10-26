import os
import librosa
import numpy as np


def sound_vector(file_audio):
    """_summary_

    Args:
        file_audio (_type_): _description_

    Returns:
        _type_: _description_
    """
    audio_path = file_audio
    y, sr = librosa.load(audio_path, sr=None)

    # Exibir algumas informações
    print(f"Vetor de valores (primeiros 10): {y[:10]}")
    print(f"Tamanho do vetor: {len(y)}")
    print(f"Taxa de amostragem: {sr} Hz")

    # Normalizar o áudio (opcional)
    y_normalizado = y / np.max(np.abs(y))

    print(f"Vetor normalizado (primeiros 10): {y_normalizado[:10]}")
    
    return y, sr


ROOT_FILE_4k = os.getcwd()[0:48]+'audio/4khz.wav'
ROOT_FILE_8k = os.getcwd()[0:48]+'audio/8khz.wav'
ROOT_FILE_16k = os.getcwd()[0:48]+'audio/16khz.wav'

y_4k, sr_4k = sound_vector(file_audio=ROOT_FILE_4k)
y_8k, sr_8k = sound_vector(file_audio=ROOT_FILE_8k)
y_16k, sr_16k = sound_vector(file_audio=ROOT_FILE_16k)

    