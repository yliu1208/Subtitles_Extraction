import sys
import os
from fpdf import FPDF

pdf = FPDF()
movie = sys.argv[1]

source = open ((str(movie) + '.srt'), 'r', encoding='UTF-8')
subtitles = open((str(movie) + '.txt'), 'w+', encoding='UTF-8')

lines = source.readlines()
for line in lines:
    if line.strip().isdigit():
        subtitles.write('\n')
    elif line.startswith('-'):
        subtitles.write(line)
    elif line[0].isalpha():
        subtitles.write(line)
    else:
        continue

subtitles.close()
intermediate = open ((str(movie) + '.txt'), 'r', encoding='UTF-8')
formattedSubtitles = open('formatted ' + str(movie) + '.txt', 'w+', encoding='UTF-8')
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

pdf.add_page()
pdf.add_font('BookAntiqua', '', 'BookAntiquaFont.ttf', uni=True)
pdf.set_font('BookAntiqua', '', 12)
pdf.set_margins(10, 10, 10)

f = open('formatted ' + str(movie) + '.txt', 'r', encoding='UTF-8')
for x in f:
    pdf.multi_cell(200, 6, txt = x, align = 'L')

pdf.output(str(movie) + '.pdf')
os.remove(str(movie) + '.txt')