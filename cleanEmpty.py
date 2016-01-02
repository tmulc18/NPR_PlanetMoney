import os
for file in os.listdir("./"):
	type = file.split(".")[-1]
	if type == "mp3":
		if os.stat(file).st_size < 280:
			os.remove(file)

	