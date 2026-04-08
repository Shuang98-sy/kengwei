#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excel 转 JSON 脚本
自动将 input 文件夹中的 Excel 文件转换为 data.json
"""

import pandas as pd
import json
import os
import glob
from datetime import datetime

def convert_excel_to_json():
    # 查找 input 文件夹中的 Excel 文件
    input_dir = 'input'
    excel_files = glob.glob(f'{input_dir}/*.xlsx') + glob.glob(f'{input_dir}/*.xls')
    
    if not excel_files:
        print("未找到 Excel 文件！")
        return False
    
    # 使用找到的第一个 Excel 文件
    excel_file = excel_files[0]
    print(f"正在处理文件: {excel_file}")
    
    try:
        # 读取 Excel
        df = pd.read_excel(excel_file)
        
        # 处理空值
        df = df.fillna('--')
        
        # 转换为字典列表
        records = df.to_dict(orient='records')
        
        # 获取当前时间
        now = datetime.now()
        update_time = now.strftime('%Y-%m-%d %H:%M')
        
        # 构建输出数据结构（包含更新时间和数据）
        output = {
            "update_time": update_time,
            "data": records
        }
        
        # 保存为 JSON
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"转换成功！共 {len(records)} 条记录")
        print(f"更新时间：{update_time}")
        return True
        
    except Exception as e:
        print(f"转换失败: {e}")
        return False

if __name__ == '__main__':
    convert_excel_to_json()
