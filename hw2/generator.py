#!/usr/bin/env python3

import audio
import numpy as np
import sys



def generate_440Hz(loc='input.wav'):
    # The number of samples per period is given by the quotient of fs/f
    # since f = periods/s, and fs = samples/s. Then fs/f = samples/period
    duration = 3

    # Input
    fi = 440

    # Compute the sampling rate
    fsi = 44100

    # Log info
    print("Generating:")
    print(f"Sine frequency: {fi} Hz")
    print(f"Samples per period: {fsi / fi}")
    print(f"Sampling Frequency: {fsi} Hz")

    # Create the input
    nsamples = duration * fsi
    x = np.arange(0, nsamples)
    samples = list(np.sin(2 * np.pi * (fi / fsi) * x))

    # Let's write the output
    audio.write_audio_file(loc, samples, fsi)

    # Play back both
    print("Playing the input wave")
    audio.play_audio(loc)

def resample_440Hz(samples_per_period, inputloc='input.wav', outputloc='output.wav'):
    # The number of samples per period is given by the quotient of fs/f
    # since f = periods/s, and fs = samples/s. Then fs/f = samples/period
    duration = 3

    # Input
    fi = 440

    # Compute the sampling rate
    fso = samples_per_period * fi

    # Log info
    print(f"Sine frequency: {fi} Hz")
    print(f"Samples per period: {samples_per_period}")
    print(f"Computed Sampling Frequency: {fso} Hz")

    # Read the input
    # Read audio file
    samples, _ = audio.read_audio_file(inputloc)

    # Let's write the output
    audio.write_audio_file(outputloc, samples, fso)

    # Play back both
    print("Playing the output wave")
    audio.play_audio(outputloc)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: this function requires an argument")
        print("Usage:")
        print("\t./generator.py SAMPLES_PER_PERIOD")
    else:
        generate_440Hz()
        resample_440Hz(float(sys.argv[1]))
