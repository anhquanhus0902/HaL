from Crypto.Signature import PKCS1_PSS as pkc
from Crypto.Hash import SHA1
a = pkc.pss
sig = a.PSS(SHA1.new(), mgf=a.MGF1(SHA1.new()), salt_length=a.PSS.MAX_LENGTH)
msg = b'abc'
sig