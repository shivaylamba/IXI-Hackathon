import requests
import time
import os
import sys
"""
reference : https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-disk
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-hand-text


Sample Output:
{'status': 'Succeeded', 'recognitionResults': [{'page': 1, 'clockwiseOrientation': 0.62, 'width': 1875, 'height': 361, 'unit': 'pixel', 'lines': [{'boundingBox': [8, 3, 1814, 23, 1812, 140, 6, 121], 'text': 'The quick brown fox jumps over the lazy', 'words': [{'boundingBox': [34, 10, 187, 13, 179, 116, 27, 111], 'text': 'The'}, {'boundingBox': [207, 14, 433, 18, 425, 123, 199, 116], 'text': 'quick'}, {'boundingBox': [453, 18, 738, 22, 730, 129, 445, 123], 'text': 'brown', 'confidence': 'Low'}, {'boundingBox': [758, 22, 905, 23, 895, 132, 750, 130], 'text': 'fox', 'confidence': 'Low'}, {'boundingBox': [931, 24, 1170, 25, 1161, 135, 922, 132], 'text': 'jumps'}, {'boundingBox': [1190, 25, 1403, 25, 1393, 137, 1180, 136], 'text': 'over'}, {'boundingBox': [1423, 25, 1569, 25, 1558, 138, 1412, 138], 'text': 'the'}, {'boundingBox': [1589, 25, 1815, 23, 1804, 138, 1578, 138], 'text': 'lazy', 'confidence': 'Low'}]}, {'boundingBox': [8, 209, 1857, 232, 1855, 340, 7, 317], 'text': 'Pack my box with five dozen liquor jugs.', 'words': [{'boundingBox': [10, 233, 188, 227, 186, 315, 7, 318], 'text': 'Pack'}, {'boundingBox': [205, 227, 344, 223, 342, 314, 202, 315], 'text': 'my'}, {'boundingBox': [389, 222, 534, 220, 531, 312, 386, 313], 'text': 'box', 'confidence': 'Low'}, {'boundingBox': [556, 219, 784, 219, 782, 313, 554, 312], 'text': 'with'}, {'boundingBox': [818, 219, 990, 222, 988, 315, 816, 313], 'text': 'five', 'confidence': 'Low'}, {'boundingBox': [1013, 222, 1241, 228, 1239, 319, 1011, 315], 'text': 'dozen'}, {'boundingBox': [1308, 230, 1614, 244, 1613, 329, 1306, 321], 'text': 'liquor', 'confidence': 'Low'}, {'boundingBox': [1652, 246, 1858, 259, 1857, 339, 1652, 331], 'text': 'jugs.', 'confidence': 'Low'}]}]}]}

"""

def image_analyser(file_path):
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    # else:
    #     print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    #     sys.exit()

    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

    text_recognition_url = endpoint + "/v2.1/read/core/asyncBatchAnalyze"
    # Set image_url to the URL of an image that you want to analyze.
    # image_path = file_path
    image_url = file_path
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    image_data = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"test.jpg"), "rb").read()
    data = {'url': image_url}
    response = requests.post(
        text_recognition_url, headers=headers, data=image_data)
    response.raise_for_status()
    operation_url = response.headers["Operation-Location"]
    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        print(analysis)
        time.sleep(1)
        if ("recognitionResults" in analysis):
            poll = False
        if ("status" in analysis and analysis['status'] == 'Failed'):
            poll = False

    if poll:
        return analysis

    return {}


if __name__=="__main__":
    image_analyser(input())