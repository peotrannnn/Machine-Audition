"""
Script tải dataset GAPS từ Hugging Face về thư mục data/raw/GAPS
Hỗ trợ:
- Tự động tạo thư mục nếu chưa có.
- Resume tải tiếp khi mạng gián đoạn.
- Đa luồng (max_workers) để tăng tốc độ tải.
"""

import os
import sys
from pathlib import Path

# Đảm bảo mã hóa UTF-8 cho console Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import argparse
from huggingface_hub import snapshot_download

def parse_args():
    # Thư mục gốc của project (D:\Machine Audition)
    project_root = Path(__file__).resolve().parent.parent
    default_output_dir = project_root / "data" / "raw" / "GAPS"

    parser = argparse.ArgumentParser(description="Download GAPS dataset from Hugging Face.")
    parser.add_argument(
        "--repo_id",
        type=str,
        default="xavriley/GAPS",
        help="Hugging Face repo ID (default: xavriley/GAPS)"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=str(default_output_dir),
        help=f"Thu muc luu dataset (default: {default_output_dir})"
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="Hugging Face access token (neu can)"
    )
    parser.add_argument(
        "--max_workers",
        type=int,
        default=4,
        help="So luong tai dong thoi (default: 4)"
    )
    return parser.parse_args()

def download_dataset():
    args = parse_args()
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print(f"Bắt đầu tải dataset: {args.repo_id}")
    print(f"Lưu vào thư mục:     {output_path.resolve()}")
    print(f"Số luồng tải:        {args.max_workers}")
    print("=" * 60)

    try:
        downloaded_dir = snapshot_download(
            repo_id=args.repo_id,
            repo_type="dataset",
            local_dir=str(output_path),
            token=args.token,
            max_workers=args.max_workers,
        )
        print("\n" + "=" * 60)
        print("TẢI HOÀN TẤT!")
        print(f"Dữ liệu đã được lưu tại: {downloaded_dir}")
        print("=" * 60)

        # Liệt kê tóm tắt các tệp/thư mục đã tải
        files = list(output_path.glob("*"))
        print(f"\nTổng số tệp/thư mục trong {output_path.name}: {len(files)}")
        for f in files[:10]:
            print(f" - {f.name}")
        if len(files) > 10:
            print(f" ... và {len(files) - 10} tệp khác.")

    except Exception as e:
        print(f"\n[LỖI] Quá trình tải gặp sự cố: {e}", file=sys.stderr)
        print("Gợi ý: Kiểm tra lại kết nối mạng hoặc thử chạy lại script để tiếp tục tải (resume).", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    download_dataset()
