from core.print import print_warning, print_error
from driver.base import WX_API
from core.config import cfg
from jobs.notice import sys_notice
from driver.success import Success
from tools.base64_tools import image_to_base64
import time
import os
import base64

def compress_qrcode_to_webp(png_path: str, quality: int = 80) -> str:
    """
    将 PNG 二维码压缩转换为 WebP 格式的 Base64 字符串
    
    Args:
        png_path: PNG 图片路径
        quality: WebP 压缩质量 (1-100)，默认 80
        
    Returns:
        Base64 编码的 WebP 图片 data URL
    """
    try:
        from PIL import Image
        from io import BytesIO
        
        if not os.path.exists(png_path):
            print_error(f"二维码文件不存在: {png_path}")
            return ""
        
        # 打开 PNG 图片
        with Image.open(png_path) as img:
            # 转换为 RGB（WebP 不支持 RGBA 的某些模式）
            if img.mode in ('RGBA', 'LA', 'P'):
                # 创建白色背景
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 压缩为 WebP
            buffer = BytesIO()
            img.save(buffer, format='WEBP', quality=quality, method=6)
            webp_data = buffer.getvalue()
            
            # 转为 Base64
            base64_data = base64.b64encode(webp_data).decode('utf-8')
            
            print(f"二维码压缩: PNG {os.path.getsize(png_path)} bytes -> WebP {len(webp_data)} bytes (Base64: {len(base64_data)} bytes)")
            
            return f"data:image/webp;base64,{base64_data}"
            
    except ImportError:
        print_error("PIL 库未安装，无法压缩二维码")
        # 回退到原始方法
        return image_to_base64(png_path)
    except Exception as e:
        print_error(f"压缩二维码失败: {e}")
        # 回退到原始方法
        return image_to_base64(png_path)

def send_wx_code(title:str="",url:str=""):
    if cfg.get("server.send_code",False):
        WX_API.GetCode(Notice=CallBackNotice,CallBack=Success)
    pass

def CallBackNotice(data=None,ext_data=None):
        if data is not None:
            print_warning(data)
            return 
        img_path=WX_API.QRcode()['code']
        rss_domain=str(cfg.get("rss.base_url",""))
        url=rss_domain+str(img_path)
        # 使用 WebP 压缩，避免钉钉 20KB 消息体限制
        url=compress_qrcode_to_webp("./static/wx_qrcode.png")
        text=f"**[订阅消息]**\n\n"  # 添加钉钉关键词
        text+=f"- 服务名：{cfg.get('server.name','')}\n"
        text+=f"- 发送时间： {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}"
        if WX_API.GetHasCode():
            text+=f"![描述]({url})"
            # text+=f"<img src='{url}' width='100' height='100'/>"
            text+=f"\n- 请使用微信扫描二维码进行授权"
        sys_notice(text, str(cfg.get("server.code_title","[订阅消息] WeRss授权过期,扫码授权")))