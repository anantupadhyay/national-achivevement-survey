# Gramener Assignment Files

## Directories:
	# Codes
	# NAS-Assignment

### Codes:
	The Codes directory consist of 3 files:
	1.py - It contains the code to find common element between two lists and difference between 		two lists.
	2.py - It contains the code to find the number of thursdays between 1990 and 2000. 
			There were 574 thursdays between the given time.

	3.js - Javascript function or expression that returns an array with just
			the zeroes removed.


	The NAS-assignment consists of 3 jupyter notebooks:
	NAS-1 - Find factors which influences students performance the most.
	NAS-2 - Analyses the performance of girls and boys in all the states.
	NAS-3 - Compares the performance of Students from south India with students from Rest of India.

## Dependencies :
	i)	Matplotlib
	ii) Numpy
	iii)Pandas
	iv) Scikit-learn


	In all the files, first of all preprocessing was done to replace null-values in the dataset.


	#In NAS-1, I have defined a numpy array 'performance' which contains the sum of marks obtained in Maths, Science, Social and Reading. Then through 'performance' array found out the mean score of individuals and categorized them as avg performer, best performer, and poor performer.
	Also added a column 'th' which is set true if an individual is above average, otherwise, is set to false. After that used ExtraTreeClassifier to extract import features from the available factors and plotted a bar chart of same. The results shows that 'Siblings' was the most influencing factor while 'Like School' was the least influencing factor.

	In NAS-2, After performing all the preprocessing part, calculated the average marks obtained by boys and girls in each state and plotted them. Also plotted a pie chart of percentage of states where girls were better performer. Similar, approach was followed to calculate the marks in other categories of subject as well. Results obtained reflected that in 54% states, girl's average score was more than boy's average score. Although the maximum difference was around 3 marks only.

	In NAS-3, First of all defined which states I will count as south Indian states. After that made a dataframe south which consist of additional column 'is_south'. The column values were set true for south Indian states and were set false for other states. After that, I've calculated the mean scores of students in Maths, and Science for both south as well as Rest of India students. Plotted the values, the results obtained reflected that the average performance of students from rest of India was better than students from south India.