# video-summary-generator

The main purpose of this project is to generate a summary of a video.

The project consists of 3 main modules namely video_to_wav.py, wav_to_text.py
and Text_summarization.py.
The video which is required to be in MP4 format as of version 1.0 is provided to the
video to wav module which 1 st converts the video to mp3 file and then uncompress
the mp3 file to generate wav file. The wav file generated is then sends to wav_to_text
module which breaks down the audio file into small chunks and sends it to Google
Cloud API that converts the audio into broken sentences, these broken sentences are
then integrated to generate proper meaningful sentences and appended to a text file.
As soon as the text file is generated the Custom made Text summarization module
fetches it and performs text summarization. The module performs 5 tasks : Text
Cleaning, Sentence Tokenization, Word Tokenization, Word-frequency table
generation and finally summarization.

