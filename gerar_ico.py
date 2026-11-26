from pathlib import Path

from PIL import Image

BASE_DIR = Path(__file__).parent

arquivos_png = sorted(
    BASE_DIR.glob("*.png"),
    key=lambda x: x.stat().st_mtime,
    reverse=True
)
if not arquivos_png:

    print()
    print("Nenhum PNG encontrado.")
    input("ENTER para sair...")
    raise SystemExit

arquivo_png = arquivos_png[0]

arquivo_ico = arquivo_png.with_suffix(
    ".ico"
)

img = Image.open(arquivo_png)

img.save(
    arquivo_ico,
    format="ICO",
    sizes=[
        (256, 256),
        (128, 128),
        (64, 64),
        (48, 48),
        (32, 32),
        (16, 16)
    ]
)

print()
print("=" * 50)
print("ÍCONE CRIADO COM SUCESSO")
print("=" * 50)
print(f"PNG: {arquivo_png.name}")
print(f"ICO: {arquivo_ico.name}")
print("=" * 50)

input("ENTER para sair...")