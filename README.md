# 自动签到系统

基于 GitHub Actions 的自动化签到系统，支持多用户同时签到。

## 功能特点

- ✅ 支持多用户同时签到
- ✅ 每天自动执行（北京时间 07:00，对应 UTC 23:00）
- ✅ 无需本地运行，通过 GitHub Actions 云端执行
- ✅ 支持手动触发
- ✅ 安全的 Secrets 配置，账号信息不上传代码

## GitHub Secrets 配置

在 GitHub 仓库中配置 Secrets 配置步骤：

1. 进入你的 GitHub 仓库
2. 点击 `Settings`（设置）
3. 在左侧菜单选择 `Secrets and variables` -> `Actions`
4. 点击 `New repository secret`
5. Name（名称）填写：`USERS`
6. Value（值）按照以下格式填写：

```
3838451843@qq.com,@Tmx12531574121,vsi.gs.i.e.h.v.d.i.d.o.d@gmail.com,@Tmx12531574121,bd.idh.idvskd.i.or@gmail.com,@Tmx12531574121,ar.ro.ga.n.cepchzxp@gmail.com,@Tmx12531574121
```

格式说明：邮箱1,密码1,邮箱2,密码2,邮箱3,密码3...

7. 点击 `Add secret` 保存

## 工作原理

工作流会在以下时间运行：
- 每天 UTC 23:00（即北京时间第二天 07:00）
- 你也可以手动触发（在 Actions 标签页点击 "Run workflow"）

## 本地测试

如果你想在本地测试，可以设置环境变量后运行：

Windows PowerShell:
```powershell
$env:USERS = "3838451843@qq.com,@Tmx12531574121,vsi.gs.i.e.h.v.d.i.d.o.d@gmail.com,@Tmx12531574121,bd.idh.idvskd.i.or@gmail.com,@Tmx12531574121,ar.ro.ga.n.cepchzxp@gmail.com,@Tmx12531574121"
python signin.py
```

Linux/macOS:
```bash
export USERS="3838451843@qq.com,@Tmx12531574121,vsi.gs.i.e.h.v.d.i.d.o.d@gmail.com,@Tmx12531574121,bd.idh.idvskd.i.or@gmail.com,@Tmx12531574121,ar.ro.ga.n.cepchzxp@gmail.com,@Tmx12531574121"
python signin.py
```
```
```text
或者使用 test.bat（Windows）
