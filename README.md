# HEIC to JPG Converter

此程式為將 HEIC 圖片轉換為 JPG 格式的 Python 程式
這樣就不用買Windows Store內用來瀏覽HEIC程式的外掛套件了
現省1USD，薛爛

## 功能

- 讀取指定資料夾內的 HEIC 圖片
- 根據 JSON 配置檔轉換為 JPG 格式
- 設置轉換品質和解析度
- 處理檔案名稱衝突
- 顯示轉換進度條

## 安裝

1. 確保你已安裝 Python 3.x。
2. 建立虛擬環境（可選）：

   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
   ```

3. 安裝所需的庫：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 將 HEIC 圖片放入指定的資料夾中。
2. 創建一個 JSON 配置檔，並根據需要設置轉換參數。範例配置如下：

   ```json
   {
       "quality": 85,
       "resolution": {
           "width": 1920,
           "height": 1080
       },
       "output_folder": "output_images"
   }
   ```

3. 執行程式：

   ```bash
   python Converter.py
   ```

## 注意事項

- 確保已安裝 `Pillow` 和 `pillow-heif` 的正確版本。
- 如果遇到任何問題，請檢查錯誤訊息並根據需要進行調整。

