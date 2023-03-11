import pvleopard
leopard = pvleopard.create(access_key= "kdCYPIJyrL61fwhTHvWtkIL14Gzs58/X2CvwpdGQf3zjkASJNjEKxA==")
transcript, words = leopard.process_file("11.03.2023.mp3")

subtitle_path = "11.03.2023.mp3"



with open(subtitle_path, 'w') as f:
    f.write(property.to_srt(words))


