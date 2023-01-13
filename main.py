import module

if __name__ == "__main__":
    while True:
        choice = input("1. Manuel Denklem Girişi\n2. Dosyadan Denklem Girişi\n3. Çıkış\n")
        if choice == "1":
            module.solve_from_input()
        elif choice == "2":
            file_name = input("Dosya adını girin: ")
            module.solve_from_file(file_name)
        elif choice == "3":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
