"""Build the Cyber Risk Ranger Games WordPress plugin from the two standalone game files.

Run from anywhere:  python3 wordpress-plugin/build_plugin.py
Writes:             wordpress-plugin/dist/cyber-risk-ranger-games.zip
"""
import base64
import hashlib
import pathlib
import re
import shutil
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
DIST = HERE / 'dist'
SLUG = 'cyber-risk-ranger-games'
ASSET_TOKEN = '__CRR_ASSETS__'
GAMES = {
    'spot-the-phish.html': ROOT / 'spot-the-phish.html',
    'defender-style.html': ROOT / 'cyber-risk-ranger-quiz.html',
}
SILENCE = '<?php\n// Silence is golden.\n'


def externalize_images(html, assets):
    # The standalone page embeds each JPEG as a data URI, some of them more than once. As plugin
    # files they download once and keep the upload under the 2 MB limit common on WordPress hosts.
    def swap(match):
        data = base64.b64decode(match.group(1))
        name = 'ranger-' + hashlib.sha1(data).hexdigest()[:10] + '.jpg'
        assets[name] = data
        return f'{ASSET_TOKEN}/{name}'

    return re.sub(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)', swap, html)


def main():
    shutil.rmtree(DIST, ignore_errors=True)
    plugin = DIST / SLUG
    (plugin / 'games').mkdir(parents=True)
    (plugin / 'assets').mkdir()

    assets = {}
    for name, source in GAMES.items():
        html = externalize_images(source.read_text(encoding='utf-8'), assets)
        (plugin / 'games' / name).write_text(html, encoding='utf-8')
    for name, data in assets.items():
        (plugin / 'assets' / name).write_bytes(data)
    for folder in ('games', 'assets'):
        (plugin / folder / 'index.php').write_text(SILENCE, encoding='utf-8')
    for name in (f'{SLUG}.php', 'readme.txt'):
        shutil.copy(HERE / name, plugin / name)

    archive = DIST / f'{SLUG}.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in sorted(plugin.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(DIST).as_posix())

    print(f'{len(assets)} images moved out of the pages')
    for path in sorted(plugin.rglob('*')):
        if path.is_file():
            print(f'  {path.relative_to(DIST).as_posix():<60} {path.stat().st_size:>10,} bytes')
    print(f'{archive.relative_to(ROOT)}: {archive.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
