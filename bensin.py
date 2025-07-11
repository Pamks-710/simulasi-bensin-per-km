def hitung_bensin():
    try:
        jarak = float(input("Masukkan jarak perjalanan (km): "))
        konsumsi = float(input("Masukkan konsumsi bahan bakar kendaraan (km per liter): "))
        
        if konsumsi < 10:
            print("Boros dasar")

        harga_per_liter = float(input("Masukkan harga bensin per liter (Rp): "))
        
        if jarak <= 0 or konsumsi <= 0 or harga_per_liter <= 0:
            print("Jarak, konsumsi bahan bakar, dan harga bensin harus lebih dari 0 kang.")
            return
        
        

        bensin_dibutuhkan = jarak / konsumsi
        total_biaya = bensin_dibutuhkan * harga_per_liter

        print(f"\nBensin yang dibutuhkan: {bensin_dibutuhkan:.2f} liter")
        print(f"Perkiraan biaya bensin: Rp{total_biaya:,.2f}")

    except ValueError:
        print("Harap masukkan angka yang valid.")


hitung_bensin()
