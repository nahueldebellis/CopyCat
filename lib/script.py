#import the pyplot and wavfile modules 

import matplotlib.pyplot as plot

from scipy.io import wavfile


# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read('Do.wav')
a = signalData[::4]
a = a[:,1]
print(samplingFrequency)

for n in range(nFrames):
	xFrame[:,n] = x[start:start+nfft] 
	start = start + nfft - hop_size 
	timestamp[n] = n*(nfft-hop_size)/fs
	chroma[:,n] = compute_chroma(xFrame[:,n],fs)


	"""Correlate 12D chroma vector with each of 24 major and minor chords"""
	cor_vec = np.zeros(24)
	for ni in range(24):
		cor_vec[ni] = np.correlate(chroma[:,n], np.array(templates[ni])) 
	max_cor[n] = np.max(cor_vec)
	id_chord[n] =  np.argmax(cor_vec) + 1
    

# Plot the signal read from wav file

plot.subplot(211)

plot.title('Spectrogram of a wav file with piano music')

 

plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

 

plot.subplot(212)
plot.specgram(a, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

 

plot.show()
'''import scipy.io.wavfile as waves

def compara(sonido, sonido2):
	for item_a, item_b in zip(sonido, sonido2):
		for a, b in zip(item_a, item_b):
			if a != b:
			    return 'distintos'
	return 'iguales'


archivo = input('archivo de sonido:' )
muestreo, sonido = waves.read(archivo)
print(sonido)
archivo2 = input('segundo archivo: ')
muestra, sonido2 = waves.read(archivo2)
print(compara(sonido, sonido2))

# canales: monofónico o estéreo
tamano = np.shape(sonido)
muestras = tamano[0]

m = len(tamano)
canales = 1  # monofónico
if (m>1):  # estéreo
    canales = tamano[1]
# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = sonido[:,canal] 
else:
    uncanal = sonido
print(len(uncanal))
# rango de observación en segundos
inicia = 1.000
termina = 2.002
# observación en número de muestra
a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = uncanal[a:b]
# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
waves.write('parte01.wav', muestreo, parte)'''

