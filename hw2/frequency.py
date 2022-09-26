#!/usr/bin/env python3

import audio
import numpy as np

def change_frequency():
    # The playback frequency is determined by the sampling frequency
    # let's set that we want to have a wave of 200Hz sampled at 40kHz 
    # and we want to play it back at 300Hz. Then
    duration = 3

    # Input
    fsi = 40000
    fi = 200

    # Create the input
    nsamples = duration * fsi
    x = np.arange(0, nsamples)
    samples = list(np.sin(2 * np.pi * (fi / fsi) * x))

    # Let's write the output
    audio.write_audio_file('input-sample.wav', samples, fsi)

    # Output
    fo = 300

    # Based on the fact we can change the sampling frequency
    # 40000 -> 200 Hz then fso -> fo
    # fso = fo * fsi / fi
    fso = fo * fsi / fi
    print(f"FSI: {fsi} Hz FSO: {fso} Hz")

    # Let's write the output (resampled)
    audio.write_audio_file('resampled-sample.wav', samples, fso)

    # Play back both
    print(f"Input: {fi} Hz")
    audio.play_audio('input-sample.wav')
    print(f"Resampled: {fo} Hz")
    audio.play_audio('resampled-sample.wav')

if __name__ == "__main__":
    change_frequency()
