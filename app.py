Last login: Sun Oct 25 11:00:40 on ttys000
d4lcaso@Skylynns-Air ~ % >....                                                  
    print("==================================================")
    print(f"Open the folder '{EXTRACT_FOLDER}' to examine manifests or property lists.")
    print("When your updates are completed, return here.")
    input("\n👉 Press [ENTER] to rebuild the firmware archive...")

    # 5. PACKAGING
    print(f"\n[4/4] 🗜️ Compiling files into {OUTPUT_IPSW}...")
    with zipfile.ZipFile(OUTPUT_IPSW, 'w', zipfile.ZIP_DEFLATED) as custom_zip:
        for root, _, files in os.walk(EXTRACT_FOLDER):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, EXTRACT_FOLDER)
                custom_zip.write(full_path, relative_path)
                
    print(f"\n🎉 Success! Output compiled at: {OUTPUT_IPSW}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Process canceled by user.")

