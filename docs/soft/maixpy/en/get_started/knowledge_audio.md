---
title: Audio processing background knowledge
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: audio processing background knowledge
---


## What is sound (audio)

> People are rational, and the world is emotional.

What is audio, audio is vibration.
The vibration of light particles forms light waves, namely light;

And the vibration of universal objects forms sound waves, that is, sound

## Audio coding basics

- Number of channels (number of channels)

That is, the number of sound channels. When recording the sound, simultaneously record the audio of different spatial positions, that is, record multi-channel audio;

Common audio files are divided into mono and stereo, that is, mono records audio at a single location, while stereo has left and right channels to record audio at different spatial locations, and can play different channels of audio through different speakers. In this way, the audio of different spatial positions is restored, and the human ear can feel the different spatial positions through audio (more spatial sense).

- Number of sampling bits

That is, the sampling value or sampling value (that is, the sampling sample amplitude is quantized). It is a parameter used to measure the fluctuation of sound, and it can also be said to be the resolution of the sound card. The larger its value, the higher the resolution and the stronger the sound power.

The number of sampling bits in a computer is generally divided into 8 bits and 16 bits, but please note that 8 bits does not mean dividing the ordinate into 8 parts, but divided into 2 to the 8th power, which is 256 parts; the same is true for 16 bits. It divides the ordinate into 2 to the 16th power of 65536.

- Sampling frequency

That is, the sampling frequency, which refers to the number of times a sound sample is obtained per second. The higher the sampling frequency, the better the sound quality, and the more realistic the sound reproduction, but at the same time it occupies more resources. Due to the limited resolution of the human ear, too high a frequency cannot be distinguished. In the 16-bit sound card, there are 22KHz, 44KHz, etc., of which 22KHz is equivalent to the sound quality of ordinary FM broadcasting, and 44KHz is equivalent to the sound quality of CD. The current common sampling frequency does not exceed 48KHz.

## PCM of audio encoding processing

PCM introduction

At present, we all need to rely on audio files for audio playback on computers. The generation process of audio files is the process of sampling, quantizing and encoding sound information. The lowest frequency of the sound that human ears can hear is from From 20Hz to the highest frequency 20Khz, so the maximum bandwidth of the audio file format is 20Kzh. According to Nyquist's theory, only when the sampling frequency is higher than twice the highest frequency of the sound signal, can the sound represented by the digital signal be restored to the original sound, so the sampling rate of the audio file is generally 40~50KHZ, such as the most common The CD sound quality sampling rate is 44.1KHZ.

The process of sampling and quantizing the sound is called Pulse Code Modulation, or PCM for short. From the above three concepts of sampling frequency, number of sampling bits, and number of channels, the three concepts can be derived from the following formula. PCM file in the computer The amount of storage space occupied:

PCM audio data size = (sampling frequency * number of sampling bits * channel * time)//8 (unit: Bytes).

Since PCM data is the most primitive audio data, it is completely lossless to the sampled data. Although PCM data has excellent sound quality, its volume is still too large for computer storage. In order to solve this problem, a series of audio formats have been born. These audio formats use Different methods are used to compress audio data, including lossless compression (ALAC, APE, FLAC) and lossy compression (MP3, AAC, OGG, WMA).

## WAV

Waveform Audio File Format (WAVE, or WAV known by the public because of its extension) is an encoding format developed by Microsoft and IBM to store audio streams on personal computers. The application software on the Windows platform is widely supported. The status is similar to AIFF in Macintosh computers. This format is one of the applications of the Resource Exchange File Format (RIFF), and the audio data modulated by pulse code is usually stored in blocks. It is also one of the designated specifications commonly used among music enthusiasts. Since this audio format is not compressed, there will be no distortion in sound quality, but the volume of the file is larger among many audio formats.

All WAVs have a file header, which is the encoding parameter of the audio stream. WAV has no hard and fast rules on the encoding of audio streams. In addition to PCM, almost all encodings that support the ACM specification can encode WAV audio streams. WAV can also use a variety of audio encodings to compress its audio stream, but we are usually WAV whose audio stream is encoded by PCM, but this does not mean that WAV can only use PCM encoding. MP3 encoding can also be used in WAV. Like AVI, as long as the corresponding Decode is installed, you can enjoy these WAVs.

Under the Windows platform, WAV based on PCM encoding is the best supported audio format. All audio software can perfectly support it. Because it can meet the requirements of higher sound quality, WAV is also the preferred format for music editing and creation. Suitable for saving music material. Therefore, WAV based on PCM encoding is used as an intermediary format, which is often used in the mutual conversion of other encodings, such as converting MP3 to WMA.

**In MaixPy, the WAV file format supported by the aduio module is PCM_s16le (signed 16 bits little endian, signed 16 bits little endian)**
