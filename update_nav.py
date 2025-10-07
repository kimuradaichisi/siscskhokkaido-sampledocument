import os
import yaml
from pathlib import Path
import shutil

# --- 設定 ---
DOCS_DIR = 'docs'
MKDOCS_CONFIG = 'mkdocs.yml'
# ----------------

def get_title_from_name(name: str) -> str:
    """ファイル名/ディレクトリ名からナビゲーション用のタイトルを生成します。"""
    if name.endswith('.md'):
        name = name[:-3]
    return name.replace('_', ' ').replace('-', ' ')

def generate_nav_recursive(current_path: Path) -> list:
    """指定されたパスから再帰的にナビゲーション構造のリストを生成します。"""
    nav_list = []
    # ファイルシステムから項目を読み込み、名前でソートして順序を安定させる
    items = sorted(os.listdir(current_path))

    # 'index.md' または 'README.md' をリストの先頭に移動させる
    index_files = ['index.md', 'README.md']
    for index_file in index_files:
        if index_file in items:
            items.remove(index_file)
            items.insert(0, index_file)
            break

    for item in items:
        item_path = current_path / item
        # 'docs'ディレクトリからの相対パスに変換
        relative_path = item_path.relative_to(DOCS_DIR).as_posix()

        if item_path.is_dir():
            # ディレクトリの場合、再帰的にサブナビゲーションを生成
            sub_nav = generate_nav_recursive(item_path)
            if sub_nav:  # 空のディレクトリはナビゲーションに追加しない
                title = get_title_from_name(item)
                nav_list.append({title: sub_nav})
        elif item.endswith('.md'):
            # Markdownファイルの場合
            title = get_title_from_name(item)
            # docs/index.md はトップレベルの特別な項目としてmain関数で処理するため、ここではスキップ
            if relative_path.lower() == 'index.md':
                continue
            nav_list.append({title: relative_path})

    return nav_list

def main():
    """メイン処理"""
    docs_path = Path(DOCS_DIR)
    config_path = Path(MKDOCS_CONFIG)

    if not docs_path.is_dir():
        print(f"エラー: '{DOCS_DIR}' ディレクトリが見つかりません。")
        return
    if not config_path.is_file():
        print(f"エラー: '{MKDOCS_CONFIG}' ファイルが見つかりません。")
        return

    print("ドキュメントの階層構造を解析中...")
    
    # docsディレクトリ直下からナビゲーションを生成
    new_nav = generate_nav_recursive(docs_path)

    # トップレベルの 'index.md' があれば、ナビゲーションの先頭に追加
    top_index_path = docs_path / 'index.md'
    if top_index_path.exists():
        new_nav.insert(0, {'はじめに': 'index.md'})

    print(f"'{MKDOCS_CONFIG}' を更新します。")

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        # awesome-pagesプラグインが有効な場合は警告
        plugins = config_data.get('plugins', [])
        if plugins and any('awesome-pages' in (p if isinstance(p, str) else list(p.keys())[0]) for p in plugins):
            print("\n警告: 'awesome-pages' プラグインが有効です。")
            print("このスクリプトによる'nav'セクションの自動更新は不要かもしれません。")
            choice = input("それでも続行しますか？ (y/N): ")
            if choice.lower() != 'y':
                print("処理を中断しました。")
                return

        # navセクションを新しい構造で上書き
        config_data['nav'] = new_nav

        # 元のファイルをバックアップ
        backup_path = config_path.with_suffix('.yml.bak')
        print(f"既存の設定を '{backup_path.name}' にバックアップします。")
        shutil.copy(config_path, backup_path)

        with open(config_path, 'w', encoding='utf-8') as f:
            # YAMLを書き出す
            # allow_unicode=True: 日本語がエスケープされるのを防ぐ
            # sort_keys=False: キーの順序を保持する
            # indent=2: 見やすいインデントを設定
            yaml.dump(config_data, f, allow_unicode=True, sort_keys=False, indent=2)

        print(f"\n'{MKDOCS_CONFIG}' の 'nav' セクションが正常に更新されました。")
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == '__main__':
    main()