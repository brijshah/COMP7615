import wave, argparse, warnings
from pydub import AudioSegment

def main():
	# silent sounds
	silentStart = AudioSegment.silent(duration=13200)
	silent5 = AudioSegment.silent(duration=22000)
	smallSilent = AudioSegment.silent(90)
	# open song
	song = AudioSegment.from_wav('bspears.wav')
	# create backround beat
	background = song[2600:5000]
	background = background.append(background)
	background = background * 50
	background_reverse = background.reverse()
	background_reverse = background_reverse
	background_reverse = background_reverse.apply_gain(-25.0)
	background = background.overlay(background_reverse)
	background = background.fade_in(8800).fade_out(8800)
	background.export('background.wav', 'wav')
	# pretty girls
	prettyGirls = song[12050:14800]
	prettyGirls = prettyGirls.fade_in(1500)
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
	girlsPretty = prettyGirls.append(smallSilent).append(soPrettySlow).append(silent5)
	# oh yeah
	oyeah = song[121800:122400]
	quietest = oyeah.apply_gain(-20)
	quieter = oyeah.apply_gain(-12.5)
	quiet = oyeah.apply_gain(-5)
	oyeahs = oyeah.append(quiet).append(quieter).append(quietest)
	oyeahs.export('oyeah.wav', 'wav')
	# mars
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
	# drums
	drums = song[196090:198400]
	drums = drums.append(smallSilent)
	drums = drums.overlay(drums[500:1000], position = 1300)
	drums = drums * 45
	drums = drums.apply_gain(-5)
	drums = silentStart.append(drums)
	output = background.overlay(drums).overlay(marsOyeah, times=3).overlay(girlsPretty, position=35200, times=3)
	output.export('output.wav', 'wav')

if __name__ == '__main__':
	main()

