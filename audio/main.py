import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
# from datetime import datetime


def record_sound(sample_rate, time_second):
    """_summary_

    Args:
        sample_rate (_type_): _description_
        time_second (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Parâmetros de gravação    
    fs = sample_rate    
    seconds = time_second
    print("Gravando...")
    # Grava o áudio
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Espera a gravação finalizar
    time = np.linspace(0, seconds, num=len(audio))  # Eixo do tempo
    # Salva o áudio no formato WAV
    # now = datetime.now()
    # timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    # name_file_audio = f'gravacao.wav'+'_'+str(timestamp)
    write("16khz.wav", fs, np.int16(audio * 32767))
    print("Gravação finalizada e salva como 'gravacao.wav'")
    return audio, time


def plot_sound(audio, time):
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio, label="Sinal de Áudio")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.title("Forma de Onda do Sinal Gravado")
    plt.legend()
    plt.grid(True)
    # Salvando o gráfico como PNG
    output_file = "16khz.png"
    plt.savefig(output_file, format='png', dpi=300)
    print(f"Gráfico salvo como '{output_file}'")
    # Exibindo o gráfico
    plt.show()
    


audio, time = record_sound(time_second=5, sample_rate=16000)
plot_sound(audio, time)
