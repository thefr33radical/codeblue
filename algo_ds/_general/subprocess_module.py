# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:52:08 2017

@author: gowtham
"""

from subprocess import call
call(["java","-cp","*","-mx5g edu.stanford.nlp.sentiment.SentimentPipeline", "-input.txt",">","output.txt"])