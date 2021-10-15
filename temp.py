import time

# 타임 포맷
# [2021-10-15 10:34:20]
lt = time.localtime()
print(lt)
formatedTime = time.strftime('[%Y-%m-%d %H:%M:%S]')
print(f'formatedTime : {formatedTime}')