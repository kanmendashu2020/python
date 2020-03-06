import requests
import re
import os
from urllib import error


def main():
    dirPath = "girl-images"
    base_url = "https://www.buxiuse.com/?page={}"
    page = 2
    j = 0
    # while page < 11:
    for page in range(2, 12):
        url = base_url.format(page)
        try:
            result = requests.get(url, timeout=10)
        except error.HTTPError as e:
            page += 1
            continue
        else:
            text = result.text
            list = re.findall('src="(.*?.jpg)"', text, re.S)
            if len(list) == 0:
                page += 1
                continue
            else:
                for enum in list:
                    image = requests.get(enum, timeout=7)
                    filePath = os.path.join(dirPath, "girl_image_" + str(j) + ".jpg")
                    print_str = '这是第 {} 个妹子,妹子我爱你'
                    print(print_str.format(j))
                    f = open(filePath, 'wb')
                    f.write(image.content)
                    f.close()
                    j += 1
                page += 1


if __name__ == '__main__':
    main()
