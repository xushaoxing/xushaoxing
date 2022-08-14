from PIL import Image, ImageGrab
import time,os
class Screenshot():
    def fail_screenshot(self,result):
        im1 = ImageGrab.grab()  # 截屏操作 默认全屏
        # im1 = ImageGrab.grab(300,100,1400,600)
        TimeName = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 通过时间命名
        path=os.getcwd()
        path = r'C:\Users\Administrator\PycharmProjects\untitled1\Reports\Screenshot' + '\\'+ str(TimeName) + result + '.jpg'
        # print(path)
        im1.save(path)
        # im1.show()  # 展示
        # im2 = ImageGrab.grabclipboard()  # 获取粘贴板的图片  但是如果没有图像就会报错
        # # 判断粘贴板是否为空
        # if isinstance(im2, Image.Image):
        #     im2.save('.\\a.jpg')
        # else:
        #     print("粘贴板没有图片")
if __name__=='__main__':
    a=Screenshot()
    a.fail_screenshot('cu')