from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('KSTdsMPsUS62SL58EqzaZbAFtEW2JlggKYHUI-NKLuvx')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/10758658-1ffd-49e5-ae59-ffb2aaa3b131')

with open('Medicine.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Its time for your medicine',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
