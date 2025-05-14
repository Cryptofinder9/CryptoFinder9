# src/mnemonic_recovery.py
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins
def generate_mnemonic(strength: int = 128) -> str:
    """
    12 शब्दों वाली BIP39 mnemonic बनाएगा (default 128-bit strength).
    अगर 24 शब्द चाहिए, तो strength=256 सेट करें।
    """
    # FromWordsNumber(12) भी लिख सकते हैं, पर strength/32 करके automatically काम करता है
    return Bip39MnemonicGenerator().FromWordsNumber(int(strength / 32))
def derive_private_key(mnemonic: str, account_idx: int = 0) -> str:
    """
    दिए गए mnemonic से Bitcoin का पहला WIF-format private key निकालता है।
    """
    # Seed bytes बनाएँ
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_ctx = (
        Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
            .Purpose()
            .Coin()
            .Account(account_idx)
            .Change(False)
            .AddressIndex(0)
    )
    # WIF-format में private key लौटाएं
    return bip44_ctx.PrivateKey().ToWif()
