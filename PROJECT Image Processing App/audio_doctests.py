import numpy as np
from pydub import AudioSegment

import project

def reverse_song_test():
    """
    Checks the output of reverse_song() for PremiumPlusMultimediaProcessing

    >>> reverse_song_test()
    True
    """
    multi_proc = project.PremiumPlusMultimediaProcessing()
    audio = project.audio_read_helper('audio/one_summers_day.wav')
    audio_reversed = multi_proc.reverse_song(audio)
    audio_exp = project.audio_read_helper('audio/exp/one_summers_day_reversed.wav')
    project.audio_save_helper('audio/out/one_summers_day_reversed.wav', audio_reversed)
    return audio_reversed.wave == audio_exp.wave

def slow_down_test():
    """
    Checks the output of slow_down() for PremiumPlusMultimediaProcessing

    >>> slow_down_test()
    True
    """
    multi_proc = project.PremiumPlusMultimediaProcessing()
    audio = project.audio_read_helper('audio/one_summers_day.wav')
    audio_slow = multi_proc.slow_down(audio, 2)
    audio_exp = project.audio_read_helper('audio/exp/one_summers_day_slow.wav')
    project.audio_save_helper('audio/out/one_summers_day_slow.wav', audio_slow)
    return audio_slow.wave == audio_exp.wave

def speed_up_test():
    """
    Checks the output of speed_up() for PremiumPlusMultimediaProcessing

    >>> speed_up_test()
    True
    """
    multi_proc = project.PremiumPlusMultimediaProcessing()
    audio = project.audio_read_helper('audio/one_summers_day.wav')
    audio_sped_up = multi_proc.speed_up(audio, 2)
    audio_exp = project.audio_read_helper('audio/exp/one_summers_day_sped_up.wav')
    project.audio_save_helper('audio/out/one_summers_day_sped_up.wav', audio_sped_up)
    return audio_sped_up.wave == audio_exp.wave

def reverb_test():
    """
    Checks the output of reverb() for PremiumPlusMultimediaProcessing

    >>> reverb_test()
    True
    """
    multi_proc = project.PremiumPlusMultimediaProcessing()
    audio = project.audio_read_helper('audio/one_summers_day.wav')
    audio_reverb = multi_proc.reverb(audio)
    audio_exp = project.audio_read_helper('audio/exp/one_summers_day_reverb.wav')
    project.audio_save_helper('audio/out/one_summers_day_reverb.wav', audio_reverb)
    return audio_reverb.wave == audio_exp.wave

def clip_test():
    """
    Checks the output of clip_song() for PremiumPlusMultimediaProcessing

    >>> clip_test()
    True
    """
    multi_proc = project.PremiumPlusMultimediaProcessing()
    audio = project.audio_read_helper('audio/one_summers_day.wav')
    audio_clipped = multi_proc.clip_song(audio, 30, 70)
    audio_exp = project.audio_read_helper('audio/exp/one_summers_day_clipped.wav')
    project.audio_save_helper('audio/out/one_summers_day_clipped.wav', audio_clipped)
    return audio_clipped.wave == audio_exp.wave

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)