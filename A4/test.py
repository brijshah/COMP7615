import wave, argparse, warnings
from pydub import AudioSegment

#increase/decrease
def volume():
	song = AudioSegment.from_wav('pants.wav')

	#reduce volume by 10dB
	song_10_db_quieter = song + 10

	#very quiet
	song = song - 36

	#save
	song.export('quiet.wav', 'wav')

def blend():
	sound1 = AudioSegment.from_file('pants.wav')
	sound2 = AudioSegment.from_file('thankyou.wav')

	combined = sound1.overlay(sound2)
	combined.export('combined.wav', format='wav')

def main():
	volume()

if __name__ == '__main__':
	main()

