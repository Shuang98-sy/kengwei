name: Convert Excel to JSON

on:
  push:
    paths:
      - 'input/*.xlsx'

permissions:
  contents: write

jobs:
  convert:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install pandas openpyxl
    
    - name: Convert Excel to JSON
      run: |
        python convert.py
    
    - name: Get current time
      id: time
      run: echo "timestamp=$(date +'%Y-%m-%d %H:%M')" >> $GITHUB_OUTPUT
    
    - name: Update time in index.html
      run: |
        sed -i "s|数据更新时间：<span>[^<]*</span>|数据更新时间：<span>${{ steps.time.outputs.timestamp }}</span>|g" index.html
    
    - name: Commit changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        git commit -m "Update data.json and timestamp"
        git push --force
