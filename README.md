# 坑位信息查询系统

## 文件说明
- `index.html` - 查询页面
- `data.json` - 数据文件

## 更新数据流程

### 方法一：让我帮你转换（最简单）
1. 把新的 Excel 表格发给我
2. 我帮你生成新的 `data.json` 文件
3. 你下载后上传到 GitHub 覆盖旧文件
4. 几秒钟后网站自动更新

### 方法二：自己转换
1. 打开在线转换工具：https://products.aspose.app/cells/zh/conversion/xlsx-to-json
2. 上传你的 Excel 文件
3. 下载生成的 JSON 文件
4. 重命名为 `data.json`
5. 上传到 GitHub 覆盖旧文件

## 更新时间
每次更新数据后，需要修改 `index.html` 第 232 行的时间：
```javascript
const UPDATE_TIME = '2026-04-07 16:30'; // 改成新的更新时间
```

## GitHub 更新步骤
1. 打开你的 GitHub 仓库
2. 找到 `data.json` 文件
3. 点击右上角的铅笔图标（编辑）
4. 删除旧内容，粘贴新内容
5. 点击 "Commit changes"
6. 等几十秒，网站自动更新

## 网站部署
- GitHub Pages 会自动部署
- 访问地址：`https://你的用户名.github.io/仓库名/`
