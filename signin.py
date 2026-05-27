import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import sys

USERS = [
    {
        "email": "3838451843@qq.com",
        "password": "@Tmx12531574121"
    },
    {
        "email": "vsi.gs.i.e.h.v.d.i.d.o.d@gmail.com",
        "password": "@Tmx12531574121"
    }
]

async def signin_user(user, user_index):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} ({user['email']}) 开始登录...")
            
            await page.goto("https://api.iamhc.cn/login")
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(1)
            
            # 输入用户名/邮箱
            await page.fill('input[placeholder="请输入您的用户名或邮箱地址"]', user['email'])
            await asyncio.sleep(0.5)
            
            # 输入密码
            await page.fill('input[placeholder="请输入您的密码"]', user['password'])
            await asyncio.sleep(0.5)
            
            # 使用键盘操作来勾选复选框
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 勾选协议...")
            
            await page.click('input[placeholder="请输入您的密码"]')
            await asyncio.sleep(0.3)
            
            for i in range(2):
                await page.keyboard.press('Tab')
                await asyncio.sleep(0.3)
            
            await page.keyboard.press('Space')
            await asyncio.sleep(0.5)
            
            # 点击继续按钮
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 点击登录...")
            await page.click('button:has-text("继续")')
            
            # 等待页面跳转
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 等待跳转...")
            await asyncio.sleep(10)
            
            # 查找并点击个人设置
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 查找个人设置...")
            found = False
            try:
                await page.click('text=个人设置', timeout=3000)
                found = True
            except:
                try:
                    await page.click('a:has-text("个人设置")', timeout=3000)
                    found = True
                except:
                    try:
                        await page.click('button:has-text("个人设置")', timeout=3000)
                        found = True
                    except:
                        pass
            
            if not found:
                try:
                    await page.click('text=控制台', timeout=3000)
                    await asyncio.sleep(2)
                    try:
                        await page.click('text=个人设置', timeout=3000)
                        found = True
                    except:
                        pass
                except:
                    pass
            
            await asyncio.sleep(2)
            
            # 查找并点击立即签到
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 查找签到按钮...")
            signed_in = False
            try:
                await page.click('text=立即签到', timeout=5000)
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 签到成功！ ✅")
                signed_in = True
            except:
                try:
                    await page.click('button:has-text("立即签到")', timeout=5000)
                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 签到成功！ ✅")
                    signed_in = True
                except:
                    try:
                        await page.click('a:has-text("立即签到")', timeout=5000)
                        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 签到成功！ ✅")
                        signed_in = True
                    except:
                        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 未找到签到按钮或今日已签到")
            
            if signed_in:
                await asyncio.sleep(3)
            
            return signed_in
            
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户 {user_index+1} 发生错误: {e}")
            return False
            
        finally:
            await asyncio.sleep(2)
            await browser.close()

async def main():
    print("=" * 60)
    print("自动签到系统启动")
    print("=" * 60)
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"用户数量: {len(USERS)}")
    print("=" * 60)
    
    results = []
    for i, user in enumerate(USERS):
        print(f"\n正在处理用户 {i+1}/{len(USERS)}: {user['email']}")
        result = await signin_user(user, i)
        results.append(result)
        
        if i < len(USERS) - 1:
            print(f"等待 5 秒后处理下一个用户...")
            await asyncio.sleep(5)
    
    print("\n" + "=" * 60)
    print("签到完成汇总")
    print("=" * 60)
    for i, result in enumerate(results):
        status = "成功" if result else "失败/已签到"
        print(f"用户 {i+1} ({USERS[i]['email']}): {status}")
    
    success_count = sum(results)
    print(f"\n总计: {success_count}/{len(USERS)} 用户签到成功")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
