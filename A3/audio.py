import wave, argparse

#-----------------------------------------------
#-- Source File:	audio.py - reverse audio
#
#-- Programmers:	Brij Shah & Callum Styan
#
#-- Date:			October 4, 2015
#-----------------------------------------------

parser = argparse.ArgumentParser(description='Steganography')
parser.add_argument('-o', '--output', dest='outputFile', help='the output file', required=True)
parser.add_argument('-i', '--input', dest='inputFile', help='the input file', required=True)
parser.add_argument('-u', '--speedup', dest='speedUp', help='fast forward the file')
parser.add_argument('-d', '--slowdown', dest='slowDown', help='slow down the file')
parser.add_argument('-r', '--reversal', action="store_true", help='play audio reversed')
args = parser.parse_args()

if args.speedUp and args.slowDown:
	print "Sorry, you can't speed up and slow down.  Please only set one of those flags"
	exit()

def main():
	#open wave file for reading
	w = wave.open(args.inputFile, 'r')

	#open wave file for writing to
	openWaveFile = wave.open(args.outputFile, 'w')

	#returns sample width in bytes
	sampRate = w.getsampwidth()

	#returns sampling frequency
	frameRate = w.getframerate()

	#sets the frame rate to n
	openWaveFile.setframerate(frameRate)

	#set sample width to n bytes
	openWaveFile.setsampwidth(sampRate)

	#returns number of audio channels(1 for mono 2 for stereo)
	channels = w.getnchannels()

	#set the number of channels
	openWaveFile.setnchannels(channels)

	#empty string
	writeframes = ""

	if args.reversal == True:
		#loop through frames and assign each frame to the reversedframe variable
		for i in range(w.getnframes()):
			frame = w.readframes(1)
			writeframes = frame + writeframes
	else:
		writeframes = w.readframes(w.getnframes())

	#write reversed frames to wav file
	if args.speedUp is not None:
		openWaveFile.setframerate(int(round(openWaveFile.getframerate() * float(args.speedUp))))
	elif args.slowDown is not None:
		openWaveFile.setframerate(int(round(openWaveFile.getframerate() / float(args.slowDown))))
	openWaveFile.writeframes(writeframes)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "Exiting.."
	except IOError:
		print "file not found, try again.."



