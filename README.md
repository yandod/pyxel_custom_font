# pyxel_custom_font

Pyxel Code Maker の公式サンプルにある「日本語フォント表示」の挙動を再現するプロジェクトです。

## 参考

- Pyxel Code Maker
	- https://kitao.github.io/pyxel/web/code-maker/
- 元になった公式サンプル
	- https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/13_custom_font.py

## 実行

Pyxel Code Makerの Load > Github を選択し、以下のURLを指定します。

```
https://github.com/yandod/pyxel_custom_font/blob/dist/pyxel_custom_font.zip
```

`Load from GitHub` ダイアログは `https://github.com/USER/REPO/blob/BRANCH/PATH/TO/PROJECT.zip` という、リポジトリにコミットされたzipファイルへの通常のURL(blob URL)を要求します。GitHubが自動生成する `archive/refs/heads/main.zip` 形式のURLは受け付けません。

このリポジトリでは `main` ブランチへのpushをトリガーに GitHub Actions (`.github/workflows/publish-zip.yml`) が実行用ファイル一式を zip にまとめ、`dist` ブランチに `pyxel_custom_font.zip` として自動でコミットします(ソース一式のある `main` にzipを直接コミットして二重管理になるのを避けるため)。

## ライセンス

ライセンスなどは、元の公式サンプルコードに準じます。
