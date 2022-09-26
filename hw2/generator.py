#!/usr/bin/env python3

import audio
import numpy as np
import sys


def generate_440Hz(samples_per_period):
    # The number of samples per period is given by the quotient of fs/f
    # since f = periods/s, and fs = samples/s. Then fs/f = samples/period
    duration = 3

    # Input
    fi = 440

    # Compute the sampling rate
    fsi = samples_per_period * fi

    # Log info
    print(f"Sine frequency: {fi} Hz")
    print(f"Samples per period: {samples_per_period}")
    print(f"Computed Sampling Frequency: {fsi} Hz")

    # Create the input
    nsamples = duration * fsi
    x = np.arange(0, nsamples)
    samples = list(np.sin(2 * np.pi * (fi / fsi) * x))

    # Let's write the output
    audio.write_audio_file('sample.wav', samples, fsi)

    # Play back both
    print("Playing the wave")
    audio.play_audio('sample.wav')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: this function requires an argument")
        print("Usage:")
        print("\t./generator.py SAMPLES_PER_PERIOD")
    else:
        generate_440Hz(float(sys.argv[1]))
