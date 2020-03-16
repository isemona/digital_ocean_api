import requests

resp = requests.get('https://semonav2.oktapreview.com')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# for profile in resp.json():
#     print('{} {}'.format(profile['firstName'], profile['lastName']))
    print(resp.json)