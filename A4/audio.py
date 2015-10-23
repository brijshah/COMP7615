#!/usr/bin/python

#-----------------------------------------------------------------------------
#--	SOURCE FILE:	audio.py -   audio song generator
#--
#--	FUNCTIONS:		createBackground(song)
#--					prettyGirls(song)
#--					ohYeah(song)
#--					mars(song)					
#--					drums(song)
#--					delete(song)
#--					main()															
#--
#--	DATE:			October 12, 2015
#--
#--	PROGRAMMERS:	Brij Shah & Callum Styan
#--
#--	NOTES:
#--	
#-----------------------------------------------------------------------------

import wave, argparse, warnings, os
from pydub import AudioSegment

# globals
background = None
prettyGirls = None
ohyeahs = None
marsOyeah = None
girlsPretty = None

# open song
song = AudioSegment.from_wav('bspears.wav')

# create background beat
def createBackground(song):
	global background
	background = song[2600:5000]
	background = background.append(background)
	background = background * 50
	background_reverse = background.reverse()
	background_reverse = background_reverse
	background_reverse = background_reverse.apply_gain(-25.0)
	background = background.overlay(background_reverse)
	background = background.fade_in(8800).fade_out(8800)
	background.export('background.wav', 'wav')

# creates snippet from song given and fades in
def prettyGirls(song):
	global prettyGirls
	prettyGirls = song[12050:14800]
	prettyGirls = prettyGirls.fade_in(1500)

# creates snippet from song given
# applies gain to the same snippet 
# creates three snippets with different volume
def ohYeah(song):
	global oyeahs
	oyeah = song[121800:122400]
	quietest = oyeah.apply_gain(-20)
	quieter = oyeah.apply_gain(-12.5)
	quiet = oyeah.apply_gain(-5)
	oyeahs = oyeah.append(quiet).append(quieter).append(quietest)
	oyeahs.export('oyeah.wav', 'wav')

# creates snippet from song given
# opens another snippet from opened wave file
# attaches two snippets 
def mars(song):
	global marsOyeah
	silent5 = AudioSegment.silent(duration=22000)
	mars = song[78000:80500]
	mars.export('mars.wav', 'wav')
	mars = wave.open('mars.wav', 'r')
	marsFast = wave.open('marsFast.wav', 'w')
	marsFast.setparams(mars.getparams())
	writeFrames = mars.readframes(mars.getnframes())
	marsFast.setframerate(int(round(mars.getframerate() * 1.25)))
	marsFast.writeframes(writeFrames)
	marsFast.close()
	marsFast = AudioSegment.from_wav('marsFast.wav')
	marsOyeah = silent5.append(marsFast).append(oyeahs).append(silent5)

# creates snippet from song given
# overlays all other snippets to drum beat
def drums(song):
	global girlsPretty
	silentStart = AudioSegment.silent(duration=13200)
	smallSilent = AudioSegment.silent(90)
	drums = song[196090:198400]
	drums = drums.append(smallSilent)
	drums = drums.overlay(drums[500:1000], position = 1300)
	drums = drums * 45
	drums = drums.apply_gain(-5)
	drums = silentStart.append(drums)
	output = background.overlay(drums).overlay(marsOyeah, times=3).overlay(girlsPretty, position=35200, times=3)
	output.export('output.wav', 'wav')

# delete unused files
def delete():
	os.remove('background.wav')
	os.remove('mars.wav')
	os.remove('marsFast.wav')
	os.remove('oyeah.wav')
	os.remove('soPretty.wav')
	os.remove('soPrettySlow.wav')

# pseudomain
def main():
	global background
	global prettyGirls
	global oyeahs
	global marsOyeah
	global girlsPretty

	createBackground(song)
	prettyGirls(song)

	# we just so pretty
	soPretty = song[19990:21250]
	soPretty.export('soPretty.wav', 'wav')
	soPretty = wave.open('soPretty.wav', 'r')
	soPrettySlow = wave.open('soPrettySlow.wav', 'w')
	soPrettySlow.setparams(soPretty.getparams())
	writeFrames = soPretty.readframes(soPretty.getnframes())
	soPrettySlow.setframerate(soPretty.getframerate() / 2)
	soPrettySlow.writeframes(writeFrames)
	soPrettySlow.close()
	soPrettySlow = AudioSegment.from_wav('soPrettySlow.wav')

	#combine last two
	silent5 = AudioSegment.silent(duration=22000)
	smallSilent = AudioSegment.silent(90)
	girlsPretty = prettyGirls.append(smallSilent).append(soPrettySlow).append(silent5)

	ohYeah(song)
	mars(song)
	drums(song)
	delete()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "exiting.."
	

