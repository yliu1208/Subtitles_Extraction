

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
intermediate = open ("subtitles.txt", "r", encoding='UTF-8')
formattedSubtitles = open("formattedSubtitles.txt", "w+", encoding='UTF-8')
sentence = ''

newlines = intermediate.readlines()
for newline in newlines:
    if newline.startswith('-') or newline[0].isupper():
        if (len(sentence) != 0):
            formattedSubtitles.write(sentence)
        # write a new line
        formattedSubtitles.write('\n\n')
        sentence = ''
        sentence += newline.strip()
    elif newline[0].islower():
        sentence += ' '
        sentence += newline.strip()
    else:
        continue

intermediate.close()
formattedSubtitles.close()
