import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyA7ajqUxYZMZtxbiDrDu8YMkDa_e_NB8uc")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)