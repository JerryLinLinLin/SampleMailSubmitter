pyinstaller --noconfirm --log-level=WARN ^
    -F -w -n "SampleMailSubmitter" ^
    --add-data="locale;locale" ^
    --add-data="mail.ico;." ^
    --icon="mail.ico" ^
    --upx-exclude=vcruntime140.dll ^
    Main.py