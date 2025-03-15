import gzip
import zlib
import io

data = "1f8b0800000000000000b34cb4b03431b1484d36493136313632020029885dca10000000"
data = "1f8b080000000000000033343033333131b630b7483236314b320500968bbbfb100000000c0c0c0c0c0c0c0c0c0c0c0ce18265be6e4afc9ebe56e32f7026dc93"
with gzip.GzipFile(fileobj=io.BytesIO(bytes.fromhex(data))) as f:
    # 解压缩数据
    decompressed_data = f.read()
print(decompressed_data.decode())