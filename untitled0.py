#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 23:18:00 2021

@author: gintriag
"""

import glassdoor_scraper as gs
import pandas as pd
path = "/Users/gintriag/Google Drive/PERSONAL/Github/Data-science-for-jobs/chromedriver"

df = gs.get_jobs('data scientist',15,False,path,15)