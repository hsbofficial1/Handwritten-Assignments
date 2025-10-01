#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author: Harsharaj Shetty B
# Version: 1.0.0

import pywhatkit as pw

text_to_convert = """
I’m Harsharaj Shetty B, someone who finds joy in building things that combine creativity and logic. From coding websites to designing visuals to experimenting with tech projects, I see each challenge as a chance to learn and create something meaningful. I started out exploring design and development just out of curiosity, but over time it turned into a passion that shaped my work and businesses. Today, I run ventures like SparkBee Technologies, Cucoon, and Aquatic.In, while also diving deep into side projects ranging from IoT systems to AI-based solutions. \n I’m also the creator of Curiosity Weekends, a makerspace in Kasaragod that grew from small weekend meetups into a 700 sq ft lab. It’s a non-commercial community where students, educators, and lifelong learners explore AI, robotics, IoT, mathematics, and more—driven by curiosity, collaboration, and hands-on experimentation for Absolutely Free.
"""

pw.text_to_handwriting(text_to_convert, 'demo.png',[0,0,135])
print("Converted !!")
6