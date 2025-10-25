import http.client
import requests

import json
import pandas as pd
import numpy as np

from transformers import pipeline

import os
import sys

from newsapi import NewsApiClient

#Build cuda_12.4.r12.4/compiler.33961263_0
import torch
print(torch.cuda.is_available())

import pyspark
from pyspark.sql import SparkSession


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps