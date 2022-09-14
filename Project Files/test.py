from main import arrange_path, main


# TODO: run test with -> pytest -s test.py
def test_main() -> None:
    assert main() is None


# TODO: Run this test if you are on Windows. Else, comment out.
# TODO: This is a test path, you can add a valid path to test.
def test_arrange_path_on_windows() -> None:
    assert arrange_path(r"C:\Users\USER\Downloads") is None


# TODO: Run this test if you are on MacOS or Linux. Else, comment out.
# TODO: This is a test path, you can add a valid path to test.
def test_arrange_path_on_macOS_and_linux() -> None:
    assert arrange_path("~/home/user/Downloads") is None


# TODO: Also comment out if you comment out the function above.
if __name__ == '__main__':
    test_arrange_path_on_windows()
    test_arrange_path_on_macOS_and_linux()
    main()
