table = open('pipeline.csv', 'r')
output = open('pipeline.tex', 'w')

lines = table.readlines()
table.close()

output.write('\\begin{table}\n')
output.write('  \\centering\n')

counter = 0
for line in lines:
	quoted = line.split("\"")
	splitted = quoted[2].split(',')[:-1]
	if counter == 0:
		print(''.join('c' * (len(splitted) + 1)))
		output.write('  \\begin{tabular}{' + 'l' * (len(splitted) + 1) + '} \n')
	# Removing quotes
	quoted[1] = "\\textbf{" + quoted[1] + "}"
	tex_line = "  {} & {} \\\\ \n".format(quoted[1], ' & '.join(splitted))
	output.write(tex_line)
	counter += 1

output.write('  \\end{tabular}\n')
output.write('\\end{table}\n')

output.close()
