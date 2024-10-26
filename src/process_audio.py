"""_summary_

    Returns:
        _type_: _description_
"""
import os
import librosa
import numpy as np
from scipy.signal import decimate
from scipy.io.wavfile import write


def sound_vector(file_audio):
    """_summary_

    Args:
        file_audio (_type_): arquivo de audio

    Returns:
        _type_: vetor com o valor de amostras
    """
    audio_path = file_audio
    vetor, sample_rate = librosa.load(audio_path, sr=None)

    # Exibir algumas informações
    print(f"Tamanho do vetor: {len(vetor)} Taxa de amostragem: {sample_rate} Hz")
    return vetor, sample_rate

def interpolar_vetor_numpy(vetor, novo_tamanho):
    """_summary_

    Args:
        vetor (_type_): _description_
        novo_tamanho (_type_): _description_

    Returns:
        _type_: _description_
    """
    x_original = np.linspace(0, 1, len(vetor))
    x_novo = np.linspace(0, 1, novo_tamanho)
    return np.interp(x_novo, x_original, vetor)


def downsample_decimate(vetor, fator):
    """_summary_

    Args:
        vetor (_type_): _description_
        fator (_type_): _description_

    Returns:
        _type_: _description_
    """
    return decimate(vetor, fator, ftype='iir')


def salvar_audio(vetor, taxa_amostragem, nome_arquivo):
    """_summary_

    Args:
        vetor (_type_): _description_
        taxa_amostragem (_type_): _description_
        nome_arquivo (_type_): _description_
    """
    # Normalizar e converter para int16 (padrão para áudio PCM)
    vetor_normalizado = (vetor / np.max(np.abs(vetor)) * 32767).astype(np.int16)

    # Salvar o áudio
    write(nome_arquivo, taxa_amostragem, vetor_normalizado)
    print(f"Áudio salvo como: {nome_arquivo}")

ROOT_FILE_4k = os.getcwd()[0:48]+'audio/4khz.wav'
ROOT_FILE_8k = os.getcwd()[0:48]+'audio/8khz.wav'
ROOT_FILE_16k = os.getcwd()[0:48]+'audio/16khz.wav'

vetor_4k, sample_rate_4k = sound_vector(file_audio=ROOT_FILE_4k)
vetor_8k, sample_rate_8k = sound_vector(file_audio=ROOT_FILE_8k)
vetor_16k, sample_rate_16k = sound_vector(file_audio=ROOT_FILE_16k)

new_vetor_4k = interpolar_vetor_numpy(vetor_4k, len(vetor_8k))
print(f'antes={len(vetor_4k)} depois={len(new_vetor_4k)}')

new_vetor_16k = downsample_decimate(vetor_16k, 2)
print(f'antes={len(vetor_16k)} depois={len(new_vetor_16k)}')

salvar_audio(new_vetor_4k, 4000, 'new_4khz.wav')
