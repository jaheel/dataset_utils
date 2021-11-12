from PIL import Image
import os.path
import glob

def convertjpg(jpgfile, outdir, width=416, height=416):
    """
    convert jpg size
    
    Params
    ------
    jpgfile : {scalar, string} source picture

    outdir : {scalar, string} save dir
    
    width : {scalar, int} image width

    height : {scalar, int} image height

    Returns
    -------
    
    """
    img = Image.open(jpgfile)
    
    img_width, img_height = img.size 
    scale = min(float(width) / float(img_width), float(height) / float(img_height)) # 转换的最小比例
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)

    img = img.resize((new_width, new_height), Image.BICUBIC)

    new_img = Image.new('RGB', (width, height), (128, 128, 128)) # 生成灰色图像
    new_img.paste(img, ((width - new_width) // 2, (height - new_height) // 2))
    new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))


for jpgfile in glob.glob(r'E:\\dataset\\mahjong\\all_jpg\\*.jpg'):
    convertjpg(jpgfile, r'E:\\dataset\\mahjong\\all_jpg\\')