from aip import AipSpeech

APP_ID = '11749959'
API_KEY = '7q4DPOF2OBkfpqx0QXwp8tbo'
SECRET_KEY = 'MzQkRzsVE0Olyqjuyjgi8WFbNyxbpTuC'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
s=client.asr(get_file_content('2.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})

print(s)