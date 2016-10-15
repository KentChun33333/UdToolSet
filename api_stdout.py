
import requests
import json
import logging
import time
import datetime

# =============================================================================
# API Document
# https://review.udacity.com/api-doc/index.html#!/me/get_me_certifications

# =============================================================================
# replace token here
TOKEN = ('''_______________________________________________''')

CERTIFICATIONS_URL = ('https://review-api.udacity.com/api/v1/me'
                      '/certifications.json')

# =============================================================================
#'https://review.udacity.com/#!/submissions/dashboard'
headers = {'Authorization': TOKEN, 'Content-Length': '0'}

# =============================================================================
# Set up a logger thead name, could be used in multi-threading condition

logger = logging.getLogger('Udacity')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(ch)

while True:
    res = requests.get(CERTIFICATIONS_URL, headers=headers)
    jsonDL = json.loads(res.content)
    for jsonD in jsonDL:
        # def messages
        mess = '{} waiting [{}], lang_recruit : [{}]'.format(jsonD['project']['name'], jsonD['project']['awaiting_review_count_by_language'], jsonD['project']['languages_to_recruit'])
        if jsonD['project']['awaiting_review_count'] > 0:
            logger.warning(mess)
    print ('')
    time.sleep(30)


