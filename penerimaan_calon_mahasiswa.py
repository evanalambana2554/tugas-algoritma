def cek_syarat_penerimaan(nilai_matematika, nilai_bahasa_inggris, nilai_ipa):
    if nilai_matematika >= 80 and nilai_bahasa_inggris >= 75 and nilai_ipa >= 70:
        return True
    else:
        return False

nilai_matematika = float(input("Masukkan nilai Matematika: "))
nilai_bahasa_inggris = float(input("Masukkan nilai Bahasa Inggris: "))
nilai_ipa = float(input("Masukkan nilai IPA: "))

if cek_syarat_penerimaan(nilai_matematika, nilai_bahasa_inggris, nilai_ipa):
    print("Selamat! Anda memenuhi syarat untuk diterima sebagai mahasiswa baru.")
else:
    print("Maaf, Anda tidak memenuhi syarat untuk diterima sebagai mahasiswa baru.")