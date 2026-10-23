#!/usr/bin/env python3
"""Đóng gói sản phẩm seminar, không phải đóng gói repo để phát triển."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import zipfile
import nbformat

ROOT = Path(__file__).resolve().parents[1]
NBS = [
    ROOT / 'notebooks' / '01_EDA.ipynb',
    ROOT / 'notebooks' / '02_Segmentation_HOG.ipynb',
    ROOT / 'notebooks' / '03_Preprocessing.ipynb',
]
SLIDE = ROOT / 'slides' / 'final' / 'Seminar.pptx'
LIMIT = 30 * 1000 * 1000


def main():
    parser = argparse.ArgumentParser(description='Tạo ZIP nộp seminar <=30 MB.')
    parser.add_argument('--output', default='submission/Seminar_submission_DRAFT.zip',
                        help='Đường dẫn ZIP đầu ra (tương đối repo hoặc tuyệt đối).')
    args = parser.parse_args()
    errors = []
    if not SLIDE.is_file():
        errors.append('Thiếu slides/final/Seminar.pptx')
    for nb_path in NBS:
        if not nb_path.is_file():
            errors.append(f'Thiếu {nb_path.relative_to(ROOT)}')
            continue
        try:
            nb = nbformat.read(nb_path, as_version=4)
            nbformat.validate(nb)
        except Exception as e:
            errors.append(f'Notebook không hợp lệ: {nb_path.name}: {e}')
            continue
        if any('TODO:' in c.source for c in nb.cells):
            errors.append(f'Notebook còn TODO: {nb_path.name}')
    if errors:
        print('CHƯA THỂ ĐÓNG GÓI:', file=sys.stderr)
        for e in errors:
            print(' - ' + e, file=sys.stderr)
        return 1

    files = {Path('Seminar.pptx'): SLIDE}
    for f in NBS:
        files[Path('Resources') / 'notebooks' / f.name] = f
    for dir_rel in ['images','outputs']:
        for f in sorted((ROOT / dir_rel).rglob('*')):
            if f.is_file() and f.name != '.gitkeep':
                files[Path('Resources') / dir_rel / f.relative_to(ROOT / dir_rel)] = f
    for name in ['README.md', 'docs/references.md']:
        f = ROOT / name
        if f.is_file():
            files[Path('Resources') / name] = f

    dest = Path(args.output)
    if not dest.is_absolute():
        dest = ROOT / dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for target, source in files.items():
            z.write(source, arcname=target.as_posix())
    size = dest.stat().st_size
    if size > LIMIT:
        dest.unlink()
        print(f'ZIP vượt giới hạn 30 MB ({size/1024/1024:.1f} MiB).', file=sys.stderr)
        return 2
    print(f'Đã tạo: {dest} ({size / (1024 * 1024):.2f} MiB, {len(files)} files)')
    print('Nhớ kiểm tra trực tiếp file ZIP, tên ZIP và hạn nộp trước khi gửi.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
