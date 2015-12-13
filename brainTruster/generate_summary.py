# -*- coding: utf-8 -*-


topic_path = 'topic'

items = []
chapters = []
content = open("../SUMMARY.md", 'wb')
summary = open('list.md', 'r')
for line in summary.readlines():
	if line == '\n':
		#content.write(line)
		continue
	if ">" in line:
		chapter = line.split('>')[0].split('<')[1]
		if chapter in chapters:
			chapter = "\t"
		else:
			chapters.append(chapter)
			chapter = "\n- [%s]()\n\t" % chapter
		new_line = "%s- %s" % (chapter, line)
		items.append(new_line)
		continue
	if "》" in line:
		chapter = line.split('》')[0].split('《')[1]
		if chapter in chapters:
			chapter = "\t"
		else:
			chapters.append(chapter)
			chapter = "\n- [%s]()\n\t" % chapter
		new_line = "%s- %s" % (chapter, line)
		items.append(new_line)
		continue
	new_line = "- %s" % line
	items.insert(0, new_line)
	
for item in items:
	content.write(item)

content.close()
summary.close()