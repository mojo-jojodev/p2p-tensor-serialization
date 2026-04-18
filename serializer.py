import struct, io, torch
def pack_tensor(tensor):
    buffer = io.BytesIO()
    torch.save(tensor.contiguous(), buffer)
    payload = buffer.getvalue()
    return struct.pack("!Q", len(payload)) + payload
