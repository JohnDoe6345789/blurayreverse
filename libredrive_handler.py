import os
import time
from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import sdl2
import sdl2.ext
import av
import fcntl
import struct
from ctypes import cdll, c_char_p, c_int, c_void_p, c_uint32
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class EncryptionInterface(ABC):
    @abstractmethod
    def decrypt_disc(self, disc_path: str) -> bool:
        pass

    @abstractmethod
    def get_title_keys(self) -> List[bytes]:
        pass

class PurePythonLibreDriveHandler(EncryptionInterface):
    def __init__(self, sdf_path: str = 'sdf_00000097.bin', device: str = '/dev/sr0', dll_path: str = 'libdriveio.dll'):
        self.sdf_path = sdf_path
        self.device = device
        self.dll_path = dll_path
        self.fd = None
        self.backend = default_backend()
        self.volume_key = b'\x00' * 16  # Placeholder VUK; load from keydb.cfg
        self.title_keys = []
        self.blobs = self._parse_sdf()
        self.libdriveio = self._load_dll()

    def _load_dll(self):
        try:
            lib = cdll.LoadLibrary(self.dll_path)
            lib.DriveIO_Init.argtypes = [c_char_p]
            lib.DriveIO_Init.restype = c_int
            lib.DriveIO_UploadFirmware.argtypes = [c_char_p, c_void_p, c_uint32]
            lib.DriveIO_UploadFirmware.restype = c_int
            return lib
        except OSError as e:
            print(f'Failed to load libdriveio.dll: {e}')
            return None

    def _parse_sdf(self) -> Dict[int, bytes]:
        with open(self.sdf_path, 'rb') as f:
            data = f.read()
        magic = data[0:4]
        if magic != b'SDF0':
            raise ValueError("Invalid SDF magic")
        entry_count = struct.unpack('>I', data[4:8])[0]  # 151
        dir_length = entry_count * 6  # 906
        data_start = 20 + dir_length  # 926

        blobs = {}
        dir_data = data[20:20 + dir_length]
        for i in range(entry_count):
            offset = i * 6
            a = dir_data[offset:offset + 3]
            b = dir_data[offset + 3:offset + 6]
            a_le = int.from_bytes(a, 'little')
            b_le = int.from_bytes(b, 'little')
            blob_off = data_start + a_le
            blob_size = b_le
            if blob_off + blob_size > len(data):
                print(f'Invalid blob for entry {i}')
                continue
            blob = data[blob_off:blob_off + blob_size]
            blobs[i] = blob  # Key as index; replace with firmware hash
        return blobs

    def _open_device(self):
        if self.fd is None:
            self.fd = os.open(self.device, os.O_RDWR | os.O_NONBLOCK)

    def _send_scsi_command(self, cdb: bytes, data: Optional[bytes] = None, direction: int = 1) -> bool:
        self._open_device()
        SG_IO = 0x2285
        sense_buffer = bytearray(32)
        dxfer_direction = direction

        io_hdr = struct.pack(
            '=IiLLLLLLB3BIIQQ',
            0x2285, dxfer_direction, 0, len(cdb), len(sense_buffer), 0,
            len(data) if data else 0, 0, 0, 0, 0, 0, 0, 0, 0
        )
        buf = io_hdr + cdb + sense_buffer + (data if data else b'')
        try:
            fcntl.ioctl(self.fd, SG_IO, buf)
            return True
        except OSError as e:
            print(f'SCSI failed: {e}')
            return False

    def decrypt_disc(self, disc_path: str) -> bool:
        # Initialize libdriveio
        if self.libdriveio:
            ret = self.libdriveio.DriveIO_Init(self.device.encode('utf-8'))
            if ret != 0:
                print('DriveIO_Init failed')
                return False

        # Select blob (placeholder index; implement hash match)
        blob_idx = 0
        blob = self.blobs.get(blob_idx)
        if not blob:
            print('No matching SDF blob')
            return False

        # Try DLL upload first
        if self.libdriveio:
            from ctypes import create_string_buffer
            blob_buf = create_string_buffer(blob)
            ret = self.libdriveio.DriveIO_UploadFirmware(self.device.encode('utf-8'), blob_buf, len(blob))
            if ret == 0:
                print('Firmware uploaded via libdriveio')
            else:
                print('DLL upload failed, falling back to SCSI')
                # Fallback to manual SCSI
                cdb = b'\x3B\x0F\x00' + len(blob).to_bytes(3, 'big') + b'\x00' * 3
                if not self._send_scsi_command(cdb, blob, direction=1):
                    print('SCSI upload failed')
                    return False
        else:
            # Manual SCSI upload
            cdb = b'\x3B\x0F\x00' + len(blob).to_bytes(3, 'big') + b'\x00' * 3
            if not self._send_scsi_command(cdb, blob, direction=1):
                print('SCSI upload failed')
                return False

        # AACS decryption
        self.title_keys = self.get_title_keys()
        print(f'Disc {disc_path} decrypted')
        return True

    def get_title_keys(self) -> List[bytes]:
        # Placeholder AES; integrate libmmbd.dll or keydb.cfg
        iv = b'\x00' * 16
        cipher = Cipher(algorithms.AES(self.volume_key), modes.CBC(iv), self.backend)
        encryptor = cipher.encryptor()
        title_key = encryptor.update(b'placeholder_unit_key') + encryptor.finalize()
        return [title_key]

# Example usage
# player = BluRayPlayer(encryption_handler=PurePythonLibreDriveHandler(
#     sdf_path='C:\\Users\\richa\\Downloads\\sdf_00000097.bin',
#     device='\\\\.\\D:',  # Windows device path
#     dll_path='C:\\Users\\richa\\Downloads\\Setup_MakeMKV_v1.18.1\\libdriveio64.dll'
# ))