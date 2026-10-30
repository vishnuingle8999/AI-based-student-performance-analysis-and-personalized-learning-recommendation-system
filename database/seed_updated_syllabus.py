# -*- coding: utf-8 -*-
"""
DBATU NEP 2020 AI&DS Curriculum and Question Bank Generator.
Generates comprehensive syllabus and 60 questions per subject across all units.
"""

import os
import csv

# We will generate comprehensive data for:
# Semester V (Third Year):
#   1. Machine Learning (26AF1245PC501) - 60 Questions
#   2. Object Oriented Programming in Java (26AFAIPC502) - 60 Questions
#   3. Cloud and Distributed AI Systems (26AFAIPC503) - 60 Questions
#   4. Data Engineering and Big Data Systems (26AFAIPC504) - 60 Questions
#   5. Vector Databases (26AFAIPE507) - 60 Questions
#
# Semester IV (Second Year):
#   1. Introduction to Operating Systems (25AFAIPC401) - 60 Questions
#   2. Data Analytics (25AFAIPC402) - 60 Questions
#   3. Probability and Statistics (25AF1245PC403) - 60 Questions
#   4. Full Stack Development (25AFAIPCL404) - 60 Questions
#
# Semester III (Second Year):
#   1. Engineering Mathematics-III (25AF1000BS301) - 60 Questions
#   2. Discrete Mathematics (25AF1245PC303) - 60 Questions
#   3. Data Structures (25AF1245PC302) - 60 Questions
#   4. Artificial Intelligence (25AFAIPC304) - 60 Questions
#   5. Prompt Engineering (25AFAIPC307) - 60 Questions
#
# Semester VI (Third Year):
#   1. Deep Learning (26AFAIPC601) - 60 Questions
#   2. Natural Language Processing (26AFAIPC602) - 60 Questions
#   3. Fundamental Edge AI (26AFAIPC603) - 60 Questions
