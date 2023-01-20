"""IBM Project"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv


def english_to_french(english_text):
    "Function to translate from englisch to french"
    frenchtext_received = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    frenchtext = frenchtext_received['translations'][0]['translation']
    return frenchtext


def french_to_english(french_text):
    "Function to translate from french to englisch"
    englishtext_received = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    englishtext = englishtext_received['translations'][0]['translation']
    return englishtext

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'


#print (apikey)
#print (url)
#print (version)#

#Creating the language translator object
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=authenticator)
language_translator.set_service_url(url)


#print (englishToFrench("Hello"))
#print (frenchToEnglish("Bonjour"))
