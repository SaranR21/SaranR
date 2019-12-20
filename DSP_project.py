import wavio as w
import numpy as np

import scipy.fftpack as sfp
import matplotlib.pyplot as plt


from pydub import AudioSegment




sound1 = AudioSegment.from_file("/home/saran/Downloads/Shriram.wav")
sound2 = AudioSegment.from_file("/home/saran/Downloads/Rishita.wav")

combined = sound1.overlay(sound2)

combined.export("/home/saran/Downloads/frs.wav", format='wav')

f_combined = combined.get_array_of_samples()
f_shriram = sound1.get_array_of_samples()
f_rishita = sound2.get_array_of_samples()


F_C = sfp.fft(f_combined)
F_S = sfp.fft(f_shriram)
F_R = sfp.fft(f_rishita)

fig, axes=plt.subplots(nrows=3, ncols=1)
axes[0].stem(F_C[:5000])
axes[1].stem(F_S[:5000])
axes[2].stem(F_R[:5000])

