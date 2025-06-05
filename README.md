# 夢記録アプリ

Flask と SQLite を使った簡単な夢の記録アプリです。

## セットアップ

1. （任意）仮想環境を作成します。

```bash
python3 -m venv venv
source venv/bin/activate
```

2. 依存パッケージをインストールします。

```bash
pip install -r requirements.txt
```

3. データベースを初期化します。

```bash
python -c "from app import db; db.create_all()"
```

## 実行方法

開発サーバーを起動します。

```bash
python app.py
```

ブラウザで [http://localhost:5000](http://localhost:5000) を開くとアプリが利用できます。
