

sourceFile = open ("srt.txt", "r", encoding='UTF-8')
subtitles = open("subtitles.txt", "w+", encoding='UTF-8')

lines = sourceFile.readlines()
count = 0

for line in lines:
    count += 1
    if line.strip().isdigit():
        subtitles.write('\n')
    elif line.startswith('-'):
        subtitles.write(line)
    elif line[0].isalpha():
        subtitles.write(line)
    else:
        continue

subtitles.close()